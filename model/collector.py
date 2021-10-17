import cv2
import mediapipe as mp
import numpy as np
import math
from typing import List
from util import get_standard_data

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=2)

mp_drawing = mp.solutions.drawing_utils 

# Help I'm so sleep deprived -- Nathan

def main():
    capture = cv2.VideoCapture(0)

    while True:
        success, img = capture.read()
        img = cv2.flip(img, 1)
        key = cv2.waitKey(1)
        img = process_frame(img)
        cv2.imshow("Test", img)

        if key == ord('q'):
            cv2.destroyAllWindows()
            break

def process_frame(img: np.ndarray) -> np.ndarray:
    converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(converted)

    print(get_standard_data(results))
    
    annotated_image = img.copy()
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS)
    return annotated_image

if __name__ == "__main__":
    main()