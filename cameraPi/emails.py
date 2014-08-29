import smtplib
import logging

from cameraPi import logger

# email credentials
username = 'hogtrapalert@gmail.com'
password = 'questh0gtrap'

def send_email( subject='No Subject',
                sender=username,
                recipients=None,
                body=None):
    try:
        server = smtplib.SMTP()
        server.connect("smtp.gmail.com", 'submission')
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.sendmail(sender, recipients, 'Subject: {subject}\n\n{body}'.format(subject=subject, body=body))
        logger.info('Sent Email : {recipients}'.format(recipients=recipients))
    except Exception,R:
            return R    


def send_alert(recipients=None):
    subject = 'Motion Detected'
    sender = username
    body = """
        Greetings,

            This is an email generated by the raspberry pi. Hopefully,
            this will work and I will be able to move on to something
            more interesting than sending out fake emails.
    """
    send_email(subject, sender, recipients, body)
