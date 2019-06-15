import cv2

img = cv2.imread('rose.jpeg')

cv2.imshow('rose.jpeg',img)

cv2.waitKey(0)
cv2.destryAllWindows()