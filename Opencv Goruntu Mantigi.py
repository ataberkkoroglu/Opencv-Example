import cv2,numpy as np

#img=np.zeros((10,10,3),dtype=np.uint8)
img=np.zeros((20,20),dtype=np.uint8)
"""
img[0,0]=(255,255,255)
img[0,1]=(255,255,200)
img[0,2]=(255,255,150)
img[0,3]=(255,255,15)
"""

for i in range(0,20):
 sayı=255   
 for e in range(0,20):  
  img[i,e]=sayı
  sayı -=10
 img=cv2.resize(img,(1500,1500),interpolation=cv2.INTER_AREA)
cv2.imshow("Canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()