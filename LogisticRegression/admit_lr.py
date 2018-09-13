import copy

import pandas as pd
import pylab as pl
import statsmodels.api as sm

# load data
df = pd.read_csv("../data/lr-binary.csv")
print(df.head())

df.columns = ["admit", "gre", "gpa", "prestige"]
print(df.columns)
# Index(['admit', 'gre', 'gpa', 'prestige'], dtype='object')

# summarize the data
print(df.describe())
#             admit         gre         gpa   prestige
# count  400.000000  400.000000  400.000000  400.00000
# mean     0.317500  587.700000    3.389900    2.48500
# std      0.466087  115.516536    0.380567    0.94446
# min      0.000000  220.000000    2.260000    1.00000
# 25%      0.000000  520.000000    3.130000    2.00000
# 50%      0.000000  580.000000    3.395000    2.00000
# 75%      1.000000  660.000000    3.670000    3.00000
# max      1.000000  800.000000    4.000000    4.00000

# 查看每一列的标准差
print(df.std())
# admit      0.466087
# gre      115.516536
# gpa        0.380567
# prestige   0.944460

# 频率表，表示prestige与admin的值相应的数量关系
print(pd.crosstab(df['admit'], df['prestige'], rownames=['admit']))

# prestige   1   2   3   4
# admit
# 0         28  97  93  55
# 1         33  54  28  12

# plot all of the columns
df.hist()
pl.show()

# 将prestige设为虚拟变量
dummy_ranks = pd.get_dummies(df['prestige'], prefix='prestige')
print(dummy_ranks.head())
#    prestige_1  prestige_2  prestige_3  prestige_4
# 0           0           0           1           0
# 1           0           0           1           0
# 2           1           0           0           0
# 3           0           0           0           1
# 4           0           0           0           1

# 为逻辑回归创建所需的data frame
# 除admit、gre、gpa外，加入了上面常见的虚拟变量（注意，引入的虚拟变量列数应为虚拟变量总列数减1，减去的1列作为基准）
cols_to_keep = ['admit', 'gre', 'gpa']
data = df[cols_to_keep].join(dummy_ranks.ix[:, 'prestige_2':])
print(data.head())
#    admit  gre   gpa  prestige_2  prestige_3  prestige_4
# 0      0  380  3.61           0           1           0
# 1      1  660  3.67           0           1           0
# 2      1  800  4.00           0           0           0
# 3      1  640  3.19           0           0           1
# 4      0  520  2.93           0           0           1

# 需要自行添加逻辑回归所需的intercept变量
data['intercept'] = 1.0

print(">>>start to logic")
# 指定作为训练变量的列，不含目标列`admit`
train_cols = data.columns[1:]
# Index([gre, gpa, prestige_2, prestige_3, prestige_4], dtype=object)

logit = sm.Logit(data['admit'], data[train_cols])

# 拟合模型
result = logit.fit()
print(result.summary())
result.save("lr_admit.model")

combos = copy.deepcopy(data)
print(combos.head())
# 数据中的列要跟预测时用到的列一致
predict_cols = combos.columns[1:]

# 预测集也要添加intercept变量
combos['intercept'] = 1.0
combos['predict'] = result.predict(combos[predict_cols])

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
print(combos)
print('Total: %d, Hit: %d, Precision: %.2f' % (total, hit, 100.0 * hit / total))
# Total: 49, Hit: 30, Precision: 61.22
