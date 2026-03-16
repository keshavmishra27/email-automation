import smtplib
from email.message import EmailMessage
from datetime import datetime
import os

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
SUBJECT = "Daily Update"


def load_emails():
    with open("emails.txt", "r") as f:
        # Strip whitespace, newlines, and trailing commas/punctuation
        emails = [line.strip().strip(',').strip() for line in f]
        return [email for email in emails if email]

def send_email(to_email):
    if not to_email or "@" not in to_email:
        print(f"Skipping invalid email address: '{to_email}'")
        return

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = SUBJECT

    msg.set_content(f"""
Hello,

This is your automated daily email.
Sent on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Regards,
Automation Agent
""")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, APP_PASSWORD)
            server.send_message(msg)
    except smtplib.SMTPRecipientsRefused as e:
        print(f"Recipient refused for {to_email}: {e}")
    except Exception as e:
        print(f"Failed to send to {to_email}: {e}")

def main():
    emails = load_emails()
    for email in emails:
        send_email(email) #comment here before sending mails to crosscheck no. of mails
        print(f"Sent to {email}")

if __name__ == "__main__":
    main()

