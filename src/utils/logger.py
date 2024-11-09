#!/usr/bin/env python3
# logger.py

"""
Logger Module

Description:
Sets up logging for the `audio_splitter` project with an option to enable debug logging.
Configures a log file with timestamps and message levels.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.0
"""

import logging
from datetime import datetime

def setup_logger(debug: bool = False):
    """
    Configures the logging settings. If debug is True, logging is enabled
    and saved with a timestamped filename.

    Args:
        debug (bool): If True, enable logging to a file.
    """
    if debug:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f'transcription_{timestamp}.log'
        logging.basicConfig(
            filename=log_filename, 
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info(f"Debug mode enabled. Logging to '{log_filename}'.")

def close_logger():
    """
    Closes the logger to release file handles.
    """
    logging.shutdown()
