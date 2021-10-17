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
model = keras.models.load_model("./model/trained_model")

def get_landmark_results(img):
    converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(converted)
    return results

def annotate_img(img, results):
    converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    annotated_image = img.copy()
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS)
    return annotated_image

def predict(results):
    return (model.predict(np.array(get_standard_data(results)).reshape(1,66))[0][0] < 0.4)
    