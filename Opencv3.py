import cv2,os,sys
from datetime import datetime
cap=cv2.VideoCapture(0)
filename=f"{os.getcwd()}/Webcam.avi"
#os.makedirs("Opencv/opencv")
#os.removedirs("Opencv/opencv")

codec=cv2.VideoWriter_fourcc("W","M","V",'2')
frameRate=30
resloution=(640,480)
VideoFileOutput=cv2.VideoWriter(filename,codec,frameRate,resloution)
while(1):
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    cv2.imshow("Frame",frame)
    VideoFileOutput.write(frame)
    if ret==False:
        break
    if cv2.waitKey(1) & 0xFF==ord('q'): #0xFF:to Take Data From Keyboard
        break
VideoFileOutput.release()
cap.release()

print(datetime.ctime(datetime.fromtimestamp(os.stat("Webcam.avi").st_atime)))
print(help(os.path.dirname))
cv2.destroyAllWindows()