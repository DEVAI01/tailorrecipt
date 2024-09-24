from tailorrecipt.models import EmailStatus  # Import your model
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from django.utils import timezone

def sendMail(emailid, subject="", html="", attachment_path=None, attachment_name=None):
    # Create an entry in the EmailStatus model
    email_status = EmailStatus.objects.create(
        recipient=emailid,
        subject=subject,
        body=html,
        attachment_path=attachment_path if attachment_path else '',
        attachment_name=attachment_name if attachment_name else '',
        status='Pending'
    )

    try:
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
        s.login("naveenpatidar951@gmail.com", "scit wmxx eukm jzww")  # Use your app-specific password

        # Send email
        s.sendmail(me, you, msg.as_string())
        s.quit()

        # Update status to 'Sent'
        email_status.status = 'Sent'
        email_status.sent_at = timezone.now()
        email_status.save()

        print("Mail sent successfully....")
    except Exception as e:
        # Log failure
        email_status.sent_at = timezone.now()
        email_status.status = f'Failed: {str(e)}'
        email_status.save()
        print(f"Mail failed to send: {str(e)}")

