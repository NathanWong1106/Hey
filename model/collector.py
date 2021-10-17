import cv2
import mediapipe as mp
import numpy as np
import math
from typing import List
from util import get_standard_data
import csv

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=2)

mp_drawing = mp.solutions.drawing_utils 

# Help I'm so sleep deprived -- Nathan

def main():
    # State of the data collection script
    label = "raised"
    is_recording = False

    capture = cv2.VideoCapture(0)
    file = open("./model/data/data.csv", "w", newline="")

    while True:
        success, img = capture.read()
        img = cv2.flip(img, 1)
        key = cv2.waitKey(1)
        img, res = process_frame(img, label, is_recording, file)

        cv2.imshow("Test", img)

        if key == ord('q'):
            cv2.destroyAllWindows()
            break

        if key == ord(' '):
            is_recording = not is_recording
        elif key == ord('s'):
            label = "unraised" if label == "raised" else "raised"
    
    file.close()


def process_frame(img: np.ndarray, label: str, is_recording: bool, file):
    converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(converted)

    if is_recording and results.pose_landmarks != None:
        try:
            data = get_standard_data(results)
            data.append(label)

            writer = csv.writer(file)
            writer.writerow(data)
        except:
            pass
        
    annotated_image = img.copy()
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS)
    cv2.putText(annotated_image, label, (0,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
    cv2.putText(annotated_image, "recording" if is_recording else "paused", (100,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0))
    return (annotated_image, results)


if __name__ == "__main__":
    # output = ["Foo", "Bar"]

    # f = open("data.csv", "w")
    # w = csv.writer(f)
    # w.writerow(output)
    # f.close()
    # # writer = csv.writer(open("data.csv", "w"))
    # # writer.writerow(["hi"])

    # # reader = csv.reader(open("data.csv", "r"))
    # # for l in reader:
    # #     print(l)
    main()