from datetime import datetime
import time
import flytime

def daysToGo():
    flyTime = datetime(*(time.strptime(flytime.FlightTime, "%Y-%m-%d")[0:6]))
    #flyTime = datetime.strptime(flytime.FlightTime,'%Y-%m-%d')
    currentDateTime = datetime.now() 
    return (flyTime - currentDateTime).days 


def createhtmlmail (html, text, subject):
    """Create a mime-message that will render HTML in popular
    MUAs, text in better ones"""
    
    # email clients that don't want to display the HTML.
    
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.MIMEImage import MIMEImage
    
    # Define these once; use them twice!
    strFrom = mailcon.mailfrom
    strTo = mailcon.mailto
    
    # Create the root message and fill in the from, to, and subject headers
    

    strTime =  time.strftime("%A, %d %B %Y")
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'US Holiday Newsletter ' + strTime
    msgRoot['From'] = strFrom
    msgRoot['To'] = (','.join(strTo))
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    
    
    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    
    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)
    
    # We reference the image in the IMG SRC attribute by the ID we give it below
    #msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
    msgText = MIMEText(html, 'html')
    msgAlternative.attach(msgText)
    
    # This example assumes the image is in the current directory
    fp = open('countdown.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)


    return msgRoot.as_string()

if __name__=="__main__":
    import smtplib
    import mailcon
    f = open("mailfile.txt", 'r')
    html = f.read()
    f.close()

    text = 'Read the email in hTML'
    subject = "Today's Newsletter!"
    message = createhtmlmail(html, text, subject)
    server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(mailcon.mailuser,mailcon.mailpassword)
    server.sendmail(mailcon.mailfrom, mailcon.mailto, message)
    server.quit()