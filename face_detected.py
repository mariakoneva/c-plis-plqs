import cv2
import smtplib
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from password import ivan_password

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


sender_email = 'ivan.g.genov.2021@elsys-bg.org'
sender_password = ivan_password
receiver_email = 'gixirobot@gmail.com'


tmp_dir = 'tmp'
if not os.path.exists(tmp_dir):
    os.mkdir(tmp_dir)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 10)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        
       
        msg = MIMEMultipart()
        msg['From'] = "ivan.g.genov.2021@elsys-bg.org"
        msg['To'] = "gixirobot@gmail.com"
        msg['Subject'] = 'Face Detected'
        password = ivan_password

       
        filename = 'face.jpg'
        filepath = os.path.join(tmp_dir, filename)
        cv2.imwrite(filepath, img)

       
        with open(filepath, 'rb') as f:
            img_data = f.read()
            image = MIMEImage(img_data, name=filename)
            msg.attach(image)

        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, receiver_email, msg.as_string())
        

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break


for f in os.listdir(tmp_dir):
    os.remove(os.path.join(tmp_dir, f))
os.rmdir(tmp_dir)

print("FACE DETECTED")
cap.release()
cv2.destroyAllWindows()
