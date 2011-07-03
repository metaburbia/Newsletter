def createhtmlmail (html, text, subject):
    """Create a mime-message that will render HTML in popular
    MUAs, text in better ones"""
    import MimeWriter
    import mimetools
    import cStringIO
    from email.MIMEImage import MIMEImage


    
    out = cStringIO.StringIO() # output buffer for our message 
    htmlin = cStringIO.StringIO(html)
    txtin = cStringIO.StringIO(text)
    
    writer = MimeWriter.MimeWriter(out)
    #
    # set up some basic headers... we put subject here
    # because smtplib.sendmail expects it to be in the
    # message body
    #
    writer.addheader("Subject", subject)
    writer.addheader("MIME-Version", "1.0")
    #
    # start the multipart section of the message
    # multipart/alternative seems to work better
    # on some MUAs than multipart/mixed
    #
    writer.startmultipartbody("alternative")
    writer.flushheaders()
    #
    # the plain text section
    #
    subpart = writer.nextpart()
    subpart.addheader("Content-Transfer-Encoding", "quoted-printable")
    pout = subpart.startbody("text/plain", [("charset", 'us-ascii')])
    mimetools.encode(txtin, pout, 'quoted-printable')
    txtin.close()
    #
    # start the html subpart of the message
    #
    subpart = writer.nextpart()
    subpart.addheader("Content-Transfer-Encoding", "quoted-printable")
    #
    #    get the countdown image
    #
    fp = open('../countdown.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')
    subpart.attach(msgImage)
    #
    # returns us a file-ish object we can write to
    #
    pout = subpart.startbody("text/html", [("charset", 'us-ascii')])
    mimetools.encode(htmlin, pout, 'quoted-printable')
    htmlin.close()
    #
    # Now that we're done, close our writer and
    # return the message body
    #
    writer.lastpart()
    msg = out.getvalue()
    out.close()
    print msg
    return msg

if __name__=="__main__":
    import smtplib
    import mailcon
    f = open("mailfile.txt", 'r')
    html = f.read()
    f.close()
    #f = open("newsletter.txt", 'r')
    #text = f.read()
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