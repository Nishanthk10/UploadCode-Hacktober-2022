# CREATE A DUPLICATE IMAGE
import cv2
img = cv2.imread('1.jpg')
cv2.imshow('Original image',img)
cv2.imwrite('cat.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
