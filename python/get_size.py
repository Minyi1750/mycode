# encoding=utf-8
# Purpose: 获取指定目录下文件夹的大小
# Create Time: 2021.04.28 17:52
import os
from os.path import join, getsize
import sys


def get_item_size(item):
    item_size = None
    mb = 1024.0 * 1024.0

    if os.path.isfile(item):
        item_size = getsize(item) / mb
    elif os.path.isdir(item):
        file_size_list = []

        for root, dirs, files in os.walk(item):
            # u'\\\\?\\' windows C盘执行如果没有会遇见报错
            file_size_list.append(sum(getsize(u'\\\\?\\' + join(root, name)) for name in files))
        item_size = sum(file_size_list) / mb
    else:
        print('{} is not regular file or directory')

    print('{},{:.4f},MB'.format(item, item_size))


if len(sys.argv) != 2:
    print('Usage: python {} <DIRECTORY>'.format(sys.argv[0]))
else:
    for i in os.listdir(sys.argv[1]):
        get_item_size(os.path.join(sys.argv[1], i))
