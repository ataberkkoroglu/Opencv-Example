import cv2, numpy as np,os
from matplotlib import pyplot as plt
#os.chdir("C:/Users/asus/Desktop/Fotoğraf İşlemleri")
img=cv2.imread("F22.jpg",0)
ret,th1=cv2.threshold(img,150,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)
#cv2.imshow("F22",img)
cv2.imshow("F22_1",th1)
cv2.imshow("F22_2",th2)
cv2.imshow("F22_3",th3)
cv2.waitKey(0)