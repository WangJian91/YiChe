# encoding:utf-8

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.chat_models.base import BaseChatModel
from langchain import LLMChain, PromptTemplate
from typing import Any, List, Mapping, Optional
from tqdm import tqdm
import os
import jieba
import time
import json
import re
import queue
import asyncio
import traceback
import websockets


stopwords_path = os.path.join("./stop_words.txt")


class JaccardSimilarity:
    """
    根据文本相同词汇数目，计算相似性

    similarity = 相同词汇数目/总的词汇数目
    """

    def __init__(self):
        self.stopwords = self.load_stopwords()

    def load_stopwords(self):
        with open(stopwords_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]

    def cut_words(self, text, stopwords):
        return [word for word in jieba.lcut(text) if word not in stopwords]

    def similarity(self, text1: str, text2: str):
        text1 = text1.lower()
        text2 = text2.lower()
        text1_words = set(self.cut_words(text1, self.stopwords))
        text2_words = set(self.cut_words(text2, self.stopwords))

        all_words = list(text1_words | text2_words)
        same_words = list(text1_words & text2_words)
        return text1_words, text2_words, len(same_words)*1.0/len(all_words) if len(all_words) > 0 else 0


async def send_msg(websocket, prompt, r_queue):
    input_data = {
        "appId": "d3dfea3f-16d3-47b0-b1ca-2fee8e6ecd7c",  # llama
        # "appId": "5923bf20-4771-422e-9f76-9b8f0b9317c5",  # chatglm
        "version": "vicuna-13b",  # 如果没有找到会用默认的
        "userId": "OT0006",
        "userRequestId": "222",
        "requestId": "1111",
        "data": {
            "stream": False,
            # "logprobs": 5,
            "useRandom": False,
            "prompt": prompt,
            "topK": 1,
            "maxTokens": 2048,
            "stopWords": ["Observation", "Question"],
            "stopWordsIds": [[6039, 2140, 362], [13, 16492]],
        },
        "extra": {"rrrr": 666}
    }
    await websocket.send(json.dumps(input_data))
    recv_text = await websocket.recv()
    r_queue.put(recv_text)


async def main_logic(prompt, r_queue):
    # async with websockets.connect('ws://127.0.0.1:3000/infer/ws', ping_timeout=1000) as websocket:
    async with websockets.connect('ws://10.168.47.10:3000/infer/ws', ping_timeout=1000) as websocket:
        await send_msg(websocket, prompt, r_queue)


def Vicuna_13B_completion_api(query):
    """Vicuna_13B_completion_api"""
    start = time.time()
    try:
        r_queue = queue.Queue()
        # asyncio.run(main_logic("生成一个92年的个人介绍", r_queue))
        asyncio.run(main_logic(query, r_queue))
        recv_text = r_queue.get()
        recv_data = json.loads(recv_text)
        result_data = recv_data["data"]["result"]["text"]
        print(f'recv_data: {recv_data}')
        print(f'result_data: {result_data}')

    except BaseException as e:
        print('Vicuna_13B_completion_api: %s: %s' %
              (e, traceback.format_exc()))

    print(f'Vicuna_13B_completion_api request time: {time.time() - start}')
    return result_data


class Vicuna_13B(LLM):
    # class Vicuna_13B(BaseChatModel):

    # url: str
    # temperature: float

    @property
    def _llm_type(self) -> str:
        return "Vicuna_13B"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        # if stop is not None:
        #     raise ValueError("stop kwargs are not permitted.")

        result_data = Vicuna_13B_completion_api(prompt)
        result_data = result_data.lstrip('<s>').rstrip('</s>')
        result_data_part = result_data  # [len(prompt):]

        # stopWords = ["Observation", "Question"]
        result_data_part = result_data_part.replace(
            'Observation', '').replace('Question', '')

        if stop is not None:
            stop_idx = None
            for _stop in stop:
                if _stop in result_data_part:
                    stop_idx = result_data_part.index(_stop)

            if stop_idx:
                _result_data = result_data_part[:stop_idx]
            else:
                _result_data = result_data_part

            if "Question:" in _result_data:
                _idx = _result_data.index("Question:")
                _result_data = _result_data[:_idx]

            return _result_data

        return result_data_part

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model_type": "Vicuna_13B"}


def load_json_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json_file(path, obj):
    with open(path, 'w', encoding='utf8') as json_file:
        json.dump(obj, json_file, indent=4, ensure_ascii=False)


def parse_llm_output(llm_output: str):
    print(f"-------------- llm_output: {llm_output}")

    regex = r"Action\s*\d*\s*:(.*?)\nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
    match = re.search(regex, llm_output, re.DOTALL)

    if match:
        action = match.group(1).strip()
        action_input = match.group(2).strip().strip('"')
    else:
        # \nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)
        regex = r"Action\s*\d*\s*:[\s]*(.*)"
        match = re.search(regex, llm_output, re.DOTALL)
        if match:
            action = match.group(1).strip()
            action_input = ''
        else:
            print(ValueError(
                f"-------------- Could not parse LLM output: `{llm_output}`"))
            action, action_input = '', ''

    # print(f"-------------- action: {action}")
    # print(f"-------------- action_input: {action_input}")
    return action, action_input


