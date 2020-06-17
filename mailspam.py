#import all modules
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from termcolor import colored
global stroka
stroka = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*"


print(colored("---Mail spam v 0.1---","red",attrs=['bold']))
print(colored("---Maded by Didenko Aleksandr---","red",attrs=['bold']))
#func that spam messages

def send_mail():
    #requests all variables from the user
    login = str(input(colored("Your email: ","green")))
    password = str(input(colored("Your password: ","green")))
    url = str(input(colored("URL: ","green")))
    whom = str(input(colored("Whom: ","green")))
    message = str(input(colored("Text: ","green")))
    number = int(input(colored("How many messages: ","green")))

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
        print(colored(f"[+] Sended {str(x)} messages","red",attrs=['bold']))

#for comfortable makes new func

def spam():
    send_mail()

#start spam,enjoy :)))

if __name__ == '__main__':
    spam()
