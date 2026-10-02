import re

# Read the input file
with open("input.txt", "r") as file:
    text = file.read()

# Find email addresses
emails = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    text
)

# Remove duplicate emails
emails = list(set(emails))

# Save emails to another file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email extraction completed!")
print("Total emails found:", len(emails))