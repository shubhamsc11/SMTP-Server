# Sending HTMl Message Mail


import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = "Check out new mail"
msg['From'] = 'Sender mail id'
msg['To'] = 'receiver mail id'
msg.set_content('Plain text')

msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:red;">This is HTML MSG AND REPLY ME ONCE YOU GET BYE !!!!!</h1>
        </body>
    </html>
    """, subtype = "html")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("your mail id", "your password")
    smtp.send_message(msg)
    print("send successfully...")

    # smtp.quit()

