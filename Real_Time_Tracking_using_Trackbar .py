#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np


#  ### Creating Trackbar - Trackbar would help us in finding out the exact lower and higher hsv values. Later, we can use it in finding the contours.

# In[5]:


def passing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')

cv2.createTrackbar('L - H', 'frame', 0, 179, passing)
cv2.createTrackbar('L - S', 'frame', 0, 255, passing)
cv2.createTrackbar('L - V', 'frame', 0, 255, passing)
cv2.createTrackbar('U - H', 'frame', 179, 179, passing)
cv2.createTrackbar('U - S', 'frame', 255, 255, passing)
cv2.createTrackbar('U - V', 'frame', 255, 255, passing)


# In[6]:


while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos('L - H', 'frame')
    l_s = cv2.getTrackbarPos('L - S', 'frame')
    l_v = cv2.getTrackbarPos('L - V', 'frame')
    u_h = cv2.getTrackbarPos('U - H', 'frame')
    u_s = cv2.getTrackbarPos('U - S', 'frame')
    u_v = cv2.getTrackbarPos('U - V', 'frame')
    
    
    lower_green = np.array([l_h,l_s,l_v])
    upper_green = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv,lower_green,upper_green)
    
    cv2.imshow('mask',mask)
    key = cv2.waitKey(1)
    if key ==27:
        break
        
cap.release()
cv2.destroyAllWindows()


# In[ ]:




