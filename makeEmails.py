import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send(contacts, title : str, content : str):
    #email information
    senderName = "Elevated Temples"
    emailSender = "elevatedtemples@gmail.com"

    emailReceiver = ""
    if isinstance(contacts, str):
        emailReceiver = contacts
    elif isinstance(contacts, list):
        emailReceiver = ", ".join(contacts)
    else:
        print("error of contacts type")
        exit(0)

    emailPassword = "rvdt amng jbem ogsc"

    subject = title
    html = content
    htmlText = MIMEText(html, "html")


    #compose email content
    message = MIMEMultipart("alternative")
    message["From"] = f"{senderName} <{emailSender}>"
    message["To"] = emailReceiver
    message["Subject"] = subject
    message.attach(htmlText)


    #send email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
        server.login(emailSender, emailPassword)
        server.sendmail(emailSender, emailReceiver, message.as_string())
        server.quit()
