import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

def send_email(subject: str, body: str, from_email: str, to_emails: List[str], smtp_server: str, smtp_port: int, login: str, password: str) -> None:
    """Send an email using SMTP.

    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
        from_email (str): The sender's email address.
        to_emails (List[str]): List of recipient email addresses.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        login (str): The login for the SMTP server.
        password (str): The password for the SMTP server.
    """
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)
        text = msg.as_string()
        server.sendmail(from_email, to_emails, text)
        server.quit()
        print(f"Email sent to {', '.join(to_emails)}")
    except Exception as e:
        print(f"Failed to send email: {e}")
