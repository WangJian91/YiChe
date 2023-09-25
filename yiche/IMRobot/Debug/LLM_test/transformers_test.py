# -*- coding: utf-8 -*-

import transformers
from accelerate import dispatch_model
from transformers import LlamaForCausalLM, LlamaTokenizer


models_path = "/chengxiaojie/vicuna/vicuna-13b"
models_path = "./vicuna-13b-v1.3"
models_path = "./vicuna-13b-v1.5-16k"
tokenizer = LlamaTokenizer.from_pretrained(models_path)


prompt = """You are a Language Retelling Engineer. Answer the following questions as best you can.
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
User: 图片内容：这是一辆宝马6系GT车
]
User Question: '女朋友特喜欢，不过会不会太大？'
Thought: you should always think about what to do
User Retelling Question: """


prompt = """Given the following user prompt and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.
  You should follow the following rules when generating and answer:
  - Always prioritize the user prompt over the conversation log.
  - Ignore any conversation log that is not directly related to the user prompt.
  - Only attempt to answer if a question was posed.
  - The question should be a single sentence.
  - You should remove any punctuation from the question.
  - You should remove any words that are not relevant to the question.
  - If you are unable to formulate a question, respond with the same USER PROMPT you got.
  - The generated question must be in Chinese.

USER PROMPT: 和宝马6GT相比呢？

CONVERSATION LOG: User: 图片内容：奥迪RS 7
根据用户图片内容，这是什么车
Agent: 奥迪RS 7是一款中大型跑车，搭载4.0TV型八缸涡轮增压发动机和8档手自一体变速箱，最大功率441千瓦，最大扭矩800牛米，百公里加速时间只需要3.9秒，最高车速可以达到250千米每时。rs 7在外
User: 它的配置怎么样？
Agent: 奥迪RS7是一款高性能的跑车，配置非常豪华，拥有多种不同的配置，包括运动风格座椅、皮质座椅、运动外观套件、铝合金轮圈等。此外，它还提供了多种不同的颜色和内部颜色，让用户可以根据自己的喜好进行选择。在座


Final answer: """


prompt = """You are a Language Retelling Engineer. Answer the following questions as best you can.
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
User: 宝马有前驱车吗
Agent: 我们无法得知天籁车是否有前驱车。
]
User Question: '新款glc没有点烟器，那要是想买个车载冰箱怎么办'
Thought: you should always think about what to do
User Retelling Question: """


prompt = """You are a Language Retelling Engineer. Answer the following questions as best you can.
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
User: 零跑C11空调真的不行吗？
Agent: 根据您提供的信息，我无法确定您的天籁C11零跑空调是否存在问题。空调是一个复杂的系统，可能存在多种原因导致它不起作用。如果您的空调已经出现了问题，
User: 宝马3是前驱车么
Agent: 宝马3系的车身设计是后轮驱动，而不是前轮驱动。这意味着宝马3系的车身结构比较简单，承载能力好，操控性能也很好。但是，宝马3系的车身结构比较大，耗油量也比较大。如果你需要更好的维护行车安全性，
]
User Question: '5系呢'
Thought: you should always think about what to do
User Retelling Question: """


prompt = """You are a Language Retelling Engineer. Answer the following questions as best you can.
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
User: 宝马有前驱车吗
Agent: 我们无法得知天籁车是否有前驱车。
]
User Question: '新款glc没有点烟器，那要是想买个车载冰箱怎么办'
Thought: you should always think about what to do
User Retelling Question: """


inputs = tokenizer(prompt, return_tensors='pt')


model = LlamaForCausalLM.from_pretrained(models_path, trust_remote_code=True, device_map='auto').half().eval()


"""
device_map = {'model.embed_tokens': 0, 'model.layers.0': 0,
              'model.layers.1': 0, 'model.layers.2': 0,
              'model.layers.3': 0, 'model.layers.4': 0,
              'model.layers.5': 0, 'model.layers.6': 0,
              'model.layers.7': 0, 'model.layers.8': 0,
              'model.layers.9': 0, 'model.layers.10': 0,
              'model.layers.11': 0, 'model.layers.12': 0,
              'model.layers.13': 0, 'model.layers.14': 0,
              'model.layers.15': 0, 'model.layers.16': 0,
              'model.layers.17': 0, 'model.layers.18': 0,
              'model.layers.19': 0, 'model.layers.20': 0,
              'model.layers.21': 0, 'model.layers.22': 0,
              'model.layers.23': 0, 'model.layers.24': 0,
              'model.layers.25': 0, 'model.layers.26': 0,
              'model.layers.27': 0, 'model.layers.28': 0,
              'model.layers.29': 0, 'model.layers.30': 0,
              'model.layers.31': 0, 'model.layers.32': 1,
              'model.layers.33': 1, 'model.layers.34': 1,
              'model.layers.35': 1, 'model.layers.36': 1,
              'model.layers.37': 1, 'model.layers.38': 1,
              'model.layers.39': 1, 'model.norm': 1, 'lm_head': 0}
model = dispatch_model(model.half(), device_map=device_map)
model.eval()
"""

hf_config = vars(model.config)
# print(hf_config)
# generated_ids = model.forward(inputs.input_ids, output_hidden_states=True)
# print(generated_ids)
generate_ids = model.generate(inputs.input_ids.cuda(), max_length=2048)
res = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
print(res)

