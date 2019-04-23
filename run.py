import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')


def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, 1.3, 5)  # faces detected by cascade
    if faces is not ():
        if len(faces) == 1:
            return faces[0]

        # return the biggest face if multiple faces are found
        faces = faces[faces[:, 2].argsort()]
        faces = faces[faces[:, 3].argsort()]
        # (x, y, w, h)이므로 각각 h(3), w(2) 우선순으로 정렬

        # print(faces)
        return faces[-1]
    # return None if no faces are found
    return None


def detect_eyes(frame):
    img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(
            roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

prev_face = None
while True:
    ret, frame = cap.read()
    face = detect_face(frame)
    if face is None:  # use the previous detected face if no faces are found
        if prev_face is not None:
            face = prev_face
    if face is not None:
        (x, y, w, h) = face
        prev_face = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        eyes = detect_eyes(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
