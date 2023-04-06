import cv2

# read the image
img = cv2.imread('input_image.png')

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply thresholding to keep only the pixels within the range of the red line
thresh_min = 200
thresh_max = 255
thresh = cv2.inRange(gray, thresh_min, thresh_max)

# apply morphological opening to remove small noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# apply edge detection to extract the boundary of the region of interest
edges = cv2.Canny(opening, 30, 100)

# create a binary mask from the boundary
mask = cv2.bitwise_not(edges)

# apply the mask to the original image to keep only the desired region
result = cv2.bitwise_and(img, img, mask=mask)

# display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
