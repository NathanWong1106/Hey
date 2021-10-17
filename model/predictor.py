import cv2
import mediapipe as mp
import numpy as np
import math
from typing import List
from util import get_standard_data
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from typing import Tuple, List

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=2)

mp_drawing = mp.solutions.drawing_utils 

def main():
    model = keras.models.load_model("./model/trained_model")
    capture = cv2.VideoCapture(0)

    while True:
        success, img = capture.read()
        img = cv2.flip(img, 1)
        key = cv2.waitKey(1)

        img, res = process_frame(img)
        
        if res.pose_landmarks != None:
            print(model.predict(np.array(get_standard_data(res)).reshape(1,66)))

        cv2.imshow("Test", img)

        if key == ord('q'):
            cv2.destroyAllWindows()
            break

def process_frame(img: np.ndarray):
    converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(converted)

    annotated_image = img.copy()
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS)
    return (annotated_image, results)

if __name__ == "__main__":
    main()
    