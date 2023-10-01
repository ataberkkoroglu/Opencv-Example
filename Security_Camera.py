import cv2,winsound,os

cap=cv2.VideoCapture(0)
cv2.namedWindow("Frame",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Frame",720,720)
i=0
os.chdir("C://Users//Asus//Desktop")
while cap.isOpened():

    _,frame=cap.read()
    _,frame2=cap.read()

    diff=cv2.absdiff(frame,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
      if cv2.contourArea(contour)<5000:
         continue
      x,y,w,h=cv2.boundingRect(contour)
      if i==0:
        cv2.imwrite(f"{os.getcwd()}/Enemy.png",frame[y:y+h,x:x+w])
        
      else:
        cv2.imwrite(f"{os.getcwd()}/Enemy{i}.png",frame[y:y+h,x:x+w]) 
      i=i+1
      cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
      winsound.PlaySound('alert.wav',winsound.SND_ASYNC)
        
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
    cv2.imshow("Frame",frame)
cap.release()
cv2.destroyAllWindows()