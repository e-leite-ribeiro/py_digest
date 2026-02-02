import smtplib
from email.message import EmailMessage

class EmailSender:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
    
    def send(self, subject: str, body: str, sender: str, recipient: str):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["FROM"] = sender
        msg["TO"] = recipient
        msg.set_content(body)

        with smtplib.SMTP(self.host, self.port) as server:
            server.starttls()
            server.login(self.user, self.password)
            server.send_message(msg)
