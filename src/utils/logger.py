#!/usr/bin/env python3
# logger.py

"""
Logger Module

Description:
Sets up and manages logging for the `audio_splitter` project, with support for debug and
info levels. Logs are saved with timestamped filenames for session tracking.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.0
"""

import logging
from datetime import datetime


def setup_logger(debug: bool = False) -> None:
    """
    Configures and initializes the logger for the current session.
    If debug mode is enabled, sets logging level to DEBUG; otherwise INFO.
    Logs are stored in a file named with the current timestamp.

    Args:
        debug (bool): If True, enables detailed debug logging; otherwise logs INFO-level events.

    Returns:
        None
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"transcription_{timestamp}.log"

    # Define log level based on debug flag
    log_level = logging.DEBUG if debug else logging.INFO

    # Setup logging configuration
    logging.basicConfig(
        filename=log_filename,
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Immediate log to mark start of session
    logging.info(f"Logger initialized. Debug mode: {'ON' if debug else 'OFF'}. Log file: {log_filename}")


def close_logger() -> None:
    """
    Properly shuts down the logger and closes all associated file handlers to ensure data is written.

    Returns:
        None
    """
    logging.shutdown()
