#!/usr/bin/env python
# Copyright (c) Baidu apollo, Inc.
# All Rights Reserved

import os
import random

pngfilepath = r'./labels'
saveBasePath = r"./"

temp_png = os.listdir(pngfilepath)
total_png = []
for png in temp_png:
    if png.endswith(".txt"):
        id = str(int(png.split('.')[0])).zfill(6)
        total_png.append(id + '.jpg')

print("---  iter for image finished ---")

train_percent = 0.85
val_percent = 0.1
test_percent = 0.05

num = len(total_png)
# train = random.sample(num,0.9*num)
list = list(range(num))

num_train = int(num * train_percent)
num_val = int(num * val_percent)


train = random.sample(list, num_train)
num1 = len(train)
for i in range(num1):
    list.remove(train[i])

val_test = [i for i in list if not i in train]
val = random.sample(val_test, num_val)
num2 = len(val)
for i in range(num2):
    list.remove(val[i])


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:                   # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  creating new folder...  ---")
        print("---  finished  ---")
    else:
        print("---  pass to create new folder ---")


mkdir(saveBasePath)

ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')

for i in train:
    name = './images/' + total_png[i][:-4] + '.jpg' + '\n'
    ftrain.write(name)


for i in val:
    name = './images/' + total_png[i][:-4] + '.jpg' + '\n'
    fval.write(name)


for i in list:
    name = './images/' + total_png[i][:-4] + '.jpg' + '\n'
    ftest.write(name)

ftrain.close()
