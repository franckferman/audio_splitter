#!/usr/bin/env python3
# cleaner.py

"""
Cleaner Module

Description:
Utility functions for recursively cleaning temporary and unwanted files within the specified
directory. Provides a confirmation prompt to ensure safe directory cleanup.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.0
"""

import os
import logging
from pathlib import Path
from utils.helpers import print_info, print_success, print_error


def confirm_directory(directory: Path) -> bool:
    """
    Prompts the user to confirm cleanup in the specified directory.

    Args:
        directory (Path): The directory to clean.

    Returns:
        bool: True if the user confirms, False otherwise.
    """
    print_info(f"⚠️ Warning: You are about to clean the directory '{directory}'.")
    confirm = input("Do you want to proceed with cleanup in this directory? (y/n): ").strip().lower()
    return confirm == "y"


def clean_project(
    directory: Path = Path("."),
    log_file: Path = Path("transcription.log"),
    enable_logging: bool = False
) -> None:
    """
    Recursively deletes unwanted files and directories in the specified directory,
    and removes the log file if it exists. Optionally logs cleanup actions.

    Args:
        directory (Path): The root directory to start cleaning. Defaults to the current directory.
        log_file (Path): Path to the log file to delete. Defaults to "transcription.log".
        enable_logging (bool): If True, logs actions to 'cleanup.log'.
    """
    # Confirm directory
    if not confirm_directory(directory):
        print_error("🚫 Cleanup cancelled.")
        return

    if enable_logging:
        logging.basicConfig(filename="cleanup.log", level=logging.INFO, format="%(asctime)s - %(message)s")
        logging.info(f"Starting cleanup in: {directory}")

    patterns_to_delete = [
        "*.pyc", "*.pyo", "*.pyd",
        "__pycache__",
        "*.log",
        "*.tmp", "*.bak", "*.swp",
        ".DS_Store", "Thumbs.db"
    ]

    print_info(f"🚮 Cleaning up directory: {directory}")

    for pattern in patterns_to_delete:
        for item in directory.rglob(pattern):
            try:
                if item.is_file():
                    item.unlink()
                    print_info(f"🗑️  Deleted file: {item}")
                    if enable_logging:
                        logging.info(f"Deleted file: {item}")
                elif item.is_dir():
                    # Check if empty before deleting
                    if not any(item.iterdir()):
                        item.rmdir()
                        print_info(f"📂 Deleted empty directory: {item}")
                        if enable_logging:
                            logging.info(f"Deleted empty directory: {item}")
            except Exception as e:
                error_msg = f"❌ Error deleting {item}: {e}"
                print_error(error_msg)
                if enable_logging:
                    logging.error(error_msg)

    # Remove log file if present
    if log_file.exists():
        try:
            log_file.unlink()
            print_info(f"🗑️  Deleted log file: {log_file}")
            if enable_logging:
                logging.info(f"Deleted log file: {log_file}")
        except Exception as e:
            error_msg = f"❌ Error deleting log file {log_file}: {e}"
            print_error(error_msg)
            if enable_logging:
                logging.error(error_msg)

    print_success("✅ Cleanup completed.")
    if enable_logging:
        logging.info("Cleanup completed.")
