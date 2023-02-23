import smtplib

# Set up SMTP server connection
smtp_server = "" # Replace with the SMTP server for your email provider
smtp_port = 587 # Replace with the SMTP port for your email provider
sender_email = "" # Replace with your email address
password = "" # Replace with your email password
receiver_email = "" # Replace with the email address of the recipient

# Set up the email message
subject = "Test email"
body = "This is a test email sent automatically using Python!"
message = f"Subject: {subject}\n\n{body}"

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

print("Email sent successfully!")
