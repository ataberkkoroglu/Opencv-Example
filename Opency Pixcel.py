import cv2,os,numpy as np 

os.chdir("C:/Users/asus/Desktop/Python-Code-Exercise")

#canvas=np.zeros((512,512,3),dtype=np.uint8)+255

canvas=cv2.imread("Gmail2.jpg",cv2.IMREAD_COLOR)
dimension=canvas.shape
color=canvas[330,600]

#canvas=cv2.resize(canvas,(512,512))
print("BGR: ",color)
blue=canvas[330,600,0]
canvas[330,600,0]=250
print(f"Old blue Value: {blue} New Blue Value: {canvas[330,600,0]}")
blue1=canvas.item(330,600,0)
print(f"blue1: {blue1}")
canvas.itemset((330,600,0),172)
print("new blue1: ",canvas[330,600,0])
green=canvas[330,600,1]
print("green: ",green)
red=canvas[330,600,2]
print("Red: ",red)
cv2.imshow("Image",canvas)
cv2.waitKey(0)
