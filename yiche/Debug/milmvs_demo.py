#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/6/15 2:21 下午
# @Author  : fuyue
# @File    : milmvs_demo.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

# 导入相应的包
import numpy as np
from milvus import Milvus, MetricType

# pymilvus==1.1.2
# 初始化一个Milvus类，以后所有的操作都是通过milvus来的
milvus = Milvus(host='10.20.20.26', port='19530')


# 向量个数
num_vec = 5000
# 向量维度
vec_dim = 768
# name
collection_name = "test_collection"
# 创建collection，可理解为mongo的collection
collection_param = {
    'collection_name': collection_name,
    'dimension': vec_dim,
    'index_file_size': 32,
    'metric_type': MetricType.IP  # 使用内积作为度量值
}
milvus.create_collection(collection_param)

# 随机生成一批向量数据
# 支持ndarray，也支持list
vectors_array = np.random.rand(num_vec, vec_dim)

# 把向量添加到刚才建立的collection中
status, ids = milvus.insert(collection_name=collection_name, records=vectors_array)  # 返回 状态和这一组向量的ID
milvus.flush([collection_name])

# 输出统计信息
print(milvus.get_collection_stats(collection_name))

# 创建查询向量
query_vec_array = np.random.rand(1, vec_dim)
# 进行查询,
status, results = milvus.search(collection_name=collection_name, query_records=query_vec_array, top_k=5)
print(status)
print(results)

# 如果不用可以删掉
status = milvus.drop_collection(collection_name)

# 断开、关闭连接
milvus.close()