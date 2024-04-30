#!/usr/bin/env python
# encoding=gbk

import cv2  # ����OpenCV��
import numpy as np  # ����NumPy��
from matplotlib import pyplot as plt  # ��Matplotlib���е���pyplotģ�飬���ڻ�ͼ

img = cv2.imread("lenna.png", 1)  # ��ȡ��Ϊ"lenna.png"�Ĳ�ɫͼ��
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # ����ɫͼ��ת��Ϊ�Ҷ�ͼ��

'''
Sobel����
Sobel���Ӻ���ԭ�����£�
dst = cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) 
ǰ�ĸ��Ǳ���Ĳ�����
��һ����������Ҫ�����ͼ��
�ڶ���������ͼ�����ȣ�-1��ʾ���õ�����ԭͼ����ͬ����ȡ�Ŀ��ͼ�����ȱ�����ڵ���ԭͼ�����ȣ�
dx��dy��ʾ�����󵼵Ľ�����0��ʾ���������û���󵼣�һ��Ϊ0��1��2��
����ǿ�ѡ�Ĳ�����
dst��Ŀ��ͼ��
ksize��Sobel���Ӻ˵Ĵ�С������Ϊ1��3��5��7��
scale�����ŵ����ı���������Ĭ�������û������ϵ����
delta��һ����ѡ������������ӵ����յ�dst�У�ͬ����Ĭ�������û�ж����ֵ�ӵ�dst�У�
borderType���ж�ͼ��߽��ģʽ���������Ĭ��ֵΪcv2.BORDER_DEFAULT��
'''

# Sobel��������   ������ͼ��ֱ��ʾ��ԭʼͼ����ˮƽ�ʹ�ֱ�����ϵı�Ե��Ϣ  ksize��������Ϊ3����ʾʹ��3x3��Sobel���Ӻ�
img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)  # ��x�������Sobel��������
img_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)  # ��y�������Sobel��������

# Laplace ����
img_laplace = cv2.Laplacian(img_gray, cv2.CV_64F, ksize=3)  # ʹ��Laplace���Ӽ��ͼ���Ե

# Canny ����
img_canny = cv2.Canny(img_gray, 100, 150)  # ʹ��Canny���ӽ��б�Ե���

plt.subplot(231), plt.imshow(img_gray, "gray"), plt.title("Original")  # ����ԭʼ�Ҷ�ͼ��
plt.subplot(232), plt.imshow(img_sobel_x, "gray"), plt.title("Sobel_x")  # ����Sobel x������ͼ��
plt.subplot(233), plt.imshow(img_sobel_y, "gray"), plt.title("Sobel_y")  # ����Sobel y������ͼ��
plt.subplot(234), plt.imshow(img_laplace, "gray"), plt.title("Laplace")  # ����Laplace���Ӽ��ı�Եͼ��
plt.subplot(235), plt.imshow(img_canny, "gray"), plt.title("Canny")  # ����Canny��Ե�����ͼ��
plt.show()  # ��ʾ���Ƶ�ͼ��
