

import cv2 as cv
import os



# check_in = 'img/check_in_gray'
# img_name = os.listdir('img/check_in_gray')
# print(img_name)

# for _,val in enumerate(img_name):
#     img = cv.imread(check_in + '/' + val)
#     dst = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#     dst = cv.bitwise_not(dst)
#     cv.imwrite('img/check_in_gray_reverse/{}'.format(val),dst)


# 图片二值化
from PIL import Image
img = Image.open('test.jpg')
 
# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
Img = img.convert('L')
Img.save("test1.jpg")
 
# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
threshold = 200
 
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
 
# 图片二值化
photo = Img.point(table, '1')
photo.save("test2.jpg")
