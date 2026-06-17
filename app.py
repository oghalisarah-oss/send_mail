from utils import email, my_password, modify, read_file
from build_html import build_birthday_email
from send import send_birthday_email
import os


def main():
    content = modify(read_file("data/Birthday_Wish_Template (1).txt"), "Saysay", "Sarah")
    # print(content)
    html = build_birthday_email(name="Saysay", body_text=content, sender_name="Sarah")
    # print(html)
    send_birthday_email("oghalisarahifeoma@gmail.com", "Happy Birthday, Saysay! 🎉", html, "oghalisarah@gmail.com", os.getenv("my_password"))

main()