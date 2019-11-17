import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = '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'
SUBJECT = 'Welcome'
BODY = 'Hi {}'
sg = sendgrid.SendGridAPIClient(API_KEY)

def send_email(email, name):
    message = Mail(
        from_email='from_email@example.com',
        to_emails=email,
        subject=SUBJECT,
        plain_text_content=BODY.format(name)
    )
    response = sg.send(message)


send_email('somebody@gmail.com', 'Some Body')
send_email('saxin@ukr.net', 'Sasha')
print('Done')
