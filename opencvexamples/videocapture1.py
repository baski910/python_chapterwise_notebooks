import numpy as np  
import cv2  
  
cap = cv2.VideoCapture('SampleVideo.mp4')  
  
while(cap.isOpened()):  
    ret, frame = cap.read()  
#it will open the camera in the grayscale mode  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    
    cv2.imshow('frame',gray)  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
cap.release()  
cv2.destroyAllWindows()  