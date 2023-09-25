# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# 一、 生成数据表
data_file = pd.DataFrame(pd.read_excel('./结构化工具问题汇总.xlsx'))  # 导入excel文件

# data_file = pd.DataFrame(pd.read_json('./data0.json'))        # 导入json文件

# data_file = pd.DataFrame(pd.read_csv('./label.csv'))      # 导入CSV文件
# print(data_file)

# 构建数据表
df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20130102', periods=6),
                   "city": ['beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32],
                   "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]},
                  columns=['id', 'date', 'city', 'category', 'age', 'price'])

# 二、 数据表信息查看
# print(data_file.shape)   # 维度查看(几行,几列)

# print(df.info)      # 查看数据表基本信息
# print(data_file.info)

# print(df.dtypes)
# print(data_file.dtypes)     # 获取每一列数据的格式

# print(df['id'].dtype)       # 获取某一列格式
# print(data_file['问题'].dtype)       # 获取某一列格式

# print(df.isnull())      # 查看是否有空值
# print(df['price'].isnull())      # 查看某一列是否有空值

# print(df.values)  # 查看数据表的值,返回numpy.ndarray
# print(data_file.values)
# print(data_file.values[0])
# for d in data_file.values:
#     print(d)

# print(df.columns)       # 查看列名称
# print(data_file.columns)       # 查看列名称

# print(df.head())      # 默认前5行数据

# print(df.tail())        # 默认后5行数据


# 三、数据表清洗
# print(df.fillna(value=0))     # 用数字0填充空值,不修改原数据
# print(df['price'].fillna(df['price'].mean()))      # 使用列price的均值对NA进行填充,不修改原数据

# df['city'] = df['city'].map(str.strip)        # 清除city字段的字符空格,是一个动作

# df['city'] = df['city'].str.lower()       # 将city字段的字符转换为小写
# df['city'] = df['city'].str.upper()       # 将city字段的字符转换为大写
# print(df.info)

# print(df)
# print(df['price'].fillna(df['price'].mean()).astype('int'))       # 更改数据格式,不能有空值(NaN)

# print(df)
# print(df.rename(columns={'category': 'category-size'}))     # 更改列名称,不修改原数据

# print(df)
# print(df['city'].str.upper().drop_duplicates())     # 删除后出现的重复值

# print(df)
# print(df['city'].str.upper().drop_duplicates(keep='last'))  # 删除先出现的重复值

# print(df)
# print(df['city'].replace('SH', 'shanghai'))


# 四、数据预处理
df1 = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
                    "gender": ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
                    "pay": ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y', ],
                    "m-point": [10, 12, 20, 40, 40, 40, 30, 20]})

# 数据表合并
# 1. merge 必须有相同字段用来匹配
# print(df)

df = pd.merge(df, df1, how='inner')  # 匹配合并，交集，内连接，只合并能匹配到的
# print(df_inner)

# df_left = pd.merge(df, df1, how='left')     # 左连接，以左侧数据为主，匹配不到的行补NaN
# print(df_left)

# df_right = pd.merge(df, df1, how='right')     # 右链接，以右侧数据为主，匹配不到的行补NaN
# print(df_right)

# df_outer = pd.merge(df, df1, how='outer')  # 并集，匹配不到的行补NaN
# print(df_outer)

# 2. append pandas2.0以后已经弃用 会报错DataFrame has no attribute 'append'
# result = df.append(df1)
# print(result)
# print(pd.__version__)

# 3. join   # 如果两个表有相同的字段，必须为左右字段添加区分的字符 lsuffix='_left', rsuffix='_right' 否则报错columns overlap but no suffix specified
# result = df.join(df1, lsuffix='_left', rsuffix='_right')
# print(result)

# 4. concat     # 根据字段进行合并
# df3 = pd.concat([df, df1], axis=0, join='outer', ignore_index=False,
#                 keys=None, levels=None, names=None, verify_integrity=False,
#                 copy=True)
# print(df3)
"""
objs︰ 一个序列或系列、 综合或面板对象的映射。如果字典中传递，将作为键参数，使用排序的键，除非它传递，在这种情况下的值将会选择
（见下文）。任何没有任何反对将默默地被丢弃，除非他们都没有在这种情况下将引发 ValueError。
axis: {0，1，…}，默认值为 0。要连接沿轴。
join: {‘内部’、 ‘外’}，默认 ‘外’。如何处理其他 axis(es) 上的索引。联盟内、 外的交叉口。
ignore_index︰ 布尔值、 默认 False。如果为 True，则不要串联轴上使用的索引值。由此产生的轴将标记
0，…，n-1。这是有用的如果你串联串联轴没有有意义的索引信息的对象。请注意在联接中仍然受到尊重的其他轴上的索引值。
序列，默认为无。构建分层索引使用通过的键作为最外面的级别。如果多个级别获得通过，应包含元组。
levels︰ 列表的序列，默认为无。具体水平 （唯一值） 用于构建多重。否则，他们将推断钥匙。
names︰ 列表中，默认为无。由此产生的分层索引中的级的名称。
verify_integrity︰ 布尔值、 默认 False。检查是否新的串联的轴包含重复项。这可以是相对于实际数据串联非常昂贵。
副本︰ 布尔值、 默认 True。如果为 False，请不要，不必要地复制数据。
"""

