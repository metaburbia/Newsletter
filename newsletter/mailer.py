'''
Created on 12 Jun 2011

@author: david
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(selfparams):
        '''
        Constructor
        '''
        
        


import smtplib

SERVER = "localhost"
FROM = "david@cloudsoup.com"
TO = ["david.jones@cloudsoup.com"] # must be a list
SUBJECT = "Hello!"
TEXT = "This message was sent with Python's smtplib"
message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()




import smtplib
msg = 'Hello world.'
server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login('cloudsoup@gmail.com','j0neZjabber!!!')
#server.login('cloudsoup@gmail.com','j0neZjabber!!!')
FROM = "admin@cloudsoup.com"
TO = ["david.jones@cloudsoup.com"] # must be a list
SUBJECT = "Hello!"
TEXT = "This message was sent with Python's smtplib."
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
