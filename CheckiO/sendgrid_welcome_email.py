import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = ''  # https://app.sendgrid.com/settings/api_keys?extID=128039&channel=sponsorship&camp=game&pub=checkio&place=game&creative=ei&utm_medium=sponsorship&utm_source=checkio
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
