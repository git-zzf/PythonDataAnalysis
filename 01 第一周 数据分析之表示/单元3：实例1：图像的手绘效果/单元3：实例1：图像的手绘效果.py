# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import os

path = "E:/Notes/PythonDataAnalysis/01 第一周 数据分析之表示/单元3：实例1：图像的手绘效果/"
if os.path.exists(path+"手绘Lenna.jpg"):
    os.remove(path+"手绘Lenna.jpg")
a = np.array(Image.open(path+"Lenna.jpg").convert('L')).astype('float') 

depth = 0.1			
grad = np.gradient(a)			
grad_x, grad_y = grad			
grad_x = grad_x*depth
grad_y = grad_y*depth

vec_el = np.pi/2.2
vec_az = np.pi/4
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.cos(vec_el)*np.sin(vec_az)
dz = np.sin(vec_el)

A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)
b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8'))
im.save(path+"手绘Lenna.jpg")