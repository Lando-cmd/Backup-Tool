import os
import zipfile
import shutil
import sys


# Function to backup files with compression
def backup(source, destination):
    # Check if the source directory exists
    if not os.path.exists(source):
        print(f"Source directory {source} does not exist. Please try again.")
        return

    # Create a zip file in the destination directory
    backup_filename = os.path.basename(source.rstrip(os.sep)) + "_backup.zip"
    backup_filepath = os.path.join(destination, backup_filename)

    # Create the zip file and add the contents of the source folder
    try:
        with zipfile.ZipFile(backup_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the directory and add all files and subdirectories to the zip file
            for root, dirs, files in os.walk(source):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=source)  # Preserve directory structure inside the zip
                    zipf.write(file_path, arcname)

        print(f"Backup completed successfully! The backup is saved as {backup_filepath}")
    except Exception as e:
        print(f"Error during backup: {e}")


# Function to restore files from a zip archive
def restore(source, destination):
    # Check if the source zip file exists
    if not os.path.exists(source):
        print(f"Backup file {source} does not exist. Please try again.")
        return

    # Check if the destination directory exists; if not, create it
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Extract the contents of the zip file to the destination
    try:
        with zipfile.ZipFile(source, 'r') as zipf:
            zipf.extractall(destination)

        print(f"Restore completed successfully! The files have been extracted to {destination}")
    except Exception as e:
        print(f"Error during restore: {e}")


# Main function to interact with the user
def main():
    print("Welcome to the Backup and Recovery Tool!\n")

    while True:
        # Ask the user what they want to do
        action = input(
            "Would you like to 'backup' or 'restore' files? (Type 'backup' or 'restore', or 'exit' to quit): ").strip().lower()

        if action == 'backup':
            # Prompt for source and destination for backup
            source_folder = input("Enter the full path of the folder to back up: ").strip()
            destination_folder = input(
                "Enter the full path where the backup should be saved (e.g., 'C:\\Users\\Desktop'): ").strip()

            # Perform the backup
            backup(source_folder, destination_folder)

        elif action == 'restore':
            # Prompt for source and destination for restore
            source_backup_file = input("Enter the full path of the backup zip file: ").strip()
            destination_folder = input("Enter the full path where the files should be restored: ").strip()

            # Perform the restore
            restore(source_backup_file, destination_folder)

        elif action == 'exit':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid command. Please enter 'backup', 'restore', or 'exit'.\n")


# Run the program
if __name__ == "__main__":
    main()
