import cv2,time
from datetime import datetime
from PIL import Image,ImageColor,ImageEnhance,ImageFilter

"""
picture=Image.open("Gmail2.jpg")
picture.draft("RGB", (picture.width // 2, picture.height // 2))
print(picture.getbbox())
picture=picture.filter(ImageFilter.CONTOUR)
picture.save("Gmail.png")
picture.show()
"""
def Resize_with_aspect_ratio(img,width,height,inter=cv2.INTER_AREA):
    dimension=None
    
    (h,w)=img.shape[:2]
    if width is None and height is None:
        return img
    if width is None:
        r=height/float(h)
        dimension=(int(w*r),height)
    else:
        r=width/float(w)
        dimension=(width,int(h*r))
    
    return cv2.resize(img,dimension,interpolation=inter)
img=cv2.imread("Gmail2.jpg")
#img=cv2.imread("Gmail.png",cv2.IMREAD_GRAYSCALE)
#print(img)
img1=Resize_with_aspect_ratio(img,width=1900,height=1900)
cv2.imshow("Original",img)
cv2.imshow("Resized",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
cv2.namedWindow("Badem",cv2.WINDOW_NORMAL)
#cv2.resizeWindow("Badem",500,250)
img=cv2.resize(img,(500,500))
cv2.imshow("Badem",img)
cv2.imwrite("Gmail.png",img)
cv2.waitKey(0)
print(datetime.fromtimestamp(time.time()))
cv2.destroyAllWindows()
"""