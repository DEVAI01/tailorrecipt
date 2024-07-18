# emailsending.py

def sendMail(emailid, subject="", html="", attachment_path=None, attachment_name=None):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import os

    # Your email id
    me = "naveenpatidar951@gmail.com"
    you = emailid

    msg = MIMEMultipart()
    msg['From'] = me
    msg['To'] = you
    msg['Subject'] = subject if subject else "Profile Created Successfully"

    # Attach HTML content
    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    # Attach the PDF file
    if attachment_path and attachment_name:
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={attachment_name}',
            )
            msg.attach(part)

    # SMTP server configuration
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("naveenpatidar951@gmail.com", "scit wmxx eukm jzww")  # Replace with your email password or app-specific password

    # Send email
    s.sendmail(me, you, msg.as_string())
    s.quit()
    print("Mail sent successfully....")
