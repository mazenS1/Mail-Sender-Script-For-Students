import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path
from time import sleep


# === CONFIG ===
EMAIL_ADDRESS = "email_address"
# Generate an app password from your Google account
EMAIL_PASSWORD = "email_password"

# Change the subject to the desired subject
SUBJECT = "Co-op Major. Your Name"

# Path to resume and text file with email addresses (one per line)
RESUME_PATH = Path("Path_to_resume.pdf")
EMAILS_PATH = Path("Path_to_email_list.txt")

# Safety toggle to avoid accidental sends while testing
DRY_RUN = False
# If DRY_RUN is True, the email will be sent to the test email address
Test_Email = "example@example.com"
Test_Email2= "example@example.com" # optional


# Contact links for email signature
CONTACT_EMAIL = "example@example.com" # optional
CONTACT_PHONE = "+966000000000" # optional
GITHUB_URL = "https://github.com/your_username" # optional
LINKEDIN_URL = "https://www.linkedin.com/in/your_username/"
PORTFOLIO_URL = "https://your_portfolio_url.com" # optional


def load_emails(file_path: Path) -> list[str]:
    if DRY_RUN:
        return [Test_Email]
    """Read unique, valid-looking email addresses from a text file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Email list not found: {file_path}")

    emails: list[str] = []
    seen: set[str] = set()

    with file_path.open("r", encoding="utf-8") as f:
        for raw_line in f:
            email = raw_line.strip()
            if not email:
                continue
            if "@" not in email:
                print(f"Skipping invalid entry (no @): {email}")
                continue

            lowered = email.lower()
            if lowered in seen:
                continue

            seen.add(lowered)
            emails.append(email)

    return emails


def send_email(to_email: str) -> None:
    """Send an email with the configured subject and resume attachment."""
    if not RESUME_PATH.exists():
        raise FileNotFoundError(f"Resume not found at {RESUME_PATH}")

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = SUBJECT

    plain_body = (
        f"Dear Hiring Team,\n\n"
        f"WRITE YOUR MESSAGE HERE"
        f"✉️\u00A0Email: {CONTACT_EMAIL} | 📞\u00A0Phone: {CONTACT_PHONE} | 💻\u00A0GitHub: {GITHUB_URL} | "
        f"🔗\u00A0LinkedIn: {LINKEDIN_URL} | 🌐\u00A0Portfolio: {PORTFOLIO_URL}"
    )
    msg.set_content(plain_body)

    html_body = f"""
        <div style="font-family: Georgia, serif; 
                    font-size: 15px; 
                    line-height: 1.6; 
                    max-width: 650px; 
                    margin: 0 auto; 
                    ">

        <p>Dear Hiring Team,</p>

        <p>
            (WRITE YOUR MESSAGE HERE)
        </p>

        <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">

        <p style="font-size: 14px; color: #444;">
        <strong>
            {f'<a href="mailto:{CONTACT_EMAIL}" style="color: #0a66c2; text-decoration: none; white-space: nowrap;">&#9993;&nbsp;{CONTACT_EMAIL}</a>' if CONTACT_EMAIL else ''}
            {' | ' if CONTACT_EMAIL and CONTACT_PHONE else ''}
            {f'<a href="tel:{CONTACT_PHONE}" style="color: #0a66c2; text-decoration: none; white-space: nowrap;">&#128222;&nbsp;{CONTACT_PHONE}</a>' if CONTACT_PHONE else ''}
            {' | ' if (CONTACT_EMAIL or CONTACT_PHONE) and GITHUB_URL else ''}
            {f'<a href="{GITHUB_URL}" style="color: #0a66c2; text-decoration: none; white-space: nowrap;">&#128187;&nbsp;GitHub</a>' if GITHUB_URL else ''}
            {' | ' if (CONTACT_EMAIL or CONTACT_PHONE or GITHUB_URL) and LINKEDIN_URL else ''}
            {f'<a href="{LINKEDIN_URL}" style="color: #0a66c2; text-decoration: none; white-space: nowrap;">&#128279;&nbsp;LinkedIn</a>' if LINKEDIN_URL else ''}
            {' | ' if (CONTACT_EMAIL or CONTACT_PHONE or GITHUB_URL or LINKEDIN_URL) and PORTFOLIO_URL else ''}
            {f'<a href="{PORTFOLIO_URL}" style="color: #0a66c2; text-decoration: none; white-space: nowrap;">&#127760;&nbsp;Portfolio</a>' if PORTFOLIO_URL else ''}
        </strong>
        </p>
        </div>
        """
    msg.add_alternative(html_body, subtype="html")

    with RESUME_PATH.open("rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=RESUME_PATH.name,
        )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print(f"✅ Email sent to {to_email}")


def main() -> None:
    emails = load_emails(EMAILS_PATH)
    print(f"Loaded {len(emails)} email(s) from {EMAILS_PATH}")

    for idx, email in enumerate(emails, start=1):
        print(f"{idx}. {email}")

    if DRY_RUN:
        send_email(Test_Email)
        if Test_Email2:
            send_email(Test_Email2)
        print("DRY_RUN is enabled; no emails were sent.")
        return

    for email in emails:
        try:
            send_email(email)
            sleep(5) # sleep for 1 second for each email to avoid being blocked by the email server
        except Exception as exc:
            print(f"❌ Failed to send to {email}: {exc}")


if __name__ == "__main__":
    main()

