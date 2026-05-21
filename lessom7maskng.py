import cv2

import numpy as np

print("opencv version:,cv2__version__")

#-------------------------------VIDEO ININTIALATION-------
video_path = r"C:\Users\rache\OneDrive\Desktop\opencv\images\video.mp4"    #<----change this
capture_video = cv2.VideoCapture(video_path)

if not capture_video.isOpened():
    print("error:cannto open this file")
    exit()

#-------------------------------BG CAPTURE------------------------
background = None
print("captuting bg for video.....")
# read the first 60 frame to get a clean bg
for i in range(60):
    ret, frame = capture_video.read()
    if ret:
        background = frame

if background is None:
    print("error failed to capture bg")
    exit()

#flip bg if needed 
background = np.flip(background, axis = 1)
print("bg captured sucsefully!!!")

#--------------------RESET VIDEO TO START-----------------------------------
capture_video.set(cv2.CAP_PROP_POS_FRAMES,0)

#---------------------mainloop--------------------------------------------
while True:
    ret, img = capture_video.read()
    if not ret:
        break
    img = np.flip(img , axis = 1)
    #conver brgto hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
    # # ----------------- red color detection----------------------------------------
    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])
    
    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])
     
    mask1 = cv2.inRange(hsv, lower_red1,upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2,upper_red2)    
     
    mask = mask1 + mask2
    kernel = np.ones((3,3),np.uint8)
     
    #-----------------------------MASK CLEANING-------------------kernel = np.ones((3,3),np.uinits)
    mask = cv2.morphologyEx(mask ,cv2.MORPH_OPEN,kernel, iterations=2)
    mask = cv2.dilate(mask ,kernel , iterations=2)
      
    mask_inv = cv2.bitwise_not(mask)
    #-----------------------APPLY INVISISBILITY-----------------
    res1 = cv2.bitwise_and(background,background,mask=mask)
    res2 = cv2.bitwise_and(img,img, mask=mask_inv)
    
    final_output = cv2.addWeighted(res1,1 , res2, 1 ,0)
    #--------------------------display--------------------
    cv2.imshow("INVISBLE MAN - VIDEO",final_output)
    if cv2.waitKey(25) == 27: #ESC key
       break
#---------------------------cleanup;;;;;;;;;;;;;;;
capture_video.realease()
cv2.destroyAllWindows()