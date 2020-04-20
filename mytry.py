import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#import workingmail

email = 'enter email from'
password = 'enter your pasword'

subject = 'This is the subject'  # The subject line

# function to fetch message from txt file


def fetch_message():
    with open('message.txt', 'r') as message:
        a = str(message.read())
        print("\nmessage composed start\n#########################################################################\n"+a)
        print("\n#########################################################################\nmessage composed ended")
        return a


def main():
    with open('contacts.txt', 'r') as read:
        a = set(read)
        d = list(a)
        print("\n"+str(d))
        b = (len(a))
        n, i = 0, 0
        while i != b:
            send_to_email = d[i]
        # message sending requirements
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject
            # Attach the message to the MIMEMultipart object
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # starts the server
            server.login(email, password)  # login with the sender id
            # You now need to convert the MIMEMultipart object to a string to send
            text = msg.as_string()
            server.sendmail(email, send_to_email, text)
            print("\nSENDING YOUR MAIL TO\n"+d[i])
            n = n+1
            print("\nNO. OF MESSAGES SENT > > > "+str(n))
            i = i+1


# server.quit()
if __name__ == '__main__':
    message = fetch_message()
    main()
print("\n MAILS HAS BEEN SENT ")
wait = input("PRESS ENTER TO exit.")
