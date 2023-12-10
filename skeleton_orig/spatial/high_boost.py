import cv2
import numpy as np

path = "./HW2_test_image/skeleton_orig.bmp"
imgColor = cv2.imread(path)

kernel = np.array([[-1, -1, -1], [-1, 9.7, -1], [-1, -1, -1]])
imgHighboost = cv2.filter2D(imgColor, -1, kernel)
img2 = cv2.hconcat([imgColor,imgHighboost])
# 
cv2.imwrite('moon_Hight_boost.jpg',imgHighboost)
cv2.imshow('original & Highboost', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()