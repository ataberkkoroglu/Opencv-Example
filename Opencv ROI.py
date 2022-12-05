#Region of Interest
import cv2,os
os.chdir("C:/Users/asus/Desktop/Python-Code-Exercise")
img=cv2.imread("Gmail2.jpg",cv2.IMREAD_ANYCOLOR)
#print(img.shape[:2])

roi=img[200:500,400:800]
cv2.imshow("Gmail",img)
cv2.imshow("ROI",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()