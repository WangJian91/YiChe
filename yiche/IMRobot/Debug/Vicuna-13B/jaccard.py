# -*- coding: utf-8 -*-
import os
import jieba
import json

#
# stopwords_path = os.path.join("./stop_words.txt")
#
#
# class JaccardSimilarity():
#     """
#     根据文本相同词汇数目，计算相似性
#
#     similarity = 相同词汇数目/总的词汇数目
#     """
#
#     def __init__(self):
#         self.stopwords = self.load_stopwords()
#
#     def load_stopwords(self):
#         with open(stopwords_path, 'r', encoding='utf-8') as f:
#             return [line.strip() for line in f]
#
#     def cut_words(self, text, stopwords):
#         return [word for word in jieba.lcut(text) if word not in stopwords]
#
#     def similarity(self, text1: str, text2: str):
#         text1 = text1.lower()
#         text2 = text2.lower()
#         text1_words = set(self.cut_words(text1, self.stopwords))
#         text2_words = set(self.cut_words(text2, self.stopwords))
#         print(text1)
#         print(text2)
#         print('-'*20)
#         print(text1_words)
#         print(text2_words)
#         print('-'*20)
#         all_words = list(text1_words | text2_words)
#         same_words = list(text1_words & text2_words)
#         print(f'all_words:{all_words}')
#         print(f'same_words:{same_words}')
#         return text1_words, text2_words, len(same_words)*1.0/len(all_words) if len(all_words) > 0 else 0





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
        return label_words, llm_result_words, len(same_words) * 1.0 / len(label_words) if len(label_words) > 0 else 0


def load_json_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':

    test_set_path = './case_0704.json'

    text1 = "525"
    text2 = "525的同级车"

    text1 = "宝马525LI多少钱"
    text2 = "宝马5系、525 Li豪华型、61.2万元"

    text1 = "宝马525LI怎么样"
    text2 = "宝马525LI"

    text1 = "天籁打蜡的好处"
    text2 = "车子打蜡的好处"

    text1 = "奔驰E级车的价格"
    text2 = "这款奔驰E级车的价格多少？"

    text1 = "宝马6系GT是否适合一家六口"
    text2 = "这是一辆适合六人的宝马6系GT车"

    text1 = "图片中的车辆的燃油消耗情况"
    text2 = "风骏5的油耗"

    text1 = "评价宝马6系GT后驱车冬天开怎么样"
    text2 = "宝马6系GT车在冬天是否适合开车？后驱车在冬天开怎么样？"

    text1 = "韩系车销量不好的原因"
    text2 = "为什么韩系车销量不好？我了解一下。"

    text1 = "宝马5系"
    text2 = "我想了解有关宝马5系的信息，有关它的性能、售价、口碑等。你能帮我吗？"

    similarity = JaccardSimilarity()
    text1_words, text2_words, result = similarity.similarity(text1, text2)
    print(f'text1_words: {text1_words}\ntext2_words: {text2_words}')
    print(f'result: {result}')
