import os
import shutil
from datetime import datetime
import logging
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def setup_logger(log_folder):
    log_file = os.path.join(log_folder, "backup_log.txt")
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    return logging.getLogger(), log_file

def backup_folder(source_folder, backup_base_folder):
    # Today's date folder name in dd-mm-yyyy format
    date_str = datetime.now().strftime("%d-%m-%Y")
    backup_folder_path = os.path.join(backup_base_folder, date_str)

    # Create the backup directory if it doesn't exist
    os.makedirs(backup_folder_path, exist_ok=True)

    # Setup logger
    logger, log_file = setup_logger(backup_folder_path)
    logger.info(f"Backup started for folder: {source_folder}")

    file_type_count = {}
    total_files_copied = 0

    # Iterate over files in source_folder
    for filename in os.listdir(source_folder):
        src_file = os.path.join(source_folder, filename)

        if os.path.isfile(src_file):
            _, ext = os.path.splitext(filename)
            ext = ext.lower() if ext else "No Extension"
            dst_file = os.path.join(backup_folder_path, filename)

            try:
                shutil.copy2(src_file, dst_file)
                logger.info(f"Copied file: {filename}")
                print(f"Copied: {filename}")

                file_type_count[ext] = file_type_count.get(ext, 0) + 1
                total_files_copied += 1
            except Exception as e:
                logger.error(f"Failed to copy {filename}: {e}")
                print(f"Failed to copy {filename}: {e}")

    logger.info(f"Backup completed. Total files copied: {total_files_copied}")
    print(f"\nBackup complete! Total files copied: {total_files_copied}")
    print(f"Backup folder: {backup_folder_path}\n")

    print("File type count:")
    for ext, count in sorted(file_type_count.items()):
        ext_print = ext if ext != "No Extension" else "[No Extension]"
        print(f"{ext_print}: {count}")
        logger.info(f"File type {ext_print} count: {count}")

    return log_file

def send_email_with_attachment(sender_email, receiver_email, password, subject, body, attachment_path):
    # Create a multipart email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the email body text
    message.attach(MIMEText(body, "plain"))

    # Attach the log file
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters for email
    encoders.encode_base64(part)

    # Add header for the attachment
    filename = os.path.basename(attachment_path)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={filename}",
    )
    message.attach(part)

    # Create secure connection and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print(f"Email sent to {receiver_email} with attachment {filename}")

def main():
    source = input("Enter the source folder path: ").strip()
    backup_base = input("Enter the backup base folder path: ").strip()

    if not os.path.isdir(source):
        print("Error: Source folder does not exist.")
        return
    if not os.path.isdir(backup_base):
        print("Error: Backup base folder does not exist.")
        return

    # Run backup and get the path to the log file
    log_file_path = backup_folder(source, backup_base)

    # Email details
    sender_email = input("Enter sender email address: ").strip()
    receiver_email = input("Enter receiver email address: ").strip()
    password = input("Enter sender email password (or app password): ").strip()

    subject = " The File Transfer and Backup Log File is Completed"
    body = f"Attached is the backup log generated on {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}."

    # Send the email with the log file attached
    try:
        send_email_with_attachment(sender_email, receiver_email, password, subject, body, log_file_path)
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    main()
