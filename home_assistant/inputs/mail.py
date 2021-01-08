import email
import imaplib
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from imap_tools import MailBox, AND, MailMessageFlags


class Mail:
    def __init__(self, address, address_password_evar):
        self.email_address = address
        self.password = os.environ.get(address_password_evar)

        self.outbox = smtplib.SMTP('smtp.gmail.com', 587)
        self.outbox.ehlo()
        self.outbox.starttls()
        self.outbox.ehlo()
        self.outbox.login(self.email_address, self.password)

    def read_mail(self, delete=False):
        self.mailbox = MailBox('imap.gmail.com')
        self.mailbox.login(self.email_address, self.password, initial_folder='INBOX')

        incoming = [msg for msg in self.mailbox.fetch(AND(seen=False))]
        out = ' '.join(msg.text for msg in incoming)
        # flags = (MailMessageFlags.FLAGGED,)
        self.mailbox.seen(self.mailbox.fetch(AND(flagged=False)), True)

        self.mailbox.logout()
        return out

    def send_mail(self, toaddr, body, subject):
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = toaddr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()
        self.outbox.sendmail("jarvisbackchat@gmail.com", toaddr, text)

    def delete_all(self):

        self.mailbox.expunge()
