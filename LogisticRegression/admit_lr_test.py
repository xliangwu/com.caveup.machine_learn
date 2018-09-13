# 构建预测集
# 与训练集相似，一般也是通过 pd.read_csv() 读入
# 在这边为方便，我们将训练集拷贝一份作为预测集（不包括 admin 列）
import copy

import pandas as pd
from statsmodels.iolib.smpickle import load_pickle

data = pd.read_csv("../data/lr-binary.csv")
combos = copy.deepcopy(data)

print(combos.head())
# 数据中的列要跟预测时用到的列一致
predict_cols = combos.columns[1:]

# 预测集也要添加intercept变量
combos['intercept'] = 1.0

model = load_pickle("lr_admit.model")
print(model.summary())
# 进行预测，并将预测评分存入 predict 列中
print(model.predict(combos[predict_cols]))

# 预测完成后，predict 的值是介于 [0, 1] 间的概率值
# 我们可以根据需要，提取预测结果
# 例如，假定 predict > 0.5，则表示会被录取
# 在这边我们检验一下上述选取结果的精确度
total = 0
hit = 0
for value in combos.values:
    # 预测分数 predict, 是数据中的最后一列
    predict = value[-1]
    # 实际录取结果
    admit = int(value[0])

    # 假定预测概率大于0.5则表示预测被录取
    if predict > 0.5:
        total += 1
        # 表示预测命中
        if admit == 1:
            hit += 1

# 输出结果
print('Total: %d, Hit: %d, Precision: %.2f' % (total, hit, 100.0 * hit / total))
# Total: 49, Hit: 30, Precision: 61.22
