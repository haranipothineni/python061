import smtplib
from email.message import EmailMessage
sender_email = 'haranipothineni@gmail.com'
receiver_email = 'haranipothineni2005@gmail.com'
app_password = 'txlz wose pvyb sthq'
subject = 'Meeting Reminder'
body = '''Hi Guys
Just reminding you about our meeting tomorrow at 10 AM.
Regards'''
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content(body)
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        print("Email sent successfully!!")
except Exception as e:
    print("Error:", e)
