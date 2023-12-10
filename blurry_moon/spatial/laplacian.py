import cv2
import numpy as np

img = cv2.imread("./HW2_test_image/blurry_moon.tif",0)

gray_lap = cv2.Laplacian(img,cv2.CV_16S,ksize = 3)
dst = cv2.convertScaleAbs(gray_lap)
img2 = cv2.hconcat([img,dst])
# 
cv2.imwrite('moon_Laplacian.jpg',dst)
cv2.imshow('original & laplacian', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()