# df.set_index('id')    # 设置索引列

# print(df.sort_values(by=['age'], ascending=False))    # 按照特定列的值排序ascending空值数字的升降序

# print(df.sort_index(ascending=False))   # 按照索引排序ascending空值数字的升降序


# 如果price列的值>3000，group列显示high，否则显示low：
# df['group'] = np.where(df['price'] > 3000, 'high', 'low')
# print(df)


# 对复合多个条件的数据进行分组标记
# df.loc[(df['age'] > 23) & (df['price'] >= 4000), 'sign'] = 1
# print(df)

# 对category字段的值按需进行分列，并创建数据表，索引值为df的索引列，列名称分别为category和size
# dff = pd.DataFrame((x.split('-') for x in df['category']), index=df.index, columns=['category', 'size'])
# print(dff)


# 五、数据提取
# print(df.loc[2])   # 按索引提取单行的数值

# print(df.loc[0:4])   # 按索引提取单行的数值，开区间

# print(df.iloc[0:3])     # 按索引提取区域行数值, 闭区间

# df.reset_index()    # 重设索引
# print(df)

# print(df)
# df = df.set_index('date')     # 设置日期为索引

# print(df[:'2013-01-04'])      # 提取4号之前的所有数据，包括4号

# print(df)
# print(df.iloc[:3, :2])      # 使用iloc按位置区域提取数据,冒号前后的数字不再是索引的标签名称，而是数据所在的位置，从0开始，前三行，前两列。

# print(df)
# print(df.iloc[[0, 2, 5], [4, 5]])   # 按位置单独提取数据,按索引提取第0、2、5行的4、5列

# print(df.ix[:'2013-01-03', :4])     #  #2013-01-03号之前，前四列数据pandas2.0废弃了这个方法

# print(df['city'].isin(['shanghai']))     # 判断city列的值是否为shanghai 返回True、False

# print(df.loc[df['city'].isin(['beijing', 'shanghai'])])     # 判断city列里是否包含beijing或者shanghai，然后将符合条件的数据提取出来

# ndf = pd.DataFrame(df['category'].str[:3])  # 提取前三个字符，并生成新数据表
# print(ndf)


# 六、数据筛选
# 使用“与”进行筛选
# print(df)
# print(df.loc[(df['age'] > 22) & (df['city'] == 'beijing '), ['id', 'city', 'age', 'category', 'gender']])

# 使用“与”进行筛选,并按照age字段排序 默认是升序
# print(df)
# print(df.loc[(df['age'] > 25) | (df['city'] == 'beijing '),
#              ['id', 'city', 'age', 'category', 'gender']].sort_values(['age']))

# 使用“非”条件进行筛选,按照id字段排序 默认是升序
# print(df)
# print(df.loc[(df['city'] != 'beijing '), ['id', 'city', 'age', 'category', 'gender']].sort_values(['id']))

# 对筛选后的数据按age列进行计数
# print(df)
# print(df.loc[(df['city'] != 'beijing '), ['id', 'city', 'age', 'category', 'gender']].age.count())

# 使用query函数进行筛选，此处是或的关系
# print(df.query('city == ["beijing ", "shanghai"]'))

# 对筛选后的结果按price进行求和
# print(df)
# print(df.query('city == ["beijing ", "shanghai"]').price.sum())

# 七、数据汇总
# 主要函数是groupby和pivote_table
# 对所有的列进行计数汇总
# print(df.groupby('city').count())

# 按城市对id字段进行计数
# print(df.groupby('city')['id'].count())

# 对两个字段进行汇总计数
# print(df.groupby(['city', 'age'])['id'].count())

# 对city字段进行汇总，并分别计算price的计数合计和均值
# print(df.groupby('city')['price'].agg([len, np.sum, np.mean]))


# 八、数据统计
# 数据采样，计算标准差，协方差和相关系数
# 简单的数据采样,随机3行
# print(df.sample(n=3))

# 手动设置采样权重,权重？
# weights = [0, 0, 0, 0, 0.5, 0.5]
# print(df.sample(n=2, weights=weights))

# 采样后不放回
# print(df)
# print(df.sample(n=6, replace=False))

# 采样后放回
# print(df)
# print(df.sample(n=6, replace=True))

# 数据表描述性统计
# print(df.describe().round(2).T)     # round函数设置显示小数位，T表示转置

# 计算列的标准差
# print(df['price'].std())

# 计算两个字段间的协方差
# print(df)
# print(df['price'].cov(df['m-point']))

# 两个字段的相关性分析
# print(df)
# print(df['price'].corr(df['m-point']))   # 相关系数在-1到1之间，接近1为正相关，接近-1为负相关，0为不相关

# df.to_excel('test.xlsx', sheet_name='测试')

# df.to_csv('test_to.csv')


