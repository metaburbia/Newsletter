import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mailcon





def sendmail(filename):
    fh = open(filename, "r")
    msg = fh.read()
    fh.close()
    server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(mailcon.mailuser,mailcon.mailpassword)
    
    # Create the root message and fill in the from, to, and subject headers
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Holiday Newsletter"
    msg['From'] = mailcon.mailfrom
    msg['To'] = mailcon.mailto
    part1 = MIMEText(msg, 'plain')
    part2 = MIMEText(msg, 'html')
    msg.attach(part1)
    msg.attach(part2)
    server.sendmail(mailcon.mailfrom, mailcon.mailto, msg.as_string())
    server.quit()

