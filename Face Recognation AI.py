import cv2
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
videoCapture = cv2.VideoCapture(0)
while True:
    _,img = videoCapture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = trained_face_data.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

videoCapture.release()