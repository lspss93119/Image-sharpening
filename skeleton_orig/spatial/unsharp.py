import cv2

image = cv2.imread("./HW2_test_image/skeleton_orig.bmp")
gaussian_3 = cv2.GaussianBlur(image, (0, 0), 2.0)
unsharp_image = cv2.addWeighted(image, 2.0, gaussian_3, -1.0, 0)
#cv2.imwrite("example_unsharp.jpg", unsharp_image)
img2 = cv2.hconcat([image,unsharp_image])
# 
cv2.imwrite('moon_Unsharp.jpg',unsharp_image)
cv2.imshow('original & unsharp', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()