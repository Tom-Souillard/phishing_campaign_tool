import pytest
from phishing_campaign_tool.email_sender import send_email


def test_send_email(monkeypatch):
    """Test sending an email using a mock SMTP server."""

    class MockSMTP:
        def __init__(self, *args, **kwargs):
            pass

        def starttls(self):
            pass

        def login(self, login, password):
            pass

        def sendmail(self, from_email, to_emails, msg):
            assert from_email == "sender@example.com"
            assert to_emails == ["recipient@example.com"]
            assert "Subject: Test Subject" in msg
            assert "This is a test body" in msg

        def quit(self):
            pass

    monkeypatch.setattr("smtplib.SMTP", MockSMTP)

    send_email(
        subject="Test Subject",
        body="This is a test body",
        from_email="sender@example.com",
        to_emails=["recipient@example.com"],
        smtp_server="smtp.example.com",
        smtp_port=587,
        login="login",
        password="password"
    )
