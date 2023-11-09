import os
import hashlib
import time
import datetime
import smtplib
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Function to calculate checksum of a file
def calculate_checksum(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(8192)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

# Function to delete duplicate files and log their names
def delete_duplicates(directory_path, log_file_path):
    seen_checksums = set()
    duplicate_count = 0

    with open(log_file_path, 'a') as log_file:
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                checksum = calculate_checksum(file_path)
                if checksum in seen_checksums:
                    duplicate_count += 1
                    os.remove(file_path)
                    log_file.write(f"Deleted duplicate: {file_path}\n")
                else:
                    seen_checksums.add(checksum)

    return duplicate_count

# Function to send email with statistics and log file
def send_email(receiver_email, start_time, total_files_scanned, total_duplicates_found, log_file_path):
    sender_email = "akshaychandilkar811@gmail.com"
    sender_password = "jlgm baqb wdox apii"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Duplicate File Removal Report"

    body = f"Operation started at {start_time}\n"
    body += f"Total number of files scanned: {total_files_scanned}\n"
    body += f"Total number of duplicate files found: {total_duplicates_found}\n"

    msg.attach(MIMEText(body, 'plain'))

    # Attach the log file
    with open(log_file_path, "rb") as log_file:
        log_attachment = MIMEApplication(log_file.read(), _subtype="txt")
        log_attachment.add_header('content-disposition', 'attachment', filename=os.path.basename(log_file_path))
        msg.attach(log_attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", str(e))

def main():
    parser = argparse.ArgumentParser(description="Duplicate File Removal Script")
    parser.add_argument("directory", help="Absolute path of the directory containing duplicate files")
    parser.add_argument("interval", type=int, help="Time interval for script execution in minutes")
    parser.add_argument("receiver_email", help="Email ID of the receiver")
    args = parser.parse_args()

    while True:
        start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        total_files_scanned = 0
        total_duplicates_found = 0
        log_file_path = "duplicate_file_removal_log.txt"  # Specify the path for the log file

        print(f"Scanning started at {start_time}")

        total_duplicates_found = delete_duplicates(args.directory, log_file_path)
        total_files_scanned = len([f for _, _, f in os.walk(args.directory) for file in f])

        print(f"Scanning completed at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total duplicate files found: {total_duplicates_found}")
        print(f"Total files scanned: {total_files_scanned}")

        send_email(args.receiver_email, start_time, total_files_scanned, total_duplicates_found, log_file_path)
        time.sleep(args.interval * 60)  # Sleep for the specified interval

if __name__ == "__main__":
    main()
