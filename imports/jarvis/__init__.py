

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
import threading

def delay_function(command):
    print("start")
    try:
        command, delay_time = command.lower().split()[-2:]
    except:
        return
    try:
        delay_time = int(delay_time)
    except:
        return 0
    if command == "delay":
        time.sleep(delay_time)
    print("done")
class main:

    def __init__(self):
        pass

    def search_algorithm(self, commands, functions, command_string, command_start, delay_function=delay_function):
        print(command_string)
        command_position = []
        for command in range(len(commands)):
            for command_str in range(len(commands[command])):
                position = 0
                next_cheack_position = 0
                current_search_command = f"jarvis {commands[command][command_str]}"
                while position != -1:
                    position = command_string.find(current_search_command, next_cheack_position)
                    next_cheack_position = position+1
                    if position != -1:
                        command_position.append(
                            [
                                command,
                                command_str,
                                [
                                    position,
                                    (position+len(current_search_command))
                                ]
                            ]
                        )
        currected_list = []
        sorted_list = [None]*len(command_position)

        gide_list_endpoint= [sum(i[2]) for i in command_position]
        gide_list_startpoint= [sum(i[2]) for i in command_position]
        gide_list_endpoint.sort()

        for position in range(len(command_position)):
            index = gide_list_endpoint.index(gide_list_startpoint[position])
            sorted_list[index] = command_position[position]
        
        for items in range(len(sorted_list)):
            strip_position_1 = sorted_list[items][2][1]
            try:
                strip_position_2 = sorted_list[items+1][2][0]
                sorted_list[items].append(command_string[strip_position_1:strip_position_2])
            except:
                sorted_list[items].append(command_string[strip_position_1:])
        print(sorted_list)
        
        def function_runner(command, function):
            print(command)
            delay_function(command)
            function(command)

        for command_data in sorted_list:
            fucnction_to_run = functions[command_data[0]]
            string_after_command = command_data[3]
            thread = threading.Thread(target=function_runner, args=(string_after_command, fucnction_to_run))
            thread.start()




    def speach_get(self, time_len):
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

    def read_mail(self, commands, functions):
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
            m.close()   
            m.logout()
            with open("backchatmail.txt", "w") as opener:
                zd = bent[0].split()
                opener.write(str(len(bent[0].split())+1))   
            return do

    def send_mail(self, toaddr, body):
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
                server.sendmail("jarvisbackchat@gmail.com", toaddr, text)
                b = False
            except:
                pass
        print("mail sent")

def frog(x):
    print("frogger", x)

if __name__ == "__main__":
    jarvis = main()
    
    jarvis.search_algorithm([["leave", "goodbye"]], [frog], "jarvis leave pog delay 5", "jarvis")
