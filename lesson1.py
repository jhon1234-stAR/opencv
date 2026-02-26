import cv2

#### imread -> this function readug the image or telling
#  the system that where we have kept the image

image=cv2.imread ( "C:/Users/rache/OneDrive/Desktop/opencv/images/cat.jpg" , 
                  cv2.IMREAD_COLOR)
# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR ( 1 ) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE ( 0 ) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED ( -1 ) => Specify to load the image unchanged

#imshow function -> for showing the image on a new windoW

cv2.imshow ( "modefied item", image )

##to hold the window until the user presses a key on the kyboard 

cv2.waitKey(0)

## delete / close the image window after the key pressed 

cv2.destroyAllWindows()
#made but in greyscale
image=cv2.imread ( "C:/Users/rache/OneDrive/Desktop/opencv/images/cat.jpg" , 
                  0 )
cv2.imshow ( "modefied item", image )
cv2.waitKey(0)
cv2.destroyAllWindows()