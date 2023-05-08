#---------------------------------------------------IMPORTING LIBRARIES-------------------------------------------------------------------------------
import cv2
import numpy as np


#---------------------------------------------------------------------------------------------------------------------------------
cap=cv2.VideoCapture("./Videos/video.mp4");
count_line_position=500;

#Intialize Subtractor
algo=cv2.bgsegm.createBackgroundSubtractorMOG()

while(True):
    ret,frame1=cap.read()
    grey=cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(grey,(3,3),5)
    #applying on each frame
    img_sub=algo.apply(blur)
    dilat=cv2.dilate(img_sub,np.ones((5,5)))
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dilatada=cv2.morphologyEx(dilat,cv2.MORPH_CLOSE,kernel)
    dilatada=cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE,kernel)
    counterShape=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(255,127,0),3)
    cv2.imshow("DECTECTOR",frame1)

    if cv2.waitKey(1)==13:
        break

cv2.destroyAllWindows()
cap.release()