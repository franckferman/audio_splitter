#!/usr/bin/env python3
# main.py

"""
Audio Splitter Application

Description:
CLI application for splitting audio files into segments of specified duration using FFmpeg
and cleaning up temporary files. This tool is part of the `audio_splitter` project.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.0
"""

import typer
from pathlib import Path
from splitter.audio_splitter import split_audio_with_ffmpeg
from splitter.file_manager import create_output_folder
from utils.cleaner import clean_project
from utils.helpers import print_info, print_success, print_error
from utils.logger import setup_logger, close_logger
from colored import fore, style
import logging

app = typer.Typer()

@app.command(help="Splits an audio file into segments of specified duration using FFmpeg.")
def split(
    input_file: Path = typer.Argument(..., help="Path to the audio file to split."),
    output_folder: Path = typer.Argument(..., help="Folder to save the split segments."),
    segment_duration: int = typer.Option(
        600, "-d", "--duration", help="Duration of each segment in seconds."
    ),
    debug: bool = typer.Option(False, "--debug", help="Enable debug logging.")
) -> None:
    """
    Splits an audio file into segments.

    This function checks the existence of the input file, creates the output folder
    if it does not exist, and calls the function to split the audio file using FFmpeg.

    Args:
        input_file (Path): Path to the audio file to split.
        output_folder (Path): Folder where the split segments will be saved.
        segment_duration (int): Duration of each segment in seconds. Default is 600 seconds.
        debug (bool): Enables debug logging if True.
    """
    setup_logger(debug=debug)

    if not input_file.is_file():
        print_error(
            f"{fore('red')}❌ The specified file does not exist: {input_file}{style('reset')}"
        )
        logging.error(f"File does not exist: {input_file}")
        raise typer.Exit(code=1)

    create_output_folder(output_folder)
    print_info(f"{fore('yellow')}⏳ Splitting the file...{style('reset')}")
    logging.info(f"Starting split on file {input_file} with segment duration {segment_duration}")

    split_audio_with_ffmpeg(str(input_file), str(output_folder), segment_duration)
    print_success(
        f"{fore('green')}✅ Splitting complete. Segments saved in: {output_folder}{style('reset')}"
    )
    logging.info("Splitting completed successfully.")
    close_logger()


@app.command(help="Cleans up temporary files (.pyc, __pycache__, etc.) in the project.")
def clean(
    directory: Path = typer.Argument(
        ".", help="Starting directory for cleaning up unwanted files."
    ),
    debug: bool = typer.Option(False, "--debug", help="Enable debug logging.")
) -> None:
    """
    Removes temporary and unwanted files from the project directory.

    This function recursively deletes files such as Python bytecode, cache directories,
    and other temporary files within the specified directory.

    Args:
        directory (Path): The root directory to start cleaning. Defaults to the current directory.
        debug (bool): Enables debug logging if True.
    """
    setup_logger(debug=debug)
    clean_project(directory)
    logging.info(f"Cleaned project directory: {directory}")
    close_logger()


if __name__ == "__main__":
    app()
