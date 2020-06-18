#import all modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from termcolor import colored
import os
import getpass
global stroka
stroka = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*"

os.system("clear")

print(colored("---Mail spam v 0.1---","red",attrs=['bold']))
print(colored("---Maded by Didenko Aleksandr---","red",attrs=['bold']))
#func that spam messages

def send_mail():
    #requests all variables from the user
    login = str(input(colored("Your email: ","green",attrs=['bold'])))
    password = str(getpass.getpass((colored("Your password: ","green",attrs=['bold']))))
    url = str(input(colored("URL: ","green",attrs=['bold'])))
    whom = str(input(colored("Target email: ","green",attrs=['bold'])))
    message = str(input(colored("Text: ","green",attrs=['bold'])))
    number = int(input(colored("How many messages: ","green",attrs=['bold'])))

    #main cycle

    for x in range(number):
        topic = ""
        #random topic
        for i in range(6):
            topic += random.choice(stroka)

        #structure of the message

        msg = MIMEMultipart()
        msg["Subject"] = topic
        msg["From"] = login
        body = message

        msg.attach(MIMEText(body, "plain") )

        #make smtp ssl server

        server = smtplib.SMTP_SSL(url, 465)
        server.login(login, password)
        server.sendmail(login, whom, msg.as_string() )

        x += 1
        print(colored(f"[+] Sended {str(x)} messages","cyan"))

#for comfortable makes new func

def spam():
    send_mail()

#start spam and some exceptions,enjoy :)))

if __name__ == '__main__':
    try:
        spam()
    except smtplib.SMTPAuthenticationError:
        print(colored("[ERROR] Login or password are incorrect","red",attrs=['bold']))
    except smtplib.SMTPConnectError:
        print(colored("[ERROR] Connection error","red",attrs=['bold']))
    except smtplib.SMTPServerDisconnected:
        print(colored("[ERROR] Connection unexpectedly closed","red",attrs=['bold']))
    
