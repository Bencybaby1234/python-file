# programe to send mail
import smtplib
import os

# getting password and mail from which we want to send mails
# throug environment variable
EMAIL_ADD = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

# function for sending mail


def sendmail(to):
    with smtplib.SMTP('smtp.gmail.com', 587) as ser:
        ser.starttls()
        ser.login(EMAIL_ADD, EMAIL_PASS)
        ser.sendmail(EMAIL_ADD, to, "your data submited succesfully")
        ser.close()
