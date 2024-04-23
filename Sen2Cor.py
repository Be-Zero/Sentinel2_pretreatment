# coding:utf-8
import os
from fnmatch import fnmatch, fnmatchcase
import shutil


# data = []
# for line in open(r'E:\project\NDVI_DFI_model\5.txt', 'r', encoding='gbk', errors='ignore'):
#     data.append(line[-39:-1])
#
# for f in os.listdir(r'E:\Sentinel-2\5'):
#     if f not in data:
#         shutil.move('E:/Sentinel-2/5/' + f, 'E:/Sentinel-2/tmp/' + f)

data = []
path = os.listdir(r'F:\9')
for p in path:
    if fnmatch(p, 'S2B_MSIL2A*'):
        data.append(p[11:44])

print(data)

for p in path:
    if fnmatch(p, 'S2B_MSIL1C*') and p[11:44] in data:
        print(p)

