#showing image in multiple colurs(r,g,b)
import cv2 as cv
img=cv.imread(r'C:\tmp\0000.png')
B,G,R=cv.split(img)
cv.imshow('image',img). #read image
cv.waitKey(0)
cv.imshow('blue',B)
cv.waitKey(0)
cv.imshow('green',G)
cv.waitKey(0)
cv.imshow('red',R)
cv.waitKey(0)
cv.destroyAllWindows
