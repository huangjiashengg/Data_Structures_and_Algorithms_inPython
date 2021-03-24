import jieba.analyse
import jieba.posseg
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.model_selection import train_test_split
item_info_set = set()
item_info_set.add("时间都去哪儿了王铮亮")
item_info_set.add("小酒窝林俊杰")
item_info_set.add("漫步人生路邓丽君")
item_info_set.add("讲真的曾惜")
item_info_set.add("再次见到你金娜英")
item_info_set.add("大鱼周深")
item_info_set.add("暗里着迷刘德华")
item_info_set.add("青空拂晓车站")
item_info_set.add("一生所爱大话西游")
item_info_set.add("一个人过冬天宋世贤")
item_info_set.add("一个人挺好王雨笙")

token_set = set()
item_set = set()
item_fs_dict = {}
for name in item_info_set:
    item_set.add(name)
    token_score_list = []
    for x, w in jieba.analyse.extract_tags(name, withWeight=True):
        token_score_list.append((x, w))
        token_set.add(x)
    item_fs_dict[name] = token_score_list

token_id_dict = {}
for s in enumerate(list(token_set)):
    token_id_dict[s[1]] = s[0]

item_id_dict = {}
for s in enumerate(list(item_set)):
    item_id_dict[s[1]] = s[0]

item_fea_dict = {}
user_feature_offset = 10
for name, fea in item_fs_dict.items():
    token_score_list = []
    for (token, score) in fea:
        if token not in token_id_dict:
            continue
        token_id = token_id_dict[token] + user_feature_offset
        token_score_list.append(':'.join([str(token_id), str(score)]))

    #接下来输出到字典中
    item_fea_dict[name] = '\t'.join(token_score_list)


# """
out_file = open("output_item_feature_file.txt", 'w')
for name, fea in item_fea_dict.items():
    if name not in item_id_dict:
        continue
    item_id = str(item_id_dict[name])
    out_file.write('\t'.join([item_id, fea]))
    out_file.write('\n')

out_file.close()


def load_data():
    # 由于在计算过程用到矩阵计算，这里我们需要根据我们的数据设置行，列，和训练的数据准备
    # 标签列表
    target_list = []
    # 行数列表
    fea_row_list = []
    # 特征列表
    fea_col_list = []
    # 分数列表
    data_list = []

    # 设置行号计数器
    row_idx = 0
    max_col = 0

    with open("output_item_feature_file.txt", 'r') as fd:
        for line in fd:
            ss = line.strip().split('\t')
            # 标签
            label = ss[0]
            # 特征
            fea = ss[1:]
            # 将标签放入标签列表中
            target_list.append(int(label))

            for fea_score in fea:
                sss = fea_score.strip().split(':')
                if len(sss) != 2:
                    continue
                feature, score = sss
                # 增加行
                fea_row_list.append(row_idx)
                # 增加列
                fea_col_list.append(int(feature))
                # 填充分数
                data_list.append(int(round(float(score))))
                if int(feature) > max_col:
                    max_col = int(feature)

            row_idx += 1

    row = np.array(fea_row_list)
    col = np.array(fea_col_list)
    data = np.array(data_list)

    fea_datasets = csr_matrix((data, (row, col)), shape=(row_idx, max_col + 1))
    x_train, x_test, y_train, y_test = train_test_split(fea_datasets, target_list, test_size=0.4, random_state=0)
    return x_train, x_test, y_train, y_test

x_train, x_test, y_train, y_test = load_data()
print(x_test)
print("-"*20)
print(x_train)
print("-"*20)
print(y_train)
print("-"*20)
print(y_test)
# """


