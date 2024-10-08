
#最近临近插值
import cv2
import numpy as np
def function(img):
    
    height,width,chananls = img.shape
    emptyImage=np.zeros((800,800,chananls),np.unit8)
    sh=800/height
    sw=800/width
    for i in range(800)
        for j in rang(800):
            x=int(i/sh+0.5)
            y=int(j/sw+0.5)
            emptyImage[i,j]=img[i,j]
    return emptyImage

#cv2.resize(img,(800,800,c),near/bin)

img=cv2.imread("lenna.png")
zoom=function(img)
print(zoom)
print(zoom.shape)
cv2.imshow("nearest interp",zoom)
cv2.imshow("image",img)
cv2.waitKey(0)

#---------------------------------------------------------------------------------------------

#双线性插值

import cv2
import numpy as np

def bilinear_interpolation(img,out_dim):
    src_h, src_w, channel = img.shape
    dst_h, dst_w = out_dim[1], out_dim[0]
    print ("src_h, src_w = ", src_h, src_w)
    print ("dst_h, dst_w = ", dst_h, dst_w)
    if src_h == dst_h and src_w == dst_w:
        return img.copy()
    dst_img = np.zeros((dst_h,dst_w,3),dtype=np.uint8)
    scale_x, scale_y = float(src_w) / dst_w, float(src_h) / dst_h
    for i in range(channel):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):
 
                # find the origin x and y coordinates of dst image x and y
                # use geometric center symmetry
                # if use direct way, src_x = dst_x * scale_x
                src_x = (dst_x + 0.5) * scale_x-0.5
                src_y = (dst_y + 0.5) * scale_y-0.5
 
                # find the coordinates of the points which will be used to compute the interpolation
                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0 + 1 ,src_w - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, src_h - 1)
 
                # calculate the interpolation
                temp0 = (src_x1 - src_x) * img[src_y0,src_x0,i] + (src_x - src_x0) * img[src_y0,src_x1,i]
                temp1 = (src_x1 - src_x) * img[src_y1,src_x0,i] + (src_x - src_x0) * img[src_y1,src_x1,i]
                dst_img[dst_y,dst_x,i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)
 
    return dst_img
 
 
if __name__ == '__main__':
    img = cv2.imread('lenna.png')
    dst = bilinear_interpolation(img,(700,700))
    cv2.imshow('bilinear interp',dst)
    cv2.waitKey()

#---------------------------------------------------------------------------------------------

#!/usr/bin/env python
#-*- coding:utf-8 -*-
#author FangKuaiRen time:2024-09-12
import cv2
import numpy as np
from matplotlib import pyplot as plt

# #灰度图像直方图均衡化
# img = cv2.imread("lenna.png",1)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #cv2.show("imge_gray",gray)
#
# dst = cv2.equalizeHist(gray)#灰度图像直方图均衡化
#
# hist = cv2.calcHist([dst],[0],None,[256],[0,256])#直方图
#
# plt.figure()
# plt.hist(dst.ravel(),256)
# plt.show()
#
# cv2.imshow("Histogram Equalization",np.hstack([gray,dst]))
# cv2.waitKey(0)

#------------------------------------

#彩色图像直方图均衡化
img = cv2.imread("lenna.png",1)
cv2.imshow("src",img)

#分解通道，每一个进行均衡化
(b,g,r) = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)

#合并每一个通道
result = cv2.merge((bH,gH,rH))
cv2.imshow("dst_rgb", result)

# result = cv2.merge((bH))
# cv2.imshow( result)
cv2.waitKey(0)
