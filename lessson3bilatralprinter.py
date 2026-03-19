import cv2

image=cv2.imread ( "C:/Users/rache/OneDrive/Desktop/opencv/images/cityscape.jpg")

bil=cv2.bilateralFilter(image,5,70,70)

cv2.imshow("bilateral",bil)

cv2.imshow("normal image",image)


cv2.waitKey(0)

cv2.destroyAllWindows()