#!/usr/bin/env python3
# audio_splitter.py

"""
Audio Splitter Module

Description:
Contains functions to split audio files into segments using ffmpeg-python.
Handles the main logic for segmenting audio files.

Created By  : Franck FERMAN
Created Date: 09/11/2024
Version     : 1.0.0
"""

import os
import ffmpeg as ffmpeg_lib

def split_audio_with_ffmpeg(input_file: str, output_folder: str, segment_duration: int) -> None:
    """
    Splits an audio file into segments of specified duration using ffmpeg-python.

    Args:
        input_file (str): Path to the audio file to split.
        output_folder (str): Path to the folder where segments will be saved.
        segment_duration (int): Duration of each segment in seconds.
    """
    try:
        input_stream = ffmpeg_lib.input(input_file)
        output_pattern = os.path.join(output_folder, "segment_%03d.mp3")

        ffmpeg_lib.output(
            input_stream,
            output_pattern,
            f="segment",
            segment_time=segment_duration,
            c="copy"
        ).run(capture_stdout=True, capture_stderr=True)

        print(f"✅ Splitting complete. Segments saved in: {output_folder}")

    except ffmpeg_lib.Error as e:
        print(f"❌ Error during FFmpeg execution: {e.stderr.decode('utf8')}")
