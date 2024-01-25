from typing import List
from phishing_campaign_tool.email_sender import send_email


def run_phishing_campaign(subject: str, body: str, from_email: str, to_emails: List[str], smtp_server: str,
                          smtp_port: int, login: str, password: str) -> None:
    """Run a phishing campaign by sending phishing emails to a list of recipients.

    Args:
        subject (str): The subject of the phishing email.
        body (str): The body of the phishing email.
        from_email (str): The sender's email address.
        to_emails (List[str]): List of recipient email addresses.
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        login (str): The login for the SMTP server.
        password (str): The password for the SMTP server.
    """
    send_email(subject, body, from_email, to_emails, smtp_server, smtp_port, login, password)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 8:
        print(
            "Usage: python campaign.py <subject> <body> <from_email> <to_emails_comma_separated> <smtp_server> <smtp_port> <login> <password>")
    else:
        subject = sys.argv[1]
        body = sys.argv[2]
        from_email = sys.argv[3]
        to_emails = sys.argv[4].split(',')
        smtp_server = sys.argv[5]
        smtp_port = int(sys.argv[6])
        login = sys.argv[7]
        password = sys.argv[8]

        run_phishing_campaign(subject, body, from_email, to_emails, smtp_server, smtp_port, login, password)
