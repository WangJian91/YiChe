# -*- coding: utf-8 -*-

import os
import yaml
import jieba

# with open('./case.yaml', 'r', encoding='utf-8') as f:
#     data = yaml.load(stream=f, Loader=yaml.FullLoader)
#     print(data)

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
            # print(label)
            label, llm_result = label[0].lower(), llm_result.lower()
        label_words = set(self.cut_words(label, self.stopwords))
        llm_result_words = set(self.cut_words(llm_result, self.stopwords))
        same_words = list(label_words & llm_result_words)
        return label_words, llm_result_words, len(same_words) * 1.0 / len(label_words) if len(label_words) > 0 else 0


if __name__ == '__main__':
    similarity = JaccardSimilarity()
    text1 = "宝马5系"
    # text_list = ["奔驰E300", "宝马525", "宝马5系"]
    text_list = ["哈佛H6的配置", "哈佛H6的配置怎么样"]
    # text2 = "我想了解有关宝马5系的信息，有关它的性能、售价、口碑等。你能帮我吗？"
    # # text1_words, text2_words, result = similarity.similarity(text1, text2)
    # text1_words, text2_words, result = similarity.similarity(text_list, text2)
    # print(f'text1_words: {text1_words}\ntext2_words: {text2_words}')
    # print(f'result: {result}')
    text1_words, text2_words, result = similarity.similarity(text_list, "哈佛H6的配置怎么样")
    print(f'text1_words: {text1_words}\ntext2_words: {text2_words}')
    print(f'result: {result}')
