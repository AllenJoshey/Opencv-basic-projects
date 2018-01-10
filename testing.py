import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('hand.JPG',0)
ret,thresh = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(thresh, contours, -1, (255,0,0), 3)
cv2.drawContours(img, contours, -1, (255,255,0), 3)
cnt=contours[0]
hull = cv2.convexHull(cnt)
cv2.imshow('bob',img)
cv2.imshow('bobby',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


