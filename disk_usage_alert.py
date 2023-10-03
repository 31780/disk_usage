import shutil
import smtplib
from email.message import EmailMessage

# Define threshold (in percentage) for disk usage alert
DISK_USAGE_THRESHOLD = 80

# Define email settings
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'you@example.com'
EMAIL_PASSWORD = 'your_email_password'
TO_ADDRESS = 'admin@example.com'

def get_disk_usage(path="/"):
    """
    Return disk usage percentage of the given path.
    """
    _, _, free = shutil.disk_usage(path)
    return 100 - (free / _ * 100)

def send_email_alert(subject, body):
    """
    Send an email alert with the given subject and body.
    """
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_ADDRESS
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

def monitor_disk_usage():
    """
    Monitor disk usage and send an email alert if above threshold.
    """
    usage = get_disk_usage()
    if usage > DISK_USAGE_THRESHOLD:
        subject = "Disk Usage Alert"
        body = f"Disk usage has exceeded the threshold:\nCurrent Usage: {usage:.2f}%"
        send_email_alert(subject, body)
        print("Alert sent.")
    else:
        print(f"Disk usage: {usage:.2f}%. All good.")

if __name__ == "__main__":
    monitor_disk_usage()
