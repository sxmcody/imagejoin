# -*- coding: UTF-8 -*-
#无缝拼接多张图片，拼接生成的图片位于与python文件同目录下。
#将第一张图片宽度尺寸作为基准，其余图片将更改为与其一致。

import numpy as np
import os
from PIL import Image

def main():
    imgdir = input("请输入图片文件夹地址:") #指定图片位置，形如：D:\Pictures
    allfiles = os.listdir(imgdir)

    #用filter()函数过滤仅保留图片格式文件，留下的进入列表
    def file_filter(f):
        if f[-4:] in ['.jpg','.png','.bmp']:
            return True
        else:
            return False

    images = list(filter(file_filter,allfiles))
    images.sort(key = lambda x:int(x[:-4])) #对图片进行排序
    new_images = []  #建立一个列表，稍后依次将打开的图片存入其中

    resized_images = []  #建立一个新列表，稍后将更改过图片尺寸后的图片存入其中


    for image in images:
        #依次打开图片（输入的路径+图片文件名得到实际图片路径）
        imgopen = Image.open(imgdir +"\\"+ image)
        new_images.append(imgopen)  #将图片存入列表
       
    #通过循环，将列表里的每张图片的宽度尺寸以第一张图片为基准重设
    for im in new_images:
        if im == new_images[0]:  #第一张图片略过处理
            pass
        elif im.size[0]== new_images[0].size[0]:  #增加一个判断，如果图片与第一张图片宽度一样，那么略过重设大小
            pass
        else:
            im = im.resize((new_images[0].size[0],int(new_images[0].size[0]*im.size[1]/im.size[0])),Image.ANTIALIAS)
        resized_images.append(np.array(im))  #将更改过尺寸的图片转化为ndarray对象并存入列表

    imgjoin = np.concatenate(resized_images,axis = 0)  #拼接图片，axis=0为纵向拼接
    imgcreate = Image.fromarray(imgjoin)  #生成图片
    imgcreate.save('final.png')  #保存图片并以final.png命名，经测试，png可以最低程度地减少图片质量损失

if __name__ == '__main__':
    main()

