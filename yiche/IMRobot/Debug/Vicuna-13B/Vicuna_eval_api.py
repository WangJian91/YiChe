# encoding:utf-8
import os
import time
import json
import re
from typing import Any, List, Mapping, Optional
import queue
import asyncio
import traceback
import websockets
from tqdm import tqdm
import jieba
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain import LLMChain, PromptTemplate


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
            # 1
            # # prompt 1
            # "stopWords": ["Observation", "Question", "Conversation history"],
            # "stopWordsIds": [[6039, 2140, 362], [13, 16492], [1168, 874, 362, 4955]],
            # prompt 2
            "stopWords": ["Observation", "Question", "Conversation history", "\n\n"],
            "stopWordsIds": [[6039, 2140, 362], [13, 16492], [1168, 874, 362, 4955], [13, 13]],
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
        asyncio.run(main_logic(query, r_queue))
        recv_text = r_queue.get()
        recv_data = json.loads(recv_text)
        result_data = recv_data["data"]["result"]["text"]
        print(f'recv_data: {recv_data}')
        print(f'result_data: {result_data}')
    except BaseException as e:
        print('Vicuna_13B_completion_api: %s: %s' %
              (e, traceback.format_exc()))
    print(
        f'Vicuna_13B_completion_api request time: {time.time() - start}')
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
            'Observation', '').replace('Question', '').replace('Conversation history', '')
        print(f'result_data_part: {result_data_part}')

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


def action_input_acc():
    file_paths = ['./case_0705_result_prompt1_0.53.json', './data/case_0705_result_prompt2_0.80.json']
    threshold = 0.6
    print(f'threshold: {threshold}')

    for file_path in file_paths:
        cnt = 0
        cnt_right = 0
        file_content = load_json_file(file_path)
        for it in file_content:
            data = it.get("data", None)
            if data:
                cnt += 1
                similarity = it["similarity"]
                if similarity >= threshold:
                    cnt_right += 1

        print(
            f'file_path: {file_path}, cnt: {cnt}, cnt_right: {cnt_right}, Acc: {cnt_right / cnt}')
    print(f'')
# action_input_acc()


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

    def similarity(self, label, llm_result: str):

        # label, llm_result = label.lower(), llm_result.lower()
        # label_words = set(self.cut_words(label, self.stopwords))
        # llm_result_words = set(self.cut_words(llm_result, self.stopwords))

        # 交并比
        # all_words = list(label_words | llm_result_words)
        # same_words = list(label_words & llm_result_words)
        # return label_words, llm_result_words, len(same_words) * 1.0 / len(all_words) if len(all_words) > 0 else 0

        # 交集
        # same_words = list(label_words & llm_result_words)
        # return label_words, llm_result_words, len(same_words) * 1.0 / len(label_words) if len(label_words) > 0 else 0
        if isinstance(label, str):
            label, llm_result = label.lower(), llm_result.lower()
        elif isinstance(label, list):
            for i in range(len(label) - 1):
                for j in range(len(label) - i - 1):
                    llm_result_words = set(self.cut_words(llm_result, self.stopwords))
                    label_words1 = set(self.cut_words(label[j], self.stopwords))
                    same_words1 = list(label_words1 & llm_result_words)
                    simi_value1 = len(same_words1) * 1.0 / len(label_words1)

                    label_words2 = set(self.cut_words(label[j + 1], self.stopwords))
                    same_words2 = list(label_words2 & llm_result_words)
                    simi_value2 = len(same_words2) * 1.0 / len(label_words2)
                    if simi_value1 < simi_value2:
                        label[j], label[j + 1] = label[j + 1], label[j]
            label, llm_result = label[0].lower(), llm_result.lower()
        label_words = set(self.cut_words(label, self.stopwords))
        llm_result_words = set(self.cut_words(llm_result, self.stopwords))
        same_words = list(label_words & llm_result_words)
        return label_words, llm_result_words, len(same_words) * 1.0 / len(label_words) if len(
            label_words) > 0 else 0


def parse_llm_output_prompt1(llm_output: str):
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

    print(f"-------------- action: {action}")
    print(f"-------------- action_input: {action_input}")
    return action, action_input


def parse_llm_output_prompt2(llm_output: str):
    print(f"-------------- llm_output: {llm_output}")

    if '问题未明确' in llm_output or '问题未知' in llm_output:
        action_input = ''
    else:
        action_input = llm_output.strip().split('\n')[0].strip()
        action_input = action_input.replace('`', '').strip()
        action_input = action_input.replace('用户问题是关于', '').replace('用户关注的是', '').replace(
            '用户想了解', '').replace('用户问的是关于', '').replace('用户想了解', '').replace(
            '用户想知道', '').replace('用户问的是', '').replace(
            '用户', '').replace('想', '').strip()
        # 用户 想了解 用户想 想 关注 用户问的是 用户想知道 用户问的是  models/data/case_0704_result_prompt2_0.50.json L402
        # 星越L价格 -> 星越L2.0T双离合两驱旗舰型的价格
        # 还能优惠吗？最低价多少？  ->  星越L2.0T车型的价格和是否有优惠。他们对车型的性能和内饰感兴趣，但对价格感到困惑，并询问是否可以

    action = 'Vehicle parameter configuration'

    print(f"-------------- action: {action}")
    print(f"-------------- action_input: {action_input}")
    return action, action_input


