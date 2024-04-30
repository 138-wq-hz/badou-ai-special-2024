#!/usr/bin/env python
# encoding=gbk

import cv2  # ����OpenCV��
import numpy as np  # ����NumPy��
from matplotlib import pyplot as plt  # ��matplotlib���е���pyplotģ��

'''
equalizeHist��ֱ��ͼ���⻯
����ԭ�ͣ� equalizeHist(src, dst=None)
src��ͼ�����(��ͨ��ͼ��)
dst��Ĭ�ϼ���
'''

# ��ȡ��ɫͼ��
img = cv2.imread("lenna.png", 1)  # ��ȡ��ɫͼ��  ��flag��1��Ϊ0Ҳ���Ա�Ϊ�Ҷ�ͼ
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # ����ɫͼ��ת��Ϊ�Ҷ�ͼ��
cv2.imshow("image_gray", gray)  # ��ʾ��Ϊimage_gray�Ҷ�ͼ��
cv2.waitKey(0)  # �ȴ������¼�

# �Ҷ�ͼ��ֱ��ͼ���⻯
dst = cv2.equalizeHist(gray)  # �ԻҶ�ͼ�����ֱ��ͼ���⻯

# ����ֱ��ͼ
hist = cv2.calcHist([dst], [0], None, [256], [0, 256])

plt.figure()  # �����µ�ͼ��
plt.hist(dst.ravel(), 256)  # ����ֱ��ͼ
plt.show()  # ��ʾֱ��ͼ
cv2.imshow("Histogram Equalization", np.hstack([gray, dst]))  # ��ʾԭʼͼ��;��⻯���ͼ��
cv2.waitKey(0)  # �ȴ������¼�

# ----------------------------------------------------------------------------------------------------------------------
# ��ɫͼ��ֱ��ͼ���⻯
img = cv2.imread("lenna.png", 1)  # ��ȡ��ɫͼ��
cv2.imshow("src", img)  # ��ʾԭʼ��ͼ��

# ��ɫͼ����⻯,��Ҫ�ֽ�ͨ�� ��ÿһ��ͨ�����⻯
(b, g, r) = cv2.split(img)  # �����ɫͼ���ͨ��
bH = cv2.equalizeHist(b)  # ����ɫͨ������ֱ��ͼ���⻯
gH = cv2.equalizeHist(g)  # ����ɫͨ������ֱ��ͼ���⻯
rH = cv2.equalizeHist(r)  # �Ժ�ɫͨ������ֱ��ͼ���⻯
# �ϲ�ÿһ��ͨ��
result = cv2.merge((bH, gH, rH))  # �ϲ�������ͨ��
cv2.imshow("dst_rgb", result)  # ��ʾ���⻯��Ĳ�ɫͼ��

cv2.waitKey(0)  # �ȴ������¼�
