#image resizing 
#image resizing refers to scaling of images and helps in redusing the nnumbers of pixels

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image=cv.imread(r'C:\tmp\0000.png'). # file from your pc
half=cv.resize(image,(0,0),fx=0.6 ,fy=1.0)#the values inside() decides the limits of x n y axis   
bigger=cv.resize(image,(1050,1610))#fx defines the length whereas fy defines the breadth  of a any quadilateral
stretch_near=cv.resize(image,(780,540),interpolation=cv.INTER_NEAREST)#interpolation is used to calculate the pixcels values
titles=['original','half','bigger','stretch_near']
images=[image,half,bigger,stretch_near]
count=4
for i in range(count):
    plt.subplot(2,2,i+1)#subplot defines the matrix format of picture representation ie either 2*2 ,2*4 or whatever
    plt.title(titles[i])
    plt.imshow(images[i])
plt.show()
