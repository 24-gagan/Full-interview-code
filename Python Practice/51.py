import re

# Validating email addresses
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email="user@example.com"
if re.fullmatch(email_pattern,email):
    print("valid email")
else:
    print("invalid email")