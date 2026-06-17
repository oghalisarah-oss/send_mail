import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def build_birthday_email(name: str, body_text: str, sender_name: str = "") -> str:
    """
    Wrap a plain-text birthday message into a polished HTML email.

    Args:
        name: The recipient's name (used in the header/banner).
        body_text: The full personalized message (the text you already
                   filled {name} into). Paragraphs should be separated
                   by blank lines (\\n\\n).
        sender_name: Optional override for the signature line. If not
                     provided, the function tries to detect a trailing
                     "Warmest wishes,\\nX" style signature in body_text
                     and keep it; otherwise leaves it as-is.

    Returns:
        A full HTML document (string) ready to use as the email's HTML body.
    """

    # Split the message into paragraphs based on blank lines
    raw_paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body_text.strip()) if p.strip()]

    # Convert each paragraph into an HTML <p>, preserving single line breaks as <br>
    html_paragraphs = []
    for para in raw_paragraphs:
        para_html = para.replace("\n", "<br>")
        html_paragraphs.append(f'<p style="margin:0 0 20px 0; font-size:16px; line-height:1.7; color:#444444;">{para_html}</p>')

    body_html = "\n".join(html_paragraphs)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Birthday, {name}!</title>
</head>
<body style="margin:0; padding:0; background-color:#f4f1ec; font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f1ec; padding:40px 0;">
    <tr>
      <td align="center">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%; background-color:#ffffff; border-radius:16px; overflow:hidden; box-shadow:0 8px 30px rgba(0,0,0,0.08);">

          <!-- Header banner -->
          <tr>
            <td style="background:linear-gradient(135deg, #ff7e5f 0%, #feb47b 50%, #ff6a88 100%); padding:50px 30px; text-align:center;">
              <div style="font-size:48px; line-height:1; margin-bottom:10px;">🎉🎂🎈</div>
              <h1 style="margin:0; font-size:32px; color:#ffffff; font-weight:700; letter-spacing:0.5px; text-shadow:0 2px 6px rgba(0,0,0,0.15);">
                Happy Birthday, {name}!
              </h1>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="padding:40px 40px 20px 40px;">
              {body_html}
            </td>
          </tr>

          <!-- Decorative divider -->
          <tr>
            <td style="padding:0 40px;">
              <div style="height:1px; background-color:#eeeeee; margin:10px 0 30px 0;"></div>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="padding:0 40px 40px 40px; text-align:center;">
              <div style="font-size:28px; margin-bottom:8px;">🎈🥳🎁</div>
              <p style="margin:0; font-size:13px; color:#aaaaaa;">Sent with love, on your special day.</p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>"""

    return html