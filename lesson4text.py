import cv2

image=cv2.imread ( "C:/Users/rache/OneDrive/Desktop/opencv/images/white_screen.jpg" , 
                  cv2.IMREAD_COLOR)

f=cv2.Formatter_FMT_NUMPY

c=(0,0,240)

font_scale=1

width=4

co=(100,100)

image=cv2.putText(image,"hiiiiiiiii",co,f,font_scale,c,width,cv2.LINE_AA)

cv2.imshow ( "text", image )

cv2.waitKey(0)

cv2.destroyAllWindows()