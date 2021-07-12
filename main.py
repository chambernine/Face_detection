import cv2
image = '1.jpg'
face_cascade = "haarcascade_frontalface_default.xml"

face_classifier = cv2.CascadeClassifier(face_cascade)

cover_img = cv2.imread(image)

gray = cv2.cvtColor(cover_img,cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(gray)

x,y,w,h = faces[0]
rect = cv2.rectangle(cover_img,(x,y),(x+w,y+h),(0,255,0),4)


cv2.imshow('Result',cover_img)
cv2.waitKey(0)