template_en = """Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:

Vehicle parameter configuration: You just know vehicle parameter, eg: price, power, fuel, noise, internal configuration, space, comfort, color, vehicle manufacturer and other information, Action Input is the vehicle name value in conversation history and vehicle parameter.
Vehicle reviews and FAQ query: check the advantages and disadvantages of vehicles, reviews, driving experience, answer common questions about cars, recommend popular brands and models of vehicles.
Vehicle brand and series recognition: If '根据用户图片内容' not in 'Question: ', you absolutely not be able to use this tool.You can identify the brand and model of the vehicle in the picture, the input should be the user's picture.
Image content recognition: recognition and understand image content

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Vehicle parameter configuration, Vehicle reviews and FAQ query, Vehicle brand and series recognition, Image content recognition]
Action Input: the input to the action, including all car series and brand names extracted from the conversation history.
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: 我现在知道最终答案
Final Answer: 返回Observation的内容作为最终答案

Please note:

If you already know the answer to the question, be sure to output "Final Answer: Answer to the question" immediately.
如果"User:"中"图片内容"识别为"汽车", 务必选择"Vehicle Brand and Series Recognition"工具来确定车型车系.

Begin! Remember to speak as a pirate when giving your final answer. Use lots of "Arg"s

Conversation history:
{history}

Question: {input}
{agent_scratchpad}
Thought:"""


zh_en_mapping = {
    "车辆参配查询": "Vehicle parameter configuration",
    "汽车点评和常见问题查询": "Vehicle reviews and FAQ query",
    "车辆品牌车型识别": "Vehicle brand and series recognition",
    "图片内容识别": "Image content recognition",
}


stat = {
    "车辆参配查询": 0,
    "汽车点评和常见问题查询": 0,
    "车辆品牌车型识别": 0,
    "图片内容识别": 0,
}


zh_en_mapping_abbr = {}
template_en_abbr = {}


if __name__ == '__main__':
    chat_llm = Vicuna_13B()
    history_ = """User: 帕杰罗速跑最让人满意的是什么
                Agent: 帕杰罗速跑最让人满意的是它的外观设计，非常有个性，回头率很高。"""
    query_ = "价格多少"
    test_set_path = './case_0705.json'
    result_path = './case_result.json'
    use_abbr = False
    cnt = 0
    cnt_right = 0
    result = []
    cnt_action_input = 0
    sum_case = len(load_json_file(test_set_path))
    for it in tqdm(load_json_file(test_set_path)[:]):
        print(f'-------------- cnt: {cnt}, it: {it}')
        result_one = {}
        result_one["data"] = {}
        cnt += 1
        history = ["User: " + hist["user"] + "\n" +
                   "Agent: " + hist["agent"] for hist in it["history"]]
        history_str = '\n'.join(history)
        result_one["data"]["history"] = it["history"]
        query = it["question"]
        result_one["data"]["question"] = query
        label = it["action_label"]
        result_one["action_label"] = label
        info_action_input = it["action_input_info"]
        stat[label] += 1
        label_en = zh_en_mapping_abbr[label] if use_abbr else zh_en_mapping[label]
        prompt = PromptTemplate(
            input_variables=["history", "input", "agent_scratchpad"],
            template=template_en_abbr if use_abbr else template_en,
        )
        chain = LLMChain(
            llm=chat_llm,
            prompt=prompt,
            verbose=True,
        )
        try:
            result_data = chain.run(
                history=history_str, input=query, agent_scratchpad='')
            result_one["llm_result"] = result_data
            result_one["label_en"] = label_en
        except BaseException as e:
            print('chain.run: %s: %s' %
                  (e, traceback.format_exc()))
            result_one["llm_result"] = 'chain.run: %s: %s' % (
                e, traceback.format_exc())
            continue

        print(f'-------------- eval result_data: {result_data}')
        action, action_input = parse_llm_output(result_data)
        result_one["action_result"] = action
        result_one["action_input_info"] = info_action_input
        result_one["action_input_result"] = action_input
        score = 0

        # 对比action_input
        similarity = JaccardSimilarity()
        text1_words, text2_words, result_value = similarity.similarity(info_action_input, action_input)
        result_one["action_input_info_words"] = ', '.join(text1_words)
        result_one["action_input_result_words"] = ', '.join(text2_words)

        if label_en.lower() in action.lower():
            score = 1
            cnt_right += 1
        result_one["score"] = score
        result_one["result_value"] = result_value
        print(f'-------------- eval action_input_info: {info_action_input}')
        print(f'-------------- eval action_input_result: {action_input}')
        print(f'-------------- eval result_value: {result_value}')
        print(f"-------------- eval action_label: {label_en}")
        print(f"-------------- eval action_result: {action}")
        print(f'-------------- eval score: {score}')
        result.append(result_one)
        cnt_action_input += result_value
    result.append({"cnt": cnt, "cnt_right": cnt_right, "acc": cnt_right / cnt,
                   "avg_action_input": cnt_action_input / sum_case})
    result.append({"stat": stat})
    save_json_file(result_path, result)
    print(f'\n--------------finish--------------')
    print(f'-------------- eval cnt: {cnt}, cnt_right: {cnt_right}, acc: {cnt_right / cnt}, '
          f'avg_action_input: {cnt_action_input / sum_case}')
    print(f'-------------- eval stat: {stat}')
