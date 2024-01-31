import pytest
from scripts.generate_email_list import generate_email_list


def test_generate_email_list(tmp_path):
    """Test generating a sample email list."""
    email_file = tmp_path / "emails.txt"

    generate_email_list(str(email_file), 3)

    content = email_file.read_text().strip().split("\n")
    assert len(content) == 3
    assert content[0] == "user0@example.com"
    assert content[1] == "user1@example.com"
    assert content[2] == "user2@example.com"
