import cv2

import numpy as np

image=cv2.imread("C:/Users/rache/OneDrive/Desktop/opencv/images/eye.jpg")
                  
#convert to greyscale

gsclae = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#algorith, tjat we will be using for detecting cirles 
#can only be done on grayscale images

#blur image

blurred = cv2.blur(gsclae,(3,3))

#bluring reduces  the noice
#----.>unwanted backround or unwanted stuff

#decting the cirles 

circles=cv2.HoughCircles(blurred,cv2.HOUGH_GRADIENT,
                         1,20,param1=30,param2=50,
                         minRadius=1,maxRadius=40)

#(x,y,radius)-> returns this value if the cirle is found none if not found

#parameters hough cirle function
#blureed->blurred image
#cv2.houghgrafient -> modify the imgage to gradient image
#1 (dp) -> ratio of image resolution to gradient image
#2 means half of the origonal image resolution in temrs of width and hieght

#20-> minDist -> min distance between the centers of the detected circles. 
#Helps in repeated detection of the same circle
#param 1 is gradient value used in edge detection
#param2 is minimum number of votes required to detcte as a circle
#check if circles were found

if circles is not None:
    circles = np.uint16(np.around(circles))

#draw the cirle wherever detected
for i in circles [0,:]:

    x,y,r = i[0],i[1],i[2]

    cv2.circle(image,(x,y),r,(0,0,225),2)

    cv2.circle(image,(x,y),1,(0,0,225),2)

    cv2.imshow("eye",image)
    
cv2.waitKey(0)

cv2.destroyAllWindows()   