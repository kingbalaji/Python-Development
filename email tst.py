import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "balajiravi1612@gmail.com"
receiver_email = "kingbalaji46@gmail.com"
password = "balaji995$"

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Subject of the Email"

# Email body
body = "This is the body of the email."
message.attach(MIMEText(body, "plain"))

# Attach a file
file_path = "C:\Users\Kumar\Documents\Balaji\file.txt" # Change to your file path
with open(file_path, "rb") as attachment:
    part = MIMEApplication(attachment.read(), Name="file.txt")
    part['Content-Disposition'] = f'attachment; filename="file.txt"'
    message.attach(part)

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(sender_email, password)
    server.send_message(message)

print("Email sent successfully!")
