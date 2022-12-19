import cv2

cap=cv2.VideoCapture("webcam.avi")

while 1:
    ret,frame=cap.read()
    if ret==False:
        break
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("Video",cv2.WINDOW_NORMAL)
    cv2.imshow("Video",frame)
    
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()