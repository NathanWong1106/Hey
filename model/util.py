import cv2
import mediapipe as mp
import math
from typing import List

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=2)

def get_standard_data(results) -> list:
    return get_normalized_list(
        get_smallest_xy(results.pose_landmarks.landmark),
        get_largest_xy(results.pose_landmarks.landmark), 
        results.pose_landmarks.landmark)

def get_largest_xy(landmarks) -> tuple:
    x = 0
    y = 0

    for landmark_type in mp_pose.PoseLandmark:
        if landmarks[landmark_type].x > x:
            x = landmarks[landmark_type].x
        if landmarks[landmark_type].y > y:
            y = landmarks[landmark_type].y

    return (x, y)

def get_smallest_xy(landmarks) -> tuple:
    x = math.inf
    y = math.inf
    
    for landmark_type in mp_pose.PoseLandmark:
        if landmarks[landmark_type].x < x:
            x = landmarks[landmark_type].x
        if landmarks[landmark_type].y < y:
            y = landmarks[landmark_type].y

    return (x, y)

def get_normalized_list(mins: tuple, maxes: tuple, landmarks) -> List:
    landmarks_list = []
    for landmark_type in mp_pose.PoseLandmark:
        landmark = landmarks[landmark_type]
        landmarks_list.append((landmark.x - mins[0]) / maxes[0])
        landmarks_list.append((landmark.y - mins[1]) / maxes[1])

    return landmarks_list