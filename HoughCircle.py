# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 12:16:19 2022

Author: erdem
"""

import cv2
import numpy as np

# Load the image
img = cv2.imread("coins.jpg")


# Convert the images to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Apply median blur to reduce noise
img_blur = cv2.medianBlur(gray, 5)


# Detect circles using the Hough Circle Transform
# Parameters:
# - cv2.HOUGH_GRADIENT: Detection method
# - 1: Resolution of the accumulator
# - img.shape[0] / 4: Minimum distance between detected circles (computed based on image height)
# - param1=200: Gradient value for edge detection
# - param2=10: Threshold for circle center detection
# - minRadius=15: Minimum circle radius
# - maxRadius=80: Maximum circle radius
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, img.shape[0] / 4, param1=200, param2=10, minRadius=15, maxRadius=80)

if circles is not None:  # If circles are detected
    circles = np.uint16(np.around(circles))  # Round the floating-point values and store them in the same variable

    for i in circles[0, :]:  # Iterate through detected circles
        # Extract circle center (i[0], i[1]) and radius (i[2])
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 4)  # Draw the detected circles on the image

# Display the image with detected circles
cv2.imshow("im", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
