import os
import shutil
import datetime
import smtplib
from collections import defaultdict
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def get_user_input():
    """Prompt user for source folder and email address."""
    source_folder = input("Enter the path to the source folder: ").strip()
    recipient_email = input("Enter the recipient email address: ").strip()
    return source_folder, recipient_email

def count_files_by_extension(folder_path):
    """Count files in folder by their extensions."""
    extension_counts = defaultdict(int)

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            _, extension = os.path.splitext(filename)
            extension = extension.lower() if extension else "no_extension"
            extension_counts[extension] += 1

    return dict(sorted(extension_counts.items()))

def copy_and_backup_files(source_folder, backup_folder):
    """Copy files from source to backup folder with date."""
    os.makedirs(backup_folder, exist_ok=True)

    log_lines = [
        f"Backup Log - {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
        "=" * 40,
        f"Source Folder: {source_folder}",
        f"Backup Folder: {backup_folder}",
        ""
    ]

    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    files_copied = 0

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            name, ext = os.path.splitext(filename)
            backup_filename = f"{name}_{current_date}{ext}"
            backup_path = os.path.join(backup_folder, backup_filename)

            shutil.copy2(source_path, backup_path)
            log_lines.append(f"Copied: {filename:40} -> {backup_filename}")
            files_copied += 1

    log_lines.extend([
        "",
        f"Total files copied: {files_copied}",
        "Backup completed successfully."
    ])

    return "\n".join(log_lines)

def send_email_with_log(log_content, log_file_path, recipient_email, sender_email, sender_password):
    """Send log content via email with the log file as an attachment."""
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Backup Log Report"

    body = "Please find attached the backup operation log file."
    msg.attach(MIMEText(body, 'plain'))

    # Attach the log file
    with open(log_file_path, "rb") as log_file:
        part = MIMEApplication(log_file.read(), Name=os.path.basename(log_file_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(log_file_path)}"'
        msg.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def print_extension_report(extension_counts):
    """Print formatted extension count report."""
    print("\nFile Extension Count in Source Folder:")
    print("-" * 40)
    for ext, count in sorted(extension_counts.items()):
        print(f"{ext if ext != 'no_extension' else 'No Extension'}: {count}")

def main():
    print("File Backup System")
    print("=" * 40)

    # Get user input
    source_folder, recipient_email = get_user_input()

    # Verify folder exists
    while not os.path.isdir(source_folder):
        print(f"Error: Folder not found - {source_folder}")
        source_folder = input("Enter a valid source folder path: ").strip()

    backup_folder = os.path.join(source_folder, "Backup_" + datetime.datetime.now().strftime("%Y%m%d"))

    # Count files by extension
    ext_counts = count_files_by_extension(source_folder)
    print_extension_report(ext_counts)

    # Create log content
    log_content = copy_and_backup_files(source_folder, backup_folder)
    log_content += "\n\nFile Extension Counts:\n" + "-" * 40 + "\n"
    log_content += "\n".join([f"{ext}: {count}" for ext, count in ext_counts.items()])

    # Save log file
    log_file_path = os.path.join(backup_folder, "backup_log.txt")
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    with open(log_file_path, 'w') as log_file:
        log_file.write(log_content)

    # Email credentials (you might want to get these from user input or env variables)
    sender_email = "balajiravi1612@gmail.com"  # Update with your email
    sender_password = "hptg jppg eqhp ayjk"  # Update with your app password

    # Send email
    if send_email_with_log(log_content, log_file_path, recipient_email, sender_email, sender_password):
        print(f"\nBackup completed. Log sent to {recipient_email}")
    else:
        print("\nBackup completed but failed to send email.")

    print(f"\nBackup files saved to: {backup_folder}")
    print(f"Log file created at: {log_file_path}")

if __name__ == "__main__":
    main()
