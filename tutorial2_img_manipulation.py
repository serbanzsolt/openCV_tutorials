import cv2
import random

img = cv2.imread('assets/D11T.jpg', -1)

print(img)
print(type(img))
print(img.shape)
# 926 Height, 1707 Width, 3 Channel RGB BGR

#Printing the First row of the image
print("\nFirst row:\n")
print(img[0])

#First row middle pxs
print("\nFirst row in the middle:\n")
print(img[0][45:400]) #pxs between 45 and 400

print("\nValue of 1px:\n")
print(img[257][400]) 

# Change the first 100 line of the image

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        # (rows, columns, channels)

cv2.imshow("Bulldozer", img)        
cv2.waitKey(0)
cv2.destroyAllWindows()