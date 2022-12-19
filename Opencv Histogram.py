from matplotlib import pyplot as plt
import cv2,numpy as np,os

"""img=np.zeros((500,500,3),np.uint8)+50
cv2.rectangle(img,(0,60),(250,150),(255,0,255),-1)
cv2.circle(img,(250,250),50,(0,0,255),-1)
cv2.line(img,(100,100),(200,200),(255,0,0),5)"""

os.chdir("C:\\Users\\asus\Desktop\\Fotoğraf İşlemleri")
img=cv2.imread("Ataberk.jpg")

b,g,r=cv2.split(img)
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
cv2.imshow("img",img)
#plt.hist(img.ravel(),256,[0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()