

import cv2 as cv
import os
import os
import sys
path = os.path.abspath(os.path.dirname(sys.argv[0]))

img_path = os.listdir(path + '/JPEGImages')
print(img_path)


# file_path = "D:/test/test.py"
# (filepath, tempfilename) = os.path.split(file_path)
# (filename, extension) = os.path.splitext(tempfilename)
# print("tempfilename=",tempfilename)
# print("filename=",filename) 
# if extension == 'py':
#     new_name = filename + '.html'
#     print(ne)
#     os.rename(tempfilename,new_name)
# print(file_path)
for i in range(len(img_path)):

    delete_img = path + '\\JPEGImages\\' + img_path[i]
    image = cv.imread(path + '\\JPEGImages\\' + img_path[i])

    (filepath, tempfilename) = os.path.split(img_path[i])
    (filename, extension) = os.path.splitext(tempfilename)
    #print("tempfilename=",tempfilename)
    #print("filename=",filename)    

    cv.imwrite(path+"/JPEGImages/{}.jpg".format(filename),image)
    os.remove(delete_img)
