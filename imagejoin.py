# -*- coding: UTF-8 -*-
#无缝拼接多张图片，拼接生成的图片位于与python文件同目录下。由于是通过数组拼接，所以要求待拼接的图片宽度必须完全一致。
import numpy as np
import os
from PIL import Image

imgdir = input("请输入图片文件夹地址:") #指定图片位置，形如：D:\Pictures
allfiles = os.listdir(imgdir)

#用filter()函数过滤仅保留图片格式文件，留下的进入列表
def file_filter(f):
    if f[-4:] in ['.jpg','.png','.bmp']:
        return True
    else:
        return False

images = list(filter(file_filter,allfiles))

im = []  #建立一个列表，后面将数组存储到列表中

for image in images:
    #依次打开图片（输入的路径+图片文件名得到实际图片路径）
    imgopen = Image.open(imgdir+"\\"+image)
    im.append(np.array(imgopen))  #转化为ndarray对象并存入列表

imgjoin = np.concatenate(im,axis = 0)  #拼接图片，axis=0为纵向拼接
imgcreate = Image.fromarray(imgjoin)  #生成图片
imgcreate.save('final.jpg')  #保存图片并以final.jpg命名
