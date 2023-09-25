# -*- coding: utf-8 -*-
import tiktoken
import transformers
import time
import json

# # enc = tiktoken.get_encoding('cl100k_base')
enc = tiktoken.get_encoding('p50k_base')
# enc = tiktoken.get_encoding('r50k_base')
# enc = tiktoken.get_encoding('gpt2')
tokens = enc.encode("""You are a Language Retelling Engineer. Answer the following questions as best you can.
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
User Retelling Question: 如果新款的glc没有点烟器，那如果想买个车载冰箱的话，该怎么办？""")
tokens = enc.encode("""\n\nYou are responsible for creating a new language that is easy to learn and use, but also has a unique and interesting structure. Your goal is to make the language as simple as possible while still""")
tokens = enc.encode("""\n\nYou are responsible for creating a new language that is easy to learn and use, but also has a unique and interesting structure. Your goal i""")
tokens = enc.encode("""\n\nYou are responsible for creating a new language that is easy to learn and use, but also""")
tokens = enc.encode("""你是一个资深劳动合同拟定师，需要尽可能详细的拟定一份4530字的劳动合同，其中需要2000字的劳动仲裁法，2000多字的公司职工保护义务法
""")

print(tokens)
print(len(tokens))

# li = [1, 887, 526, 263, 4086, 3240, 7807, 22055, 29889, 3492, 526, 14040
#     , 363, 4969, 263, 716, 4086, 29889, 9190, 29892, 3113, 14944, 278, 4086
#     , 366, 505, 2825, 29889, 3529, 3867, 278, 1024, 310, 278, 4086, 29892
#     , 967, 3978, 322, 738, 2472, 1048, 278, 4086, 393, 723, 367, 5545
#     , 4100, 491, 263, 4856, 6509, 278, 4086, 13, 13, 797, 445, 3414
#     , 29892, 306, 505, 2825, 263, 716, 4086, 2000, 376, 29911, 261, 1705
#     , 613, 607, 338, 263, 26797, 1848, 4086, 393, 306, 505, 2825, 29889
#     , 450, 3978, 310, 445, 4086, 338, 515, 263, 2215, 29899, 2696, 15754
#     , 2000, 376, 29911, 261, 336, 1642, 450, 4086, 756, 1063, 8906, 975
#     , 17202, 310, 2440, 322, 756, 263, 5412, 25437, 322, 5877, 393, 338
#     , 3755, 1422, 515, 738, 4086, 19182, 373, 11563]
#
# print(len(li))

