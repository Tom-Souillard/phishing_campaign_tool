from typing import List

def load_email_list(file_path: str) -> List[str]:
    """Load a list of email addresses from a file.

    Args:
        file_path (str): The path to the file containing email addresses.

    Returns:
        List[str]: A list of email addresses.
    """
    with open(file_path, 'r') as file:
        emails = [line.strip() for line in file if line.strip()]
    return emails

def load_email_template(file_path: str) -> str:
    """Load an email template from a file.

    Args:
        file_path (str): The path to the file containing the email template.

    Returns:
        str: The email template as a string.
    """
    with open(file_path, 'r') as file:
        template = file.read()
    return template
