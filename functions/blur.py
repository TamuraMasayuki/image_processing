import cv2
import numpy as np

img = cv2.imread("20200517.jpeg")


kernel15 = np.ones((15,15),np.float32)/225
dst15 = cv2.filter2D(img,-1,kernel15)

cv2.imwrite("blur15.jpg", dst15)

kernel20 = np.ones((20,20),np.float32)/400
dst20 = cv2.filter2D(img,-1,kernel20)

cv2.imwrite("blur20.jpg", dst20)
