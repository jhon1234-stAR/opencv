import cv2

import numpy as np

image=cv2.imread ( "C:/Users/rache/OneDrive/Desktop/opencv/images/flower.webp" , 
                  cv2.IMREAD_COLOR),

border = cv2.copyMakeBorder( image , 4 , 4 , 4 ,4 , cv2.BORDER_CONSTANT,
value=[100,100,3])#bgr blue green red

carndall=np.ones((100,5), np.uint8 )

erosion= cv2.erode(border,carndall,iterations=1)

cv2.imshow("flower",erosion)

cv2.waitKey(0)

cv2.destroyAllWindows()