import os
import shutil
from datetime import datetime
import logging


def setup_logger(log_folder):
    log_file = os.path.join(log_folder, "backup_log.txt")
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    return logging.getLogger()


def backup_folder(source_folder, backup_base_folder):
    # Today's date folder name in dd-mm-yyyy format
    date_str = datetime.now().strftime("%d-%m-%Y")
    backup_folder_path = os.path.join(backup_base_folder, date_str)

    # Create the backup directory if it doesn't exist
    os.makedirs(backup_folder_path, exist_ok=True)

    # Setup logger
    logger = setup_logger(backup_folder_path)
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


def main():
    source = input("Enter the source folder path: ").strip()
    backup_base = input("Enter the backup base folder path: ").strip()

    # Validate both paths
    if not os.path.isdir(source):
        print("Error: Source folder does not exist.")
        return
    if not os.path.isdir(backup_base):
        print("Error: Backup base folder does not exist.")
        return

    backup_folder(source, backup_base)


if __name__ == "__main__":
    main()
