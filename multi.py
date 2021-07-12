import cv2
face_cascade = "haarcascade_frontalface_default.xml"
face_classifier = cv2.CascadeClassifier(face_cascade)

img = cv2.imread('2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_classifier.detectMultiScale(gray)
for faces in faces:
    x,y,w,h = faces
    rect = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    print(faces)
cv2.imshow('Result',img)
cv2.waitKey(0)