# prompt 1
template_en_1 = """Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:

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


# prompt 2
template_en_2 = """Answer the following questions as best you can.

根据对话历史，总结用户当前的问题。

Use the format in the example below:

<example>
Conversation history:
```
Here is the conversation history
```

总结结果: ```Here is the user question in summary```
</example>

Please note:
```
Be sure not to answer user questions, just summarize.
```

Begin!

Conversation history:
```
{history}
```

总结结果:"""


# 0.76
template_en_2_v1 = """Answer the following questions as best you can.

根据对话历史，总结用户当前的问题。

Use the format in the example below:

<example>
Conversation history:
```
User: 这款车的口碑怎样,
Agent: 根据已知信息，天籁这款车的口碑较好，消费者对其动力、操控、舒适性和空间等方面评价较高。但也有一些消费者对其外观和内饰提出了质疑。总体来说，天籁是一款性价比较高的中型车，值得消费者考虑。",
User: 售价多少,
Agent: 根据已知信息，天籁目前在售车型有2.0l和2.0t两款发动机可供选择，售价从17.98万元到26.98万元不等，目前厂家指导价优惠3万元左右，可以参考一下这个价格。因此，天籁 Observation ",
User: 变速箱怎样,
Agent: 天籁的工程师可能会告诉你，天籁使用的cvt变速箱表现很不错，具有平顺性、油耗和扭矩控制等优点。但是，cvt变速箱不太适合大排量发动机，因此可能无法提供与大排量发动机相匹配的驾驶体验。 "
User: 容易坏吗
```

总结结果: ```天籁质量怎么样？容易坏吗？```
</example>

Please note:
```
Be sure not to answer user questions, just summarize.
```

Begin!

Conversation history:
```
{history}
```

总结结果:"""


# prompt 3
prompt_xj = """You are a Language Retelling Engineer. Answer the following questions as best you can.
First you need to analyze the conversation history.
Extract dialogue logic and entity information that appears in the conversation history.

Then you need to complete the user question information based on the user question.
During the retelling generate, you can complete the following types of natural language processing tasks: 
eg: Chinese referential disambiguation tasks, complete dialogue discuss vehicle series in Retelling etc. 

<example>
```
Conversation history = [
User: 这款车的口碑怎样,
Agent: 根据已知信息，天籁这款车的口碑较好，消费者对其动力、操控、舒适性和空间等方面评价较高。但也有一些消费者对其外观和内饰提出了质疑。总体来说，天籁是一款性价比较高的中型车，值得消费者考虑。",
User: 售价多少,
Agent: 根据已知信息，天籁目前在售车型有2.0l和2.0t两款发动机可供选择，售价从17.98万元到26.98万元不等，目前厂家指导价优惠3万元左右，可以参考一下这个价格。因此，天籁",
User: 变速箱怎样,
Agent: 天籁的工程师可能会告诉你，天籁使用的cvt变速箱表现很不错，具有平顺性、油耗和扭矩控制等优点。但是，cvt变速箱不太适合大排量发动机，因此可能无法提供与大排量发动机相匹配的驾驶体验。"
]
```
User Question: '容易坏吗'
User Retelling Question: 天籁质量怎么样？容易坏吗？
</example>

Note: Ensure generated retelling to use the user's perspective and personal name.
Note: Please provide the generate in Chinese.

Now let's start retelling:
Conversation history = [ 
{history}
]
User Question: '{input}'
Thought: you should always think about what to do
User Retelling Question: """


# 0.72
prompt_xj_v1 = """You are a Language Retelling Engineer. 
First you need to analyze the conversation history.
Extract dialogue logic and entity information that appears in the conversation history.

Then you need to complete the user question information based on the user question.
During the retelling generate, you can complete the following types of natural language processing tasks: 
eg: Chinese referential disambiguation tasks, complete dialogue discuss vehicle series in Retelling etc. 

