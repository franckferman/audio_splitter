#!/usr/bin/env python3
# audio_splitter.py

"""
Audio Splitter Module

Description:
Provides a function to split audio files into multiple segments using ffmpeg-python.
Handles the core logic for segmenting audio into fixed-duration chunks efficiently.
Automatically extracts audio from video if necessary.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.1.0
"""

import os
import ffmpeg
import logging
from pathlib import Path
from utils.helpers import print_error, print_success, print_info


SUPPORTED_AUDIO_FORMATS = {".mp3", ".wav", ".m4a", ".flac"}


def is_audio_file(file_path: Path) -> bool:
    """
    Checks if the file is a supported audio format.

    Args:
        file_path (Path): Path to the input file.

    Returns:
        bool: True if it's a directly supported audio file.
    """
    return file_path.suffix.lower() in SUPPORTED_AUDIO_FORMATS


def extract_audio(input_file: str, temp_audio_file: str) -> None:
    """
    Extracts audio from video/unsupported formats as MP3.

    Args:
        input_file (str): Path to input video or unsupported file.
        temp_audio_file (str): Path to store the extracted MP3.
    """
    print_info(f"🎶 Extracting audio from '{input_file}' to '{temp_audio_file}'...")
    try:
        (
            ffmpeg
            .input(input_file)
            .output(temp_audio_file, acodec='libmp3lame', vn=None)  # Audio only, mp3
            .run(capture_stdout=True, capture_stderr=True)
        )
        print_success(f"✅ Audio extracted: {temp_audio_file}")
    except ffmpeg.Error as e:
        error_message = e.stderr.decode('utf8') if e.stderr else 'Unknown FFmpeg error during extraction.'
        print_error(f"❌ Audio extraction failed:\n{error_message}")
        raise RuntimeError("Audio extraction failed.") from e


def split_audio(input_file: str, output_folder: str, segment_duration: int, extension: str = ".mp3") -> None:
    """
    Splits a clean audio file into fixed-duration segments.

    Args:
        input_file (str): Path to the audio file.
        output_folder (str): Folder for output segments.
        segment_duration (int): Duration of each segment (seconds).
        extension (str): File extension for output segments (default: .mp3).
    """
    output_pattern = os.path.join(output_folder, f"segment_%03d{extension}")
    print_info(f"🔪 Splitting '{input_file}' into {segment_duration}s segments...")
    try:
        (
            ffmpeg
            .input(input_file)
            .output(
                output_pattern,
                f="segment",
                segment_time=segment_duration,
                c="copy",
                reset_timestamps=1
            )
            .run(capture_stdout=True, capture_stderr=True)
        )
        print_success(f"✅ Splitting complete. Segments saved in: {output_folder}")
        logging.info(f"Splitting complete. Segments saved in '{output_folder}'")
    except ffmpeg.Error as e:
        error_message = e.stderr.decode('utf8') if e.stderr else 'Unknown FFmpeg error during splitting.'
        print_error(f"❌ Splitting failed:\n{error_message}")
        raise RuntimeError("Splitting failed.") from e


def split_audio_with_ffmpeg(input_file: str, output_folder: str, segment_duration: int) -> None:
    """
    Main handler to split audio (with auto-extraction if needed).

    Args:
        input_file (str): Path to input file.
        output_folder (str): Path to output directory.
        segment_duration (int): Segment duration in seconds.
    """
    file_path = Path(input_file)
    temp_audio_file = None  # Track if we create a temp file

    try:
        if not is_audio_file(file_path):
            temp_audio_file = str(file_path.with_suffix(".extracted.mp3"))
            extract_audio(input_file, temp_audio_file)
            input_file = temp_audio_file  # Work on extracted audio

        split_audio(input_file, output_folder, segment_duration)

    finally:
        if temp_audio_file and Path(temp_audio_file).exists():
            Path(temp_audio_file).unlink()
            print_info(f"🧹 Temporary audio file deleted: {temp_audio_file}")

