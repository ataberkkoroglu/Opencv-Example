import cv2

cap=cv2.VideoCapture("Webcam.avi") #WebCam Kamerası için 0 Kullan.

while True:
   ret,frame=cap.read()
   frame=cv2.flip(frame,1) #Görüntüyü Terse Çevirmek
   if ret==0:
      break
   cv2.imshow("Webcam",frame)
   #cv2.waitKey(1000) #Waitkey Fonksiyonu Frameyi Belirtilen Sürede Bekletir
   if cv2.waitKey(100) & 0xFF==ord("q"): #OxFF Klavyeden Veri Alabilmek için Kullanılır.
    break
   
cap.release() #İşlemi Kapatarak Video Üzerinde Yapılacak İşlemlere İzin Verir.
cv2.destroyAllWindows()   #Pencereleri Kapatır.