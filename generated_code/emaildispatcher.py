from typing import Dict, Any
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailDispatcher:
    """
    EmailDispatcher handles the sending of validated emails to intended recipients.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str) -> None:
        """
        Initializes the EmailDispatcher with SMTP server credentials.

        :param smtp_server: The SMTP server address.
        :param smtp_port: The port number for the SMTP server.
        :param username: The username for SMTP authentication.
        :param password: The password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, complete_email: Dict[str, Any]) -> str:
        """
        Sends the email to the intended recipient.

        :param complete_email: A dictionary containing 'to', 'subject', and 'body' of the email.
        :return: Dispatch status as a string.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = complete_email['to']
            msg['Subject'] = complete_email['subject']

            msg.attach(MIMEText(complete_email['body'], 'plain'))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)

            return 'Email dispatched successfully.'
        except Exception as e:
            return f'Failed to dispatch email: {str(e)}'

# Example usage
if __name__ == "__main__":
    email_dispatcher = EmailDispatcher("smtp.example.com", 587, "user@example.com", "password")
    email_content = {
        'to': 'recipient@example.com',
        'subject': 'Test Email',
        'body': 'This is a test email.'
    }
    status = email_dispatcher.send_email(email_content)
    print(status)