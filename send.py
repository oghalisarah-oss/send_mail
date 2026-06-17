import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_birthday_email(
    to_email: str,
    subject: str,
    html_content: str,
    smtp_user: str,
    smtp_password: str,
    smtp_host: str = "smtp.gmail.com",
    smtp_port: int = 587,
    plain_text_fallback: str = None,
):
    """
    Send the HTML birthday email via SMTP (defaults configured for Gmail).

    Args:
        to_email: Recipient's email address.
        subject: Email subject line.
        html_content: HTML body, e.g. from build_birthday_email().
        smtp_user: Your sending email address.
        smtp_password: Your email account password or app password
                        (for Gmail, use an App Password, not your normal password).
        smtp_host: SMTP server host (default: Gmail).
        smtp_port: SMTP server port (default: 587, STARTTLS).
        plain_text_fallback: Optional plain-text version for email clients
                              that don't render HTML. If not given, a simple
                              fallback is auto-generated.
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_email

    if plain_text_fallback is None:
        plain_text_fallback = "Happy Birthday! (View this email in HTML for the full experience.)"

    msg.attach(MIMEText(plain_text_fallback, "plain"))
    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())