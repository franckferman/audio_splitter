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
from colored import fore, style

def create_output_folder(output_folder: str) -> None:
    """
    Creates the output folder if it does not already exist.

    Args:
        output_folder (str): Path to the output folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    print(f"{fore('blue')}📂 Output folder created: {output_folder}{style('reset')}")
