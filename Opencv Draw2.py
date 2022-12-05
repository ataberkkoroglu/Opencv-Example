import cv2,numpy as np

Canvas=np.zeros((512,512,3),dtype=np.uint8)+255

#canvas=cv2.imread("Canvas.png")
cv2.line(Canvas,(50,50),(512,512),(0,0,255),5)
cv2.line(Canvas,(10,500),(5,5),(255,0,0),7)

cv2.rectangle(Canvas,(20,20),(50,50),(0,255,0),-1)
cv2.circle(Canvas,(250,250),100,(0,0,255),-1)
cv2.imshow("Canvas",Canvas)

#os.remove("Canvas.png")
#print(os.access("Canvas.png",os.X_OK))
#cv2.imwrite("Canvas.png",Canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
