import cv2

face_cascade = "haarcascade_frontalface_default.xml"
face_classifier = cv2.CascadeClassifier(face_cascade)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)
    for faces in faces:
        x, y, w, h = faces
        rect = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
        print(faces)
    cv2.imshow('Result', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
