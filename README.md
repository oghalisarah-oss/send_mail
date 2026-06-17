# 🎉 Birthday Email Automation

A Python application that automatically generates and sends personalized, beautifully formatted birthday emails via Gmail SMTP.

## 📋 Overview

This project streamlines the process of sending birthday greetings by:
- Loading a customizable birthday message template
- Personalizing it with the recipient's and sender's names
- Converting the message into a polished HTML email with professional styling
- Sending the email via Gmail's SMTP server

## ✨ Features

- **Customizable Templates**: Use any text file as a birthday message template with `{name}` and `[Your Name]` placeholders
- **Professional HTML Emails**: Beautiful gradient header with emojis, responsive design, and elegant typography
- **Gmail Integration**: Send emails directly using Gmail SMTP with App Password authentication
- **Environment Variables**: Secure credential management using `.env` file
- **Personalization**: Automatically replaces placeholders with recipient and sender information
- **Fallback Support**: HTML emails with plain-text fallback for clients that don't support HTML

## 📧 Email Output Example

Here's what the birthday email looks like when received:

![Birthday Email Preview](WhatsApp%20Image%202026-06-17%20at%2012.43.58%20PM.jpeg)

The email features:
- Eye-catching gradient header with birthday emojis
- Personalized greeting with recipient's name
- Clean, readable typography with 1.7 line-height
- Decorative divider
- Footer with celebratory message

## 📁 Project Structure

```
├── app.py                              # Main entry point
├── build_html.py                       # HTML email builder
├── send.py                             # SMTP email sender
├── utils.py                            # Utility functions (file I/O, text replacement)
├── main.ipynb                          # Jupyter notebook for experimentation
├── data/
│   ├── Birthday_Wish_Template (1).txt # Customizable email template
│   └── products.csv                   # Additional data file
├── .env                               # Environment variables (credentials)
└── README.md                          # This file
```

## 🔧 Technical Details

### Core Modules

**`app.py`** - Main application orchestrator
- Loads the birthday template
- Customizes the message with names
- Builds the HTML email
- Sends via SMTP

**`build_html.py`** - HTML email builder
- `build_birthday_email()`: Converts plain text to professional HTML with:
  - Responsive email design (600px max-width)
  - Gradient background (coral/peach gradient)
  - Proper paragraph and line break handling
  - Email-safe styling

**`send.py`** - SMTP email sender
- `send_birthday_email()`: Sends HTML emails via Gmail
- Supports STARTTLS encryption on port 587
- Includes plain-text fallback for compatibility
- Uses `email.mime` for proper multipart message construction

**`utils.py`** - Helper functions
- `read_file()`: Reads template files with UTF-8 encoding
- `modify()`: Replaces `{name}` and `[Your Name]` placeholders
- Environment variable loading via `python-dotenv`

## 🚀 Setup & Usage

### Prerequisites

- Python 3.x
- Gmail account with App Password enabled
- `python-dotenv` package

### Installation

1. **Clone or download the project**

2. **Install dependencies**:
   ```bash
   pip install python-dotenv
   ```

3. **Set up environment variables** in `.env`:
   ```
   my_email=your_email@gmail.com
   my_password=your_gmail_app_password
   ```
   
   **Note**: Use a [Gmail App Password](https://support.google.com/accounts/answer/185833), not your regular password.

### Running the Application

1. **Edit `app.py`** with your details:
   ```python
   send_birthday_email(
       "recipient@example.com",           # Birthday person's email
       "Happy Birthday, [Name]! 🎉",     # Email subject
       html,                              # Generated HTML (auto-created)
       "your_email@gmail.com",           # Your email (from .env)
       os.getenv("my_password")          # Your app password (from .env)
   )
   ```

2. **Customize the template** in `data/Birthday_Wish_Template (1).txt`:
   - Use `{name}` for the birthday person's name
   - Use `[Your Name]` for your name
   - Keep paragraphs separated by blank lines

3. **Run the application**:
   ```bash
   python app.py
   ```

## 📝 Customization

### Modify the Email Template

Edit `data/Birthday_Wish_Template (1).txt` to change the birthday message. The template supports:
- Dynamic name replacement: `{name}` → Birthday person's name
- Sender identification: `[Your Name]` → Your name
- Multiple paragraphs (separated by blank lines)
- Emojis and special characters

### Customize Email Styling

In `build_html.py`, modify the HTML/CSS for:
- **Colors**: Change gradient in `background:linear-gradient(135deg, #ff7e5f 0%, #feb47b 50%, #ff6a88 100%)`
- **Font size**: Adjust values in `style` attributes
- **Spacing**: Modify `padding` and `margin` properties
- **Emojis**: Update emoji choices in header/footer

## 🔒 Security Notes

- Never commit `.env` file to version control (it's in `.gitignore`)
- Use Gmail App Passwords instead of your actual password
- Store credentials only in `.env` files
- The project includes `.gitignore` to prevent accidental credential leaks

## 📚 Dependencies

- `python-dotenv`: For secure environment variable management
- `smtplib`: Built-in Python module for SMTP
- `email`: Built-in Python module for email construction
- `re`: Built-in regex module for text processing

## 🎯 Future Enhancements

- Batch sending to multiple recipients
- HTML template files instead of hard-coded HTML
- Subject line customization in config
- Scheduling emails for future dates
- Email delivery logging and error handling
- Support for additional email providers (SendGrid, AWS SES, etc.)

## 📄 License

This project is open-source and available for personal use.

---

**Created**: June 17, 2026  
**Made with ❤️ for celebrating birthdays**
