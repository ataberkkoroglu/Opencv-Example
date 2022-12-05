import cv2,numpy,requests,os
url="http://192.168.1.32:8080/shot.jpg"
filename="C://Users/asus/Desktop/Home.mp4"
codec=cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
frameRate=30
resolution=(640,480)
VideoFileOutput=cv2.VideoWriter(filename,codec,frameRate,resolution)
while True:
    img_resp=requests.get(url)    
    img_arr=numpy.array(bytearray(img_resp.content),dtype=numpy.uint8)
    img=cv2.imdecode(img_arr,cv2.IMREAD_COLOR)
    VideoFileOutput.write(img_arr)
    img=cv2.resize(img,(1600,900))
    cv2.imshow("Android Camera",img)
    
    if cv2.waitKey(1)==ord('q'):
        break
    
cv2.destroyAllWindows()