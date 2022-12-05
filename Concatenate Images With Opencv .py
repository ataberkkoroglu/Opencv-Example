import cv2,numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)+255
canvas2=np.zeros((512,512,3),dtype=np.uint8)+255
cv2.circle(canvas,(256,256),60,(0,0,255),-1)
cv2.rectangle(canvas,(230,230),(280,280),(255,0,0),-1)

print(canvas.shape)
image=canvas[196:316,196:316]
cv2.imshow("Canvas",canvas)
cv2.imshow("Croped Img",image)
cv2.rectangle(canvas2,(226,226),(286,286),(255,0,0),-1)
add=cv2.add(canvas,canvas2)
print(add[256,256])
cv2.imshow("Canvas2",add)
cv2.waitKey(0)
cv2.destroyAllWindows()