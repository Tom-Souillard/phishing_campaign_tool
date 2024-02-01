from phishing_campaign_tool.utils import load_email_list, load_email_template
from phishing_campaign_tool.campaign import run_phishing_campaign

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 8:
        print("Usage: python run_campaign.py <subject> <template_path> <from_email> <email_list_path> <smtp_server> <smtp_port> <login> <password>")
    else:
        subject = sys.argv[1]
        template_path = sys.argv[2]
        from_email = sys.argv[3]
        email_list_path = sys.argv[4]
        smtp_server = sys.argv[5]
        smtp_port = int(sys.argv[6])
        login = sys.argv[7]
        password = sys.argv[8]

        body = load_email_template(template_path)
        to_emails = load_email_list(email_list_path)

        run_phishing_campaign(subject, body, from_email, to_emails, smtp_server, smtp_port, login, password)
