#!/usr/bin/env python3
# helpers.py

"""
Helpers Module

Description:
Provides consistent and formatted console output functions for information,
success, and error messages across the `audio_splitter` project.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.0
"""

from colored import fore, style


def print_error(message: str) -> None:
    """
    Displays an error message in red with a ❌ symbol.

    Args:
        message (str): The error message to display.

    Returns:
        None
    """
    print(f"{fore('red')}❌ {message}{style('reset')}")


def print_success(message: str) -> None:
    """
    Displays a success message in green with a ✅ symbol.

    Args:
        message (str): The success message to display.

    Returns:
        None
    """
    print(f"{fore('green')}✅ {message}{style('reset')}")


def print_info(message: str) -> None:
    """
    Displays an informational message in blue with a ℹ️ symbol.

    Args:
        message (str): The informational message to display.

    Returns:
        None
    """
    print(f"{fore('blue')}ℹ️  {message}{style('reset')}")
