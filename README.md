# Hough-Circle
## Description
This Python script leverages the power of the OpenCV library to perform intricate image processing and circle detection. The process is meticulously orchestrated to deliver accurate results. Here's a step-by-step breakdown of its functionality:


## Image Loading and Preprocessing:
The code begins by loading two images, "coins.jpg" and "balls.jpg." It then converts these color images to grayscale. Grayscale conversion simplifies image processing by reducing it to a single channel, focusing on intensity, which is essential for circle detection.


## Noise Reduction with Median Blur:
To enhance the quality of the images and eliminate noise, a median blur is applied. This process involves replacing each pixel's value with the median value of the pixels in its neighborhood. In this case, a kernel size of 5x5 is used for blurring.


## Hough Circle Transform: 
The heart of this script is the Hough Circle Transform, a powerful technique for detecting circular shapes within an image. It employs a variety of parameters:


cv2.HOUGH_GRADIENT: This indicates the chosen method for circle detection, specifically the Hough Gradient method.
1: This parameter defines the resolution of the accumulator in the Hough space.
img.shape[0] / 4: The minimum distance between the detected circles is dynamically determined based on the image's height, which ensures accuracy.
param1=200: This is the gradient value used for edge detection, a critical component of circle detection.
param2=10: It sets the threshold for circle center detection.
minRadius=15 and maxRadius=80: These values define the permissible range for circle radii.
Circle Drawing: When circles are successfully detected, they are stored as coordinates in the variable 'circles.' If circles are found, the code iterates through these coordinates. For each circle found, it extracts the center and radius, then draws a red circle around it. This provides a visual representation of the detected circles on the image.


## Display: 
The final result is displayed using OpenCV's cv2.imshow function, allowing you to visualize the image with the detected circles.


This code is exceptionally versatile and can be employed in a wide range of computer vision applications, including industrial automation, object tracking, quality control, and much more. It showcases the power of OpenCV in simplifying complex image processing tasks and highlights how precise parameter tuning can yield remarkable results in circle detection.


## Original Photo
![coins](https://github.com/Prometheussx/Hough-Circle/assets/54312783/e5f4de86-0b3b-422c-aa10-69123e50f171)

## Result
![Ekran görüntüsü 2023-10-11 144439](https://github.com/Prometheussx/Hough-Circle/assets/54312783/3b66198b-1a49-498e-83ce-3bad2b58b90e)
