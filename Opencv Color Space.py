import cv2,numpy as np,os
"""
cap=cv2.VideoCapture(0)
x=cv2.VideoWriter_fourcc("W","M","V",'2')
if cap.isOpened()==False:
    raise TimeoutError

framerate=30

VideoFile=cv2.VideoWriter("Ben.avi",x,framerate,(1000,1000))
while True:
    ret,frame=cap.read()
    if ret==0:
        break
    VideoFile.write(frame)
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
VideoFile.release()
cap.release()
cv2.destroyAllWindows()
"""
os.chdir("C:/Users/asus/Desktop/")
img=cv2.imread("C:/Users/asus/Desktop/Python-Code-Exercise/Gmail2.jpg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Renk Uzaylarını değiştirmek için kullanılır. Örneğin RGB'den BGR'a
#img1=cv2.imread("C:/Users/asus/Desktop/Python-Code-Exercise/Gmail2.jpg",cv2.IMREAD_GRAYSCALE)
#cv2.imwrite("Image.jpg",img1)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow("BGR",cv2.WINDOW_NORMAL)
cv2.namedWindow("RGB",cv2.WINDOW_NORMAL)
cv2.namedWindow("HSV",cv2.WINDOW_NORMAL)
cv2.namedWindow("Gray",cv2.WINDOW_NORMAL)
cv2.imshow("BGR",img)
cv2.imshow("RGB",img_rgb)
cv2.imshow("HSV",img_hsv)
cv2.imshow("Gray",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()