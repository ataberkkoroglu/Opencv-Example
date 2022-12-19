import cv2,numpy as np,os

filename="Ben.mp4"
cap=cv2.VideoCapture(0)
codec=cv2.VideoWriter_fourcc('m','p','4','v')

Video=cv2.VideoWriter(filename,codec,30,(640,480))

while True:
    ret,frame=cap.read()
    if ret==False:
        break
    Video.write(frame)
    cv2.imshow("Ben",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
