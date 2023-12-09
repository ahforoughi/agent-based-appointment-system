import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create SMTP connection
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "zahraarabinarei1998@gmail.com"
smtp_password = "yofxuonbqbevoqsw"

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    print("Ready for message")
except Exception as e:
    print("Error:", str(e))

# Compose email
email_from = smtp_username
email_to = "amirhosseinforoughi2@gmail.com"
email_subject = "Your Subject"
email_body = "Your HTML content"

msg = MIMEMultipart()
msg["From"] = email_from
msg["To"] = email_to
msg["Subject"] = email_subject
msg.attach(MIMEText(email_body, "html"))

# Send email
try:
    server.sendmail(email_from, email_to, msg.as_string())
    server.quit()
    print("Email sent successfully.")
except Exception as e:
    print("Error sending email:", str(e))