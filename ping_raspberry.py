import os
import smtplib
from password import ivan_password

ip_address = "10.1.79.235"
response = os.system("ping -c 1 " + ip_address)
if response == 0:
    print("Ping successful!")
else:
    print("Ping not successful!")
    sender_email = "ivan.g.genov.2021@elsys-bg.org"
    receiver_email = "gixirobot@gmail.com"
    password = ivan_password
    subject = "Malfunction in the system"
    body = "Maybe there is a problem with the robot!!! Please check it asap."
    message = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message)

    server.quit()
