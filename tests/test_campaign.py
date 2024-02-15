import pytest
from phishing_campaign_tool.campaign import run_phishing_campaign


def test_run_phishing_campaign(monkeypatch):
    """Test running a phishing campaign using a mock email sender."""

    def mock_send_email(subject, body, from_email, to_emails, smtp_server, smtp_port, login, password):
        assert subject == "Test Subject"
        assert body == "This is a test body"
        assert from_email == "sender@example.com"
        assert to_emails == ["recipient1@example.com", "recipient2@example.com"]
        assert smtp_server == "smtp.example.com"
        assert smtp_port == 587
        assert login == "login"
        assert password == "password"

    monkeypatch.setattr("phishing_campaign_tool.email_sender.send_email", mock_send_email)

    run_phishing_campaign(
        subject="Test Subject",
        body="This is a test body",
        from_email="sender@example.com",
        to_emails=["recipient1@example.com", "recipient2@example.com"],
        smtp_server="smtp.example.com",
        smtp_port=587,
        login="login",
        password="password"
    )
