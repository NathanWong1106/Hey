import socketio
import cv2
from detection import get_landmark_results, annotate_img, predict
import time

EMIT_FREQUENCY = 1 #how long (in seconds) before a ping is sent to server

def main():
    sio = socketio.Client()
    sio.connect("http://localhost:3000")

    capture = cv2.VideoCapture(0)

    last_emit = time.time()

    while True:
        success, img = capture.read()
        img = cv2.flip(img, 1)
        key = cv2.waitKey(1)

        if key == ord('q'):
            cv2.destroyAllWindows()
            break

        results = get_landmark_results(img)
        if results.pose_landmarks != None:
            img = annotate_img(img, results)
            is_raised = predict(results)
        else:
            is_raised = False

        cv2.imshow("Camera", img)

        if time.time() - last_emit > EMIT_FREQUENCY:
            print(is_raised)
            sio.emit("cam_update", {"id": 1, "state": 1 if is_raised else 0})
            last_emit = time.time()

if __name__ == "__main__":
    main()