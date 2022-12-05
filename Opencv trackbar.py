import cv2,numpy as np 

def Nothing():
    pass

canvas=np.zeros((512,512,3),dtype=np.uint8)+255
cv2.namedWindow("Trackbar")
cv2.createTrackbar("R","Trackbar",0,255,Nothing)
cv2.createTrackbar("G","Trackbar",0,255,Nothing)
cv2.createTrackbar("B","Trackbar",0,255,Nothing)
Switch="0:OFF,1:ON"
cv2.createTrackbar(Switch,"Trackbar",0,1,Nothing)

while True:
    cv2.imshow("Trackbar",canvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    r=cv2.getTrackbarPos('R',"Trackbar")
    g=cv2.getTrackbarPos('G',"Trackbar")
    b=cv2.getTrackbarPos('B',"Trackbar")
    s=cv2.getTrackbarPos(Switch,"Trackbar")
    if s==0:
        canvas[:]=[0,0,0]
    else:
     canvas[:]=[b,g,r]
    
cv2.destroyAllWindows()