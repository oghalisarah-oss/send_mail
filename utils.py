import os
from dotenv import load_dotenv
load_dotenv(override=True)

my_password = os.getenv("my_password")
email = os.getenv("my_email")

def read_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        output = f.read()
    return output
    
def modify(output: str, name: str, your_name: str):
    new_output = output.replace("{name}", name).replace("[Your Name]", your_name)

    return new_output