import cv2

import numpy as np

image=cv2.imread ( "C:/Users/rache/OneDrive/Desktop/opencv/images/flower.webp")

carndall=np.ones((100,5), np.uint8 )

erosion= cv2.erode(image,carndall,iterations=1)

cv2.imshow(" original image", image)

cv2.imshow("blurred image",erosion)

cv2.waitKey(0)

cv2.destroyAllWindows()
