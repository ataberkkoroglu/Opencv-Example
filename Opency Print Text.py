import cv2,numpy as np

canvas=np.zeros((1500,1500,3),dtype=np.uint8)+255
cv2.putText(canvas,"Would You Like To Drink Coffee from Starbucks?",(10,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,255,0),cv2.LINE_4)
#Yazı Yazdırmak İçin PutText Fonksiyonu Kullanılır.

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
