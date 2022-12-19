import cv2,numpy as np

img=cv2.imread("F22.jpg",0)
kernel=np.ones((10,10),np.uint8)
erosion=cv2.erode(img,kernel,iterations=5) #inceltme
dilation=cv2.dilate(img,kernel,iterations=5) #Kalınlaştırma
closing=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("Image",img)
cv2.imshow("Closing",closing)
cv2.imshow("Erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

