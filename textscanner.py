import cv2
import numpy as np


vid = cv2.VideoCapture(0)
detector = cv2.TextDETECTOR()
while True:
    ret, frame = vid.read()
    boxes, confidences = detector.detect(frame)
    for i, box in enumerate(boxes):
        cv2.rectangle(frame, box[0], box[1], (0, 255, 0), 2)
    cv2.imshow("Text Detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break

