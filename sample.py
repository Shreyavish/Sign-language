import cv2
print(cv2.__version__)

img = cv2.imread('images/basketball1.png',0)

print(img)

cv2.imshow('image',img)
cv2.waitKey(5000) #show image for 5000millisec
cv2.destroyAllWindows()

cv2.imwrite("basketball2.png",img)