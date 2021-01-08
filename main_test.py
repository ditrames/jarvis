from home_assistant import HomeAssistant, Mail, Speach
from commands import command_relations
import time

mailbox = Mail('jarvisbackchat@gmail.com', 'JARVIS_EMAIL_PASSWORD')
speach = Speach(10)
jarvis = HomeAssistant.from_command_relations('(gary|garry)', command_relations)
while 1:
    mail = mailbox.read_mail()
    print(mail)
    parsed_string = jarvis.parse_string(mail)
    jarvis.run_commands(parsed_string)

    speach_out = speach.recognise_speach()
    print(speach_out)
    parsed_string = jarvis.parse_string(speach_out)
    jarvis.run_commands(parsed_string)
