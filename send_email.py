# send_email.py

from email.headerregistry import Address
from email.message import EmailMessage
import os
import smtplib

# Gmail details
email_address = os.getenv('GMAIL_ADDRESS', None)
email_password = os.getenv('GMAIL_APPLICATION_PASSWORD', None)

# Recipent
to_address = 'chiragmaliwal1995@gmail.com'

def create_email_message(from_address, to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)
    return msg


if __name__ == '__main__':
    msg = create_email_message(
        from_address=email_address,
        to_address=to_address,
        subject='Hello World',
        body="Test sending the body.",
    )

    with smtplib.SMTP('smtp.gmail.com', port=587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(email_address, email_password)
        smtp_server.send_message(msg)

    print('Email sent successfully')