<example>
Conversation history:
```
Here is the conversation history
```
User Question: ```Here is the user question```
User Retelling Question: ``Here is the user retelling question```
</example>

Note: Ensure generated retelling to use the user's perspective and personal name.
Note: Please provide the generate in Chinese.

Now let's start retelling:
Conversation history:
```
{history}
```
User Question: ```{input}```
Thought: you should always think about what to do
User Retelling Question: """


# prompt 4
template_en_4 = """You are a Language Retelling Engineer. Answer the following questions as best you can.

根据对话历史，复述用户当前的问题。

Use the format in the example below:

<example>
Conversation history:
```
Here is the conversation history
```

复述结果: ```Here is the user question in summary```
</example>

Please note:
```
Be sure not to answer user questions, just summarize.
```

Begin!

Conversation history:
```
{history}
```

复述结果:"""


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

similarity = JaccardSimilarity()


if __name__ == '__main__':


    chat_llm = Vicuna_13B()
    test_set_path = './case_0714.json'
    result_path = './case_0714_result_prompt2.json'
    use_abbr = False

    cnt = 0
    cnt_right = 0
    similarity_sum = .0
    result = []
    for it in tqdm(load_json_file(test_set_path)[:]):
        print(f'-------------- cnt: {cnt}, it: {it}')
        result_one = dict()
        result_one["data"] = {}
        cnt += 1

        # history = ["User: " + hist["user"] + "\n" +
        #            "Agent: " + hist["agent"][:100] for hist in it["history"]]
        history = []
        for hist in it["history"]:
            if "agent" not in hist.keys():
                history.append("User: " + hist["user"])

            else:
                history.append("User: " + hist["user"] + "\n" + "Agent: " + hist["agent"][:100])
        history_str = '\n'.join(history)
        result_one["data"]["history"] = it["history"]

        query = it["question"]
        result_one["data"]["question"] = query

        label = it["action_label"]
        result_one["action_label"] = label
        stat[label] += 1

        label_en = zh_en_mapping_abbr[label] if use_abbr else zh_en_mapping[label]
        result_one["action_label_en"] = label_en

        action_input_info = it["action_input_info"]
        result_one["action_input_info"] = action_input_info

        # 3
        # # run prompt 1
        # prompt = PromptTemplate(
        #     input_variables=["history", "input", "agent_scratchpad"],
        #     template=template_en_1,
        # )

        # run prompt 2
        # prompt = PromptTemplate(
        #     input_variables=["history"],
        #     template=template_en_2,
        # )

        # run prompt 3
        prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=prompt_xj,
        )

        # # run prompt 4
        # prompt = PromptTemplate(
        #     input_variables=["history"],
        #     template=template_en_4,
        # )

        chain = LLMChain(
            llm=chat_llm,
            prompt=prompt,
            verbose=True,
        )

        try:
            # # prompt 1
            # result_data = chain.run(
            #     history=history_str, input=query, agent_scratchpad='')

            # # prompt 2
            # result_data = chain.run(
            #     history=history_str + f'\nUser: {query}' if history_str else f'User: {query}')

            # # prompt 3
            result_data = chain.run(
                history=history_str, input=query)

            # # prompt 4
            # result_data = chain.run(
            #     history=history_str + f'\nUser: {query}' if history_str else f'User: {query}')

            result_one["llm_result"] = result_data

        except BaseException as e:
            print('chain.run: %s: %s' %
                  (e, traceback.format_exc()))
            result_one["llm_result"] = 'chain.run: %s: %s' % (
                e, traceback.format_exc())
            continue

        # eval
        print(f'-------------- eval result_data: {result_data}')

        # 5
        # action, action_input = parse_llm_output_prompt1(result_data)
        action, action_input = parse_llm_output_prompt2(result_data)

        #
        action_input = action_input[:50] if action_input else query
        result_one["action"] = action
        result_one["action_input"] = action_input

        score = 0
        if action.lower() == label_en.lower():
            score = 1
            cnt_right += 1
        result_one["score"] = score
        print(f'-------------- eval score: {score}')

        label_words, llm_result_words, result_value = similarity.similarity(
            action_input_info, action_input)
        result_one["similarity"] = result_value
        result_one["action_input_info_words"] = ', '.join(list(label_words))
        result_one["action_input_words"] = ', '.join(list(llm_result_words))
        similarity_sum += result_value
        print(f'-------------- eval similarity: {result_value}')

        result.append(result_one)

        result.append({})
        result[-1] = {"cnt": cnt, "cnt_right": cnt_right,
                      "acc": cnt_right / cnt, "similarity": similarity_sum / cnt}
        result.append({})
        result[-1] = {"stat": stat}

        save_json_file(result_path, result)
        result.pop(-1)
        result.pop(-1)

    result.append({"cnt": cnt, "cnt_right": cnt_right,
                   "acc": cnt_right / cnt, "sicase_0710_result_prompt2.jsonmilarity": similarity_sum / cnt})
    result.append({"stat": stat})

    save_json_file(result_path, result)
    print(f'-------------- eval cnt: {cnt}, cnt_right: {cnt_right}, '
          + f'acc: {cnt_right / cnt},  similarity: {similarity_sum / cnt}')
    print(f'-------------- eval stat: {stat}')
