import json
import pandas as pd
# 标注周统计脚本
path1 = "C:/Users/wb_wangjian/Desktop/0605.json"
path2 = "C:/Users/wb_wangjian/Desktop/0606.json"
path3 = "C:/Users/wb_wangjian/Desktop/0607.json"
save_path = "C:/Users/wb_wangjian/Desktop/0611.xlsx"


def process():
    data1 = json.load(open(path1, "r"))
    data2 = json.load(open(path2, "r"))
    data3 = json.load(open(path3, "r"))

    ids, texts, labels, annots = [], [], [], []

    for d in data1+data2+data3:
        if "nlu" not in d: continue
        convds = d["convd"].split("\n")
        idx = d["id"]
        text, label, annot = "", "", ""
        for cv in convds:
            if "audio_msg" in cv:
                text = cv.split(":")[1].strip("\n")
            elif "user:"+text in cv:
                label = cv.split("    ")[1].split(":")[1].strip("\n")
        annot = d["nlu"]
        ids.append(idx)
        texts.append(text)
        labels.append(label)
        annots.append(annot)

    df = pd.DataFrame()
    df["ID"] = ids
    df["Text"] = texts
    df["Label"] = labels
    df["Annot"] = annots
    return df


def statistic(path):
    new_df = pd.read_excel(path)
    intent = set(new_df["Label"].values.tolist())

    for inte in intent:
        total = len(new_df[new_df["Label"] == inte].values.tolist())
        true = new_df["对比"][new_df["Label"] == inte].values.sum()
        print(inte, total, true, true/total)

    # df["意图"].value_counts()


if __name__ == "__main__":
    df = process()
    df.to_excel(save_path, index=None)
    # statistic(save_path)
