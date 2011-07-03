import smtplib
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
    FROM = mailcon.mailfrom
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
    server.sendmail(FROM, TO, message)
    server.quit()
    server.close()
