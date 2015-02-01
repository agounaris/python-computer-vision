__author__ = 'argi'

import cv2
import numpy as np


class RectangleDetect:
    
    def black_rectangle(self):
        cam = cv2.VideoCapture(0)
        n = 0

        while True:
            return_val, frame = cam.read()

            img = cv2.GaussianBlur(frame, (5, 5), 0)
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            blue_lower = np.array([0, 0, 0], np.uint8)
            blue_upper = np.array([0, 0, 255], np.uint8)
            blue = cv2.inRange(img, blue_lower, blue_upper)

            contours, hierarchy = cv2.findContours(blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            max_area = 0
            
            largest_contour = None
            
            for idx, contour in enumerate(contours):

                area = cv2.contourArea(contour)

                if area > max_area:
                    max_area = area
                    largest_contour = contour
                    if not (largest_contour is None):
                        moment = cv2.moments(largest_contour)
                        if moment["m00"] > 1000:
                            rect = cv2.minAreaRect(largest_contour)
                            rect = ((rect[0][0], rect[0][1]), (rect[1][0], rect[1][1]), rect[2])
                            box = cv2.cv.BoxPoints(rect)
                            box = np.int0(box)
                            cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

            cv2.imshow('img', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
