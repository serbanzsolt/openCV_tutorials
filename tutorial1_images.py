import cv2

img = cv2.imread('assets\D11T.jpg', cv2.IMREAD_GRAYSCALE)

"""
-1 - Color
0 - Greyscale
1 - Unchanged
"""
# img = cv2.resize(img, (800,500))
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('assets\\new_img.jpg', img)

cv2.imshow('BULLDOZER',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

