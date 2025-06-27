# Backup and Recovery Tool

This Python script provides a simple command-line utility to back up folders by compressing them into ZIP archives and to restore files by extracting from those archives. It preserves the directory structure within the backup and allows users to specify source and destination paths interactively.

## Features
- Backup a folder into a ZIP file with compression.
- Restore files from a ZIP archive to a specified location.
- Command-line interface prompting users to select backup, restore, or exit.
- Validates paths and creates destination folders if needed.

## Usage
Run the script and follow the prompts:

1. Choose "backup" to compress a folder:
   - Enter the full path of the folder to back up.
   - Enter the full path where the backup ZIP should be saved.

2. Choose "restore" to extract files:
   - Enter the full path of the backup ZIP file.
   - Enter the full path where files should be restored.

3. Type "exit" to quit the program.

## Requirements
- Python 3.x
- Standard library modules: os, zipfile, shutil, sys

This project is released under the MIT License.

