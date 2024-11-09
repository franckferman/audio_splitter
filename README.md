# Audio Splitter

**Audio Splitter** is a tool for splitting audio files into fixed-length segments using FFmpeg. It is designed to be easy to use from the command line with customizable options.

## Features

- Splits audio files into fixed-duration segments.
- Uses `ffmpeg` for fast and precise splitting.
- Cleans up temporary files generated during execution (e.g., `.pyc` files, `__pycache__` folders, etc.).

## Installation

### With Poetry

```bash
poetry install
```

### With pip

For a standard installation with pip:

```bash
pip install -r requirements.txt
```

### Usage

#### Splitting audio files

```bash
poetry run audio-splitter split "path/to/audio_file.mp3" "path/to/output_folder" --duration 300
```

- **split**: Main command to split audio files.
- **input_file**: Path to the audio file to split.
- **output_folder**: Folder to save the split segments.
- **--duration**: Duration in seconds for each segment (optional, default: 600 seconds).

#### Cleaning temporary files

To clean temporary files in the specified directory:

```bash
poetry run audio-splitter clean --directory .
```

- **clean**: Removes temporary files (e.g., .pyc files, __pycache__ folders, etc.) in the specified directory (default is the current directory).

### Example Usage

```bash
# Split an audio file into 10-minute segments
poetry run audio-splitter split "./audio/example.mp3" "./output" --duration 600

# Clean temporary files in the current directory
poetry run audio-splitter clean --directory .
```

## Development

### Setting up the Environment

To contribute to the project, make sure to install the development dependencies:

```bash
poetry install --with dev
```

Linting & Formatting

The project uses black, flake8, and mypy to maintain code quality.

- **Formatting**: `black .`
- **Static analysis**: `flake8 .`
- **Type checking**: `mypy .`

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
