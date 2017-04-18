import cv2
import numpy as np
from matplotlib import pyplot as plt


face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv3/3.2.0/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

def img_sobel(obj):
    #image = cv2.imread(obj)
    gray = cv2.cvtColor(obj, cv2.COLOR_BGR2GRAY)

    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    # blurred = cv2.blur(gradient, (9, 9))
    # (_, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.2,
                                          minNeighbors=5)


    for (x, y, w, h) in faces:
        cv2.rectangle(obj, (x, y), (x + w, y + h), (255, 155, 100), 2)



    return obj

def detectNum(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.blur(gray, (3, 3), 0)
    (_, thresh) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
    edged = cv2.Canny(thresh, 20, 100)

    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in cnts], key = lambda x: x[1])

    # loop over the contours
    for (c, _) in cnts:
    	# compute the bounding box for the rectangle
        (x, y, w, h) = cv2.boundingRect(c)
        if (h > 25):
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 155, 100), 2)

    return img
