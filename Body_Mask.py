import cv2,numpy as np 

cap=cv2.VideoCapture(0)

def nothing():
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",(512,512))

cv2.createTrackbar("Lower-H","Trackbar",0,180,nothing)
cv2.createTrackbar("Lower-S","Trackbar",0,255,nothing)
cv2.createTrackbar("Lower-V","Trackbar",0,255,nothing)

cv2.createTrackbar("Upper-H","Trackbar",0,180,nothing)
cv2.createTrackbar("Upper-S","Trackbar",0,255,nothing)
cv2.createTrackbar("Upper-V","Trackbar",0,255,nothing)

cv2.setTrackbarPos("Lower-H","Trackbar",180)
cv2.setTrackbarPos("Lower-S","Trackbar",255)
cv2.setTrackbarPos("Lower-V","Trackbar",255)

cv2.setTrackbarPos("Upper-H","Trackbar",180)
cv2.setTrackbarPos("Upper-S","Trackbar",255)
cv2.setTrackbarPos("Upper-V","Trackbar",255)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    h1=cv2.getTrackbarPos("Lower-H","Trackbar")
    s1=cv2.getTrackbarPos("Lower-S","Trackbar")
    v1=cv2.getTrackbarPos("Lower-V","Trackbar")
    
    h2=cv2.getTrackbarPos("Upper-H","Trackbar")
    s2=cv2.getTrackbarPos("Upper-S","Trackbar")
    v2=cv2.getTrackbarPos("Upper-V","Trackbar")
    lower_color=np.array([h1,s1,v1])
    upper_color=np.array([h2,s2,v2])
    
    mask=cv2.inRange(hsv,lower_color,upper_color)
    cv2.imshow("Original",frame)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(20) &0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()