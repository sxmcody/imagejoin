
#### 介绍
无缝纵向拼接多张图片，最适合电商详情页切片拼接为完整图片，例如网店页面上保存的多张详情页图片，一键拼接为完整图片。
支持不同尺寸的图片拼接，以文件名排序第一张为基准

![](https://images.gitee.com/uploads/images/2021/0531/140629_d87ad00f_7977066.jpeg "长图的切片")

![](https://images.gitee.com/uploads/images/2021/0531/140718_f69b83ab_7977066.jpeg "拼接后效果")

#### 使用说明

1.  如不能导入PIL，则需安装pillow，可以命令行安装或者自行搜索pillow安装方法。
``` $ pip install pillow ```
2.  python文件可随意位置放置。
3.  图片需要事先确保拼接顺序与文件名排序一致，支持jpg、png混合拼接，输出图片为jpg。合成的图片以第一张图片的宽度尺寸为基准，所以务必要确保第一张图片是所需要的尺寸。
4.  运行后生成的图片保存在python文件目录下。

![](https://images.gitee.com/uploads/images/2021/0531/140742_132c0ba7_7977066.jpeg "运行时需要手动输入图片所在目录")

![](https://images.gitee.com/uploads/images/2021/0531/140816_05536e4a_7977066.jpeg "生成图片与python文件在同一目录")
