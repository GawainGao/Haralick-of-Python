'''
Input the image and change to GLCM.
Use haralick feature to show the result.
'''

import mahotas
import cv2
image = cv2.imread('01.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

print mahotas.features.haralick(gray)


