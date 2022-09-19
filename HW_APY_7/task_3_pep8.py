import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailUser:

    def __init__(self, login_, password_):
        self.login = login_
        self.password = password_

    def send_email(self, out_server: str, port: int, recipients: list, email_subject: str, email_text):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_text))
        smtp_obj = smtplib.SMTP(out_server, port)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.ehlo()
        smtp_obj.login(self.login, self.password)
        smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp_obj.quit()

    def receive_email(self, in_server, email_folder, header=None):
        mail = imaplib.IMAP4_SSL(in_server)
        mail.login(self.login, self.password)
        mail.list()
        mail.select(email_folder)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email.decode('utf-8'))
        mail.logout()
        return email_message


if __name__ == '__main__':

    someone = EmailUser('login@gmail.com', 'qwerty')

    someone.send_email("smtp.gmail.com",
                       587,
                       ['vasya@email.com', 'petya@email.com'],
                       'test', 'Hello world!'
                       )
    print(someone.receive_email("imap.gmail.com", 'inbox'))
