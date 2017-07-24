"""
仅作为笔记
"""
import csv

#将数据读取为元组序列

with open('stocks.csv') as f:
    f_csv=csv.reader(f)
    headers=next(f_csv)
    for row in f_csv:
        #row将是元组

#将数据取为字典序列

with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        #可以用过行标头来访问每行中的元素

#将读取以TAB键分隔的数据
with open('stocks.tsv') as f:
    f_csv=csv.reader(f,delimiter='\t')
    for row in f_csv:

#读取csv数据并将其转换为命名元组时，如果标题行中有非法标识符，会出现ValueErrors
#解决：：对非法字符进行正则替换

import re
from collections import namedtuple
with open('stocks.csv') as f:
    f_csv=csv.reader()
    headers=[re.sub('[^a-zA-Z_]','_',h) for h in next(f_csv)]
    Row=namedtuple('Row',headers)
    for r in f_csv:
        row=Row(*r)

#Pandas 中有一个方便的函数 pandas.read_csv()
