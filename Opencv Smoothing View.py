import cv2,numpy as np,os
from PIL import Image,ImageColor,ImageFilter

os.chdir("C:/Users/asus/Desktop/Fotoğraf İşlemleri")
"""image=Image.open("Ataberk.jpg")
image=image.convert(mode='L')"""
#image2=image.filter(ImageFilter.GaussianBlur(45))
#image.save("Ataberk.png")

img=cv2.imread("Ataberk.jpg")
image2=img
image3=img
"""blur=cv2.blur(img,(20,20))
cv2.imshow("AtaberkBlur",blur)
blur2=cv2.blur(image2,(20,20))
cv2.imshow("Ataberk",img)"""
image3=img
image4=img
"""cv2.imwrite("AtaberkBlur.jpg",blur)
cv2.imwrite("AtaberkBlur.jpg",blur2)"""
Img=cv2.cvtColor(image2,cv2.COLOR_BGR2HSV)
Img=cv2.GaussianBlur(image2,(5,5),cv2.BORDER_DEFAULT)
visual=cv2.medianBlur(image3,5)
visual2=cv2.bilateralFilter(image4,9,85,75)
#cv2.imwrite("AtaberkHSV.png",Img)

cv2.imshow("Gaussian Blur",Img)
cv2.imshow("Median Blur",visual)
cv2.imshow("Bilateral",visual2)
cv2.waitKey(0)
cv2.destroyAllWindows()
