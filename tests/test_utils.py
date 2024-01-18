import pytest
from phishing_campaign_tool.utils import load_email_list, load_email_template


def test_load_email_list(tmp_path):
    """Test loading an email list from a file."""
    email_file = tmp_path / "emails.txt"
    email_file.write_text("user1@example.com\nuser2@example.com\n")

    emails = load_email_list(str(email_file))
    assert emails == ["user1@example.com", "user2@example.com"]


def test_load_email_template(tmp_path):
    """Test loading an email template from a file."""
    template_file = tmp_path / "template.txt"
    template_file.write_text("This is a test template.")

    template = load_email_template(str(template_file))
    assert template == "This is a test template."
