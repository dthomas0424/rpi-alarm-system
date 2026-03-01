import smtplib
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'youremailaddress', 'your email address password' ) #this is the email address and password that you will be sending the message from
from_mail = 'your email address'
to = '<email address here>' 
body = 'The door has been opened.' #This is where you put the message to be sent
message = ("From: %s\r\n" % from_mail + "To: %s\r\n" % to + "Subject: %s\r\n" % 'Barn Door Status' + "\r\n" + body)
server.sendmail(from_mail, to, message)
