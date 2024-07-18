def sendMail(emailid,pwd,subject="",html=""):
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	     #my email id
	me = "naveenpatidar951@gmail.com"
	you = emailid

	msg = MIMEMultipart('alternative')
	msg['From'] = me
	msg['To'] = you

	if subject=="registration confirmation":
		msg['Subject'] = "Profile Created Successfully"
	else:
		msg['Subject'] = subject

	if html=="":
		html = """<html>
  					<head></head>
  					<body>
    					<h1>Welcome to Artfullstitches</h1>
    					<p>You have successfully registered , please click on the link below to verify your account</p>
    					<h2>Username : """+emailid+"""</h2>
    					<h2>Password : """+str(pwd)+"""</h2>
    					<br>
  					</body>   
				</html>
			"""
	else:
		html = html
	
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("naveenpatidar951@gmail.com","scit wmxx eukm jzww") 
	
	part2 = MIMEText(html, 'html')

	msg.attach(part2)
	
	s.sendmail(me,you, str(msg)) 
	s.quit() 
	print("mail send successfully....")
