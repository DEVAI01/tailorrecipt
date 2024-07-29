# def sendMail(emailid,pwd,subject="",html=""):
# 	import smtplib
# 	from email.mime.multipart import MIMEMultipart
# 	from email.mime.text import MIMEText
# 	     #my email id
# 	me = "naveenpatidar951@gmail.com"
# 	you = emailid

# 	msg = MIMEMultipart('alternative')
# 	msg['From'] = me
# 	msg['To'] = you

# 	if subject=="registration confirmation":
# 		msg['Subject'] = "Profile Created Successfully"
# 	else:
# 		msg['Subject'] = subject

# 	if html=="":
# 		html = """<html>
#   					<head></head>
#   					<body>
#     					<h1>Welcome to Artfullstitches</h1>
#     					<p>You have successfully registered , please click on the link below to verify your account</p>
#     					<h2>Username : """+emailid+"""</h2>
#     					<h2>Password : """+str(pwd)+"""</h2>
#     					<br>
#   					</body>   
# 				</html>
# 			"""
# 	else:
# 		html = html
	
# 	s = smtplib.SMTP('smtp.gmail.com', 587) 
# 	s.starttls() 
# 	s.login("naveenpatidar951@gmail.com","scit wmxx eukm jzww") 
	
# 	part2 = MIMEText(html, 'html')

# 	msg.attach(part2)
	
# 	s.sendmail(me,you, str(msg)) 
# 	s.quit() 
# 	print("mail send successfully....")


def sendMail(emailid, pwd, subject="", html=""):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Sender and receiver email
    me = "naveenpatidar951@gmail.com"
    you = emailid

    # Create the email message
    msg = MIMEMultipart('alternative')
    msg['From'] = me
    msg['To'] = you

    # Set the subject
    if subject == "registration confirmation":
        msg['Subject'] = "Profile Created Successfully"
    else:
        msg['Subject'] = subject

    # Default HTML content
    if html == "":
        html = f"""<html>
                    <head>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                background-color: #f4f4f4;
                                margin: 0;
                                padding: 20px;
                            }}
                            .container {{
                                background-color: #ffffff;
                                border-radius: 8px;
                                padding: 20px;
                                max-width: 600px;
                                margin: auto;
                                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                            }}
                            h1 {{
                                color: #333;
                            }}
                            p {{
                                color: #555;
                            }}
                            .footer {{
                                font-size: 12px;
                                color: #888;
                                text-align: center;
                                margin-top: 20px;
                                border-top: 1px solid #ddd;
                                padding-top: 10px;
                                width: 100%;
                                box-sizing: border-box;
                            }}
                            a {{
                                color: #1a0dab;
                                text-decoration: none;
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <h1>Welcome to Artfullstitches!</h1>
                            <p>Thank you for registering on our site, <strong>murlitailor.shop</strong>. Please do not share your credentials with other:</p>
                            <h2>Username: {emailid}</h2>
                            <h2>Password: {pwd}</h2>
                            <br>
                            <p>If you have any questions, feel free to contact us at support@murlitailor.shop.</p>
                        </div>
                        <div class="footer">
                                <p>&copy; 2024 murlitailor, Inc. All rights reserved.<br>
                                   Khardon Kalan, Distt- Shajapur, M.P. India 465339<br>
                                   If you no longer wish to receive emails from murlitailor, please <a href="https://murlitailor.shop/contact/">click here</a>.</p>
                        </div>
                    </body>
                </html>"""
    # Create the MIMEText object with HTML content
    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    # Send the email
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("naveenpatidar951@gmail.com", "scit wmxx eukm jzww")
    s.sendmail(me, you, msg.as_string())
    s.quit()
    
    print("Mail sent successfully....")
