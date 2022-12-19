import cv2,numpy as np,os
os.chdir("C:/Users/asus/Desktop/Fotoğraf İşlemleri")
img=cv2.imread("Ataberk.jpg",0)

row,col=img.shape
#print(f"Row: {row}\n Col: {col}")

M=np.float32([[1,0,50],[0,1,100]])
dst=cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
cv2.waitKey(0)