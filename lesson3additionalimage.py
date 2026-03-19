import cv2

image=cv2.imread ( "C:/Users/rache/OneDrive/Desktop/opencv/images/cityscape.jpg")

image2=cv2.imread ( "C:/Users/rache/OneDrive/Desktop/opencv/images/cat.jpg")

image2=cv2.resize(image2,(image.shape[1],image.shape[0]))

revert=cv2.add(image,image2)

cv2.imshow("image",revert)

cv2.waitKey(0)

cv2.destroyAllWindows()
