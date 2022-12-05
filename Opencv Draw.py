import numpy as np
import cv2,os
"""
cap=cv2.VideoCapture(0)

while(1):
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1)==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
"""
canvas=np.zeros((512,512,3),dtype=np.uint8)+255

os.chdir("C:/Users/asus/Desktop/")
cv2.imshow("Canvas",canvas)
a=cv2.imread("Clock.jpg")
a=cv2.resize(a,(500,500))
cv2.imshow("Clock",a)
cv2.waitKey(0)
cv2.destroyAllWindows()



