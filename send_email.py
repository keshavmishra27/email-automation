import smtplib
from email.message import EmailMessage
from datetime import datetime


EMAIL_ADDRESS = "keshavmishra1729@gmail.com"
APP_PASSWORD = "**** **** **** ****"
SUBJECT = "Daily Update"


def load_emails():
    with open("emails.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]

def send_email(to_email):
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

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, APP_PASSWORD)
        server.send_message(msg)

def main():
    emails = load_emails()
    for email in emails:
        send_email(email)
        print(f"Sent to {email}")

if __name__ == "__main__":
    main()

