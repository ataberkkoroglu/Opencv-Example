import cv2,numpy as np,os
os.chdir("C:/Users/asus/Desktop/Fotoğraf İşlemleri")
img=cv2.imread("Ataberk.jpg",0)

row,col=img.shape
M=cv2.getRotationMatrix2D((col/2,row/2),180,1)
dst=cv2.warpAffine(img,M,(col,row))
cv2.imshow("Image",dst)
cv2.waitKey(0)