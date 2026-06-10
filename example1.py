import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_color = frame[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            eye = roi_color[ey:ey+eh, ex:ex+ew]

            hsv_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2HSV)
            h, s, v = cv2.split(hsv_eye)

            mean_hue = np.mean(h)

            if 20 < mean_hue < 40:
                color = "Brown"
            elif 40 <= mean_hue < 70:
                color = "Green"
            elif 90 <= mean_hue < 130:
                color = "Blue"
            else:
                color = "Unknown"

            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
            cv2.putText(roi_color, color, (ex, ey-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

    cv2.imshow("Eye Color Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
mean_hue = np.mean(h)

if 20 < mean_hue < 40:
    color = "Brown"
elif 40 <= mean_hue < 70:
    color = "Green"
elif 90 <= mean_hue < 130:
    color = "Blue"
else:
    color = "Unknown"
