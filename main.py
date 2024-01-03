import cv2

#Configurable Parameters
source="IMG_20230313_115552.png"
destination="newImage.png"
scale_percent=50

image=cv2.imread(source,cv2.IMREAD_UNCHANGED)
#cv2.imshow("title",image)

#Calculating the new dimensions 
width=int(image.shape[1]*scale_percent/100)  #new
height=int(image.shape[0]*scale_percent/100)  #new

dsize=(width,height)

output=cv2.resize(image,dsize)

cv2.imwrite(destination,output)
cv2.waitKey(0)