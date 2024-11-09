#!/usr/bin/env python3
# helpers.py

"""
Helpers Module

Description:
Functions for consistent formatted console output (info, success, error messages) 
across `audio_splitter`.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.0
"""

from colored import fore, style

def print_error(message: str) -> None:
    """
    Prints an error message in red.

    Args:
        message (str): The message to display as an error.
    """
    print(f"{fore('red')}❌ {message}{style('reset')}")


def print_success(message: str) -> None:
    """
    Prints a success message in green.

    Args:
        message (str): The message to display as a success.
    """
    print(f"{fore('green')}✅ {message}{style('reset')}")


def print_info(message: str) -> None:
    """
    Prints an informational message in blue.

    Args:
        message (str): The message to display as informational.
    """
    print(f"{fore('blue')}ℹ️  {message}{style('reset')}")
