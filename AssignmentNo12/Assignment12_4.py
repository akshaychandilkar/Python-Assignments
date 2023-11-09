import os
import psutil
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Function to get process information
def get_process_info():
    processes_info = []
    for process in psutil.process_iter(attrs=['name', 'pid', 'username']):
        processes_info.append({
            'Name': process.info['name'],
            'PID': process.info['pid'],
            'Username': process.info['username'],
        })
    return processes_info

# Function to create a log file
def create_log_file(directory_name, processes_info):
    log_file_path = os.path.join(directory_name, 'process_info.log')
    with open(log_file_path, 'w') as log_file:
        for process_info in processes_info:
            log_file.write(f"Name: {process_info['Name']}, PID: {process_info['PID']}, Username: {process_info['Username']}\n")
    return log_file_path

# Function to send the log file via email
def send_email(email, log_file_path):
    sender_email = 'akshaychandilkar@gmail.com'  # Replace with your Gmail address
    sender_password = 'mclcpgmxltkevyog'  # Replace with your Gmail password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = 'Process Information Log'

    # Attach the log file to the email
    with open(log_file_path, 'rb') as log_file:
        attach = MIMEApplication(log_file.read(), _subtype="txt")
        attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(log_file_path))
        msg.attach(attach)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, email, msg.as_string())
    server.quit()

def main():
    if len(sys.argv) != 3:
        print("Usage: ProcInfoLog.py <Directory_Name> <Mail_ID>")
        sys.exit(1)

    directory_name = sys.argv[1]
    email = sys.argv[2]

    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

    processes_info = get_process_info()
    log_file_path = create_log_file(directory_name, processes_info)

    send_email(email, log_file_path)
    print("Log file sent to", email)

if __name__ == '__main__':
    main()
