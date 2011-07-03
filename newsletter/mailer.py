from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib
import mailcon
# Define these once; use them twice!
strFrom = 'from@example.com'
strTo = 'to@example.com'



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
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Holiday newsletter'
    msgRoot['From'] =  mailcon.mailfrom
    msgRoot['To'] = mailcon.mailto
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText(msg)
    msgAlternative.attach(msgText)
    '''FROM = mailcon.mailfrom
    TO = [mailcon.mailto] # must be a list
    SUBJECT = "Holiday newsletter"
    TEXT = msg
    message = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # Send the mail
    '''
    server.sendmail(mailcon.mailfrom, mailcon.mailto, msgRoot.as_string())
    server.quit()
    server.close()
