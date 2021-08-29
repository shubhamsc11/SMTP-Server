import smtplib
ob = smtplib.SMTP("smtp.gmail.com", 587)

ob.starttls()

ob.login("your mail id", "your password")
subject = "Sending Email using python"
body = "This is testing of sending email using python"

message = "Subject:{}\n\n{}".format(subject, body)
# print(message)
ob.sendmail(msg=message, to_addrs="receiver mail id", from_addr="sender mail id")
print("send successfully...")
ob.quit()

