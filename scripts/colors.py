import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_mask(hsv , lower_color , upper_color):
    lower = np.array(lower_color)
    upper = np.array(upper_color)
    
    mask = cv2.inRange(hsv , lower, upper)

    return mask

capture = cv2.VideoCapture(0)

while True: 
    success, frame = capture.read()
    if success == False:
        raise ConnectionError

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = get_mask(hsv, [18, 255, 64], [139, 255, 216])
    
    result = cv2.bitwise_and(frame , frame , mask= mask)
    
    #plotting
    
    kernel = np.ones((30, 30), np.float32)
    
    result = cv2.dilate(result, kernel)
    result = cv2.erode(result, kernel)
    
    

    cv2.imshow('frame', result)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

cv2.waitKey(0)