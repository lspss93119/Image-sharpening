import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "./HW2_test_image/skeleton_orig.bmp"
img = cv2.imread(path, 0)
x,y = img.shape
#mask
mask =np.ones(img.shape,np.uint8)
n_x,n_y=np.ogrid[:x,:y]
r=30
mask_area = (n_x-int(x/2))**2+(n_y-int(y/2))**2<= r*r
mask[mask_area] = 0
# 傅立葉變換
# 快速傅立葉變換演算法得到頻率分佈
f = np.fft.fft2(img)
# 預設結果中心點位置是在左上角 呼叫fftshift()函式轉移到中間位置
fshift = np.fft.fftshift(f)
fsmimg = mask*fshift


# fft 結果是複數，其絕對值結果是振幅
rimg = np.log(np.abs(fsmimg))


# 傅立葉逆變換
ishift = np.fft.ifftshift(fsmimg)
iimg = np.fft.ifft2(fsmimg)
iimg = np.abs(iimg)

# 
cv2.imwrite('moon_Laplacian.jpg',iimg)
# 展示結果
plt.subplot(131), plt.imshow(img, 'gray'), plt.title('original Fourier')
plt.axis('off')
plt.subplot(132), plt.imshow(rimg, 'gray'), plt.title('fourier Fourier')
plt.axis('off')
plt.subplot(133), plt.imshow(iimg, 'gray'), plt.title('inverse fourier Fourier')
plt.axis('off')
plt.show()