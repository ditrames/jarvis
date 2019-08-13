

import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import speech_recognition as sr
import serial
import time
import imaplib, email
import webbrowser
import pyttsx3

def jarvis(x, y, z, print1, complile_code, **kwargs):
        car = True
        vcd = ""
        while car:
            if list(z)[len(list(z))-1] != " ":  z += " "
            if complile_code:   vcd += str(list(z)) + z+ "\n\n"
            z = z.lower().replace("=\r\n", " ").replace("\r\n", " ").replace("=e2=80=99", "'")
            if print1:  print("list input", list(z))
            if complile_code:   vcd += "list input"+str(list(z))+"\n\n"
            if print1:  print("loop inpput var z ",z)
            if complile_code:   vcd += "loop inpput var z " + z+ "\n\n"
            text = z.split("jarvis ", 1)
            if print1:  print("loop split jarvis list var text", text)
            if complile_code:   vcd += "loop split jarvis list var text" + str(text) + "\n\n"
            print(z)
            if len(text) == 2:
                z = text[1]
                if text[len(text)-1] == " " or text[len(text)-1] == "":
                    return 0
                snob = text[1]
                if print1:  print("command and text after jarvis var snob ",snob)
                if complile_code:   vcd += "command and text after jarvis var snob " + snob + "\n\n"
                braker = False
                if print1:  print("diffrent commads linked to functions var x",x)
                if complile_code:   vcd += "diffrent commads linked to functions var x" + str(x) + "\n\n"
                command = 0
                for i in x:
                    command += 1
                    if print1:  print("diffrent ways the command could be said var i ", i)
                    if complile_code:   vcd += "diffrent ways the command could be said var i "+ str(i) + "\n\n"
                    for q in i:
                        if print1:  print("the commands as string var q ", q)
                        if complile_code:   vcd += "the commands as string var q " + str(q) + "\n\n"
                        if q+" " in snob:
                            braker = True
                            bcd = snob.split(q, 1)[1].split("jarvis ", 1)[0]
                            if print1:  print("text ofter extraction var snob after split",bcd, "\n\n")
                            if complile_code:   vcd += "text ofter extraction var snob after split" + str(bcd) + "\n\n"
                            if print1:  print("extracted text",bcd)
                            if complile_code:   vcd += "extracted text" + str(bcd) + "\n\n"
                            print(command)
                            y[command-1](bcd, kwargs)
                            z = snob.split(q, 1)[1]
                        if braker:
                            break
                    if braker:
                        break
            else:
                car = False
        return vcd

def send_mail(fromaddr, toaddr, body):
        print("sending bounce back email")
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "automated bounce back"
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        b = True
        while b:
            try:
                server.login("jarvisbackchat@gmail.com", "Pickles123505992299505321123505992")
                text = msg.as_string()
                server.sendmail(fromaddr, toaddr, text)
                b = False
            except:
                pass
        print("mail sent")

class main:
    # jarvis
    def jarvis_strip(x, y, z, print1, complile_code):
        jarvis(x, y, z, print1, complile_code)


    def read_mail(commands, functions):
        do = True
        
        try:
            m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
            m.login("jarvisbackchat@gmail.com","Pickles123505992299505321123505992")
            m.select("inbox")
        except Exception as e:
            print("ive gone wrong ", e)
            return None
            do=False
        if do:
            result, bent = m.uid('search', None, "ALL") # search all email and return uids
            prev = 0
            with open("backchatmail.txt", "r") as opener:
                for i in opener:
                    prev = int(i)
            if result == 'OK':
                for num in bent[0].split()[prev-1:]:
                    print(int(num))
                    if int(num) > prev:
                        
                        result, data = m.uid('fetch', num, '(RFC822)')
                        if result == 'OK':
                            email_message = email.message_from_bytes(data[0][1])    # raw email text including headers
                            print('From:' + email_message['From'])
                            try:
                                print('subject:' + email_message['Subject'])
                            except:
                                pass
                            try:
                                try:
                                    do = email_message.get_payload()[ 0 ].get_payload()
                                    print(do)
                                except:
                                    do = email_message.get_payload()
                                    print(do)
                                    print(email_message['From'].split("<", 1)[1].split(">"))
                            except:
                                pass
                            
                            try:
                                jarvis(commands, functions, do, True, True)
                            except Exception as e:
                                print(str(e))
                                print(email_message['From'])
                                try:
                                    send_mail("jarvisbackchat@gmail.com", email_message['From'].split("<", 1)[1].split(">")[0], jarvis(commands, functions, do, True, True))
                                except:
                                    try:
                                        send_mail("jarvisbackchat@gmail.com", email_message['From'], jarvis(commands, functions, do, True, True))#
                                    except:
                                        jarvis(commands, functions, do, True, True)
                                        try:          
                                            send_mail("jarvisbackchat@gmail.com", email_message['From'].split("<", 1)[1].split(">")[0], "and error has ecord")
                                        except:
                                            try:
                                                send_mail("jarvisbackchat@gmail.com", email_message['From'], "error error err... *silent explotion sound* max:'wtf'*max screeming in the distance*")
                                            except:
                                                pass
                 
                      
            m.close()   
            m.logout()
            with open("backchatmail.txt", "w") as opener:
                zd = bent[0].split()
                opener.write(str(len(bent[0].split())+1))   

    # def connect_to_usb(*usb):
            
    #     return ser

    def speach_get(time_len):
        data = ""
        r = sr.Recognizer()
        r.dynamic_energy_threshold = True
        print(sr.Microphone.list_microphone_names())
        print("Speak:")
        
        try:
            with sr.Microphone(sample_rate = 20000, chunk_size = 2048) as d:
                audio = r.listen(d, phrase_time_limit=time_len)
            print("done")
        except Exception as e:
            print(e)
            print("sorry")
            
        try:
            data = r.recognize_google(audio)
            print("You said " + data)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        return data
