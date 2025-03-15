#!/usr/bin/env python3
# file_manager.py

"""
File Manager Module

Description:
Provides helper functions for managing file and directory structures, such as creating
output folders for audio segments in `audio_splitter`.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.0
"""

import os
import logging
from utils.helpers import print_info, print_error
from colored import fore, style


def create_output_folder(output_folder: str) -> None:
    """
    Creates the output folder if it does not already exist.

    Args:
        output_folder (str): Path to the output folder.

    Raises:
        OSError: If the folder cannot be created due to permission or other OS-related issues.
    """
    try:
        os.makedirs(output_folder, exist_ok=True)
        print_info(f"{fore('blue')}📂 Output folder ready: {output_folder}{style('reset')}")
        logging.info(f"Output folder created or already exists: {output_folder}")
    except OSError as e:
        print_error(f"{fore('red')}❌ Failed to create output folder: {output_folder}\nReason: {e}{style('reset')}")
        logging.error(f"Failed to create output folder '{output_folder}': {e}")
        raise
