import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while(True):
    # cature frame by frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours,-1, (0,0,255), 3)
    cnt = contours[0]
    cv2.drawContours(frame, [cnt], 0, (0,255,0), 3)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    print(hull)
      
      
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(125,255,0),2)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
   # cv2.drawContours(frame,[box],0,(0,0,255),2)
    cv2.imshow('frame',thresh)
    cv2.imshow('actualthingy',frame)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
