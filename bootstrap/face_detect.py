__author__ = 'argi'

import cv2
# import sys


class FaceDetect:
    
    def __init__(self, casc_path):
        self.classifier_path = casc_path

    def execute(self):
        face_cascade = cv2.CascadeClassifier(self.classifier_path)

        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            # # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# When everything is done, release the capture
# video_capture.release()
# cv2.destroyAllWindows()
