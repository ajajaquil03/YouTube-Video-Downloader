# 🎬 YouTube Video Downloader (using yt-dlp)

A lightweight and efficient Python script for downloading YouTube videos in high quality, specifically configured to fetch the best available video and audio streams and merge them into a single **MP4** file.

## ✨ Features

* **High Quality:** Downloads the best available video stream with a resolution of **up to 4K (2160p)**.
* **Merged Output:** Automatically combines the separate video and audio streams into a single file.
* **MP4 Format:** Output files are saved in the widely compatible `.mp4` container format.
* **Intelligent Naming:** Files are named using the video's original title (e.g., `Video Title.mp4`).

## 🛠️ Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need **Python 3.7+** installed on your system.

The script relies on the `yt-dlp` library and **FFmpeg**:
* **`yt-dlp`**: The video download library.
* **`FFmpeg`**: Required by `yt-dlp` to merge the separate video and audio streams into a single file. You must have the `ffmpeg` executable available in your system's PATH.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ajajaquil03/YouTube-Video-Downloader.git
    cd YouTube-Video-Downloader
    ```

2.  **Install the Python dependencies:**
    Use `pip` to install `yt-dlp`. It is recommended to install in a virtual environment.
    ```bash
    pip install yt-dlp
    ```

3.  **Install FFmpeg:**
    Download and install the **FFmpeg** program for your operating system and ensure the executable is accessible from your command line (i.e., in your system's PATH).

## 🚀 Usage

The core download logic is contained in the Python script (e.g., `download.py`).

1.  **Modify the Video URL:**
    Open the Python script and replace the placeholder URL with the actual URL of the YouTube video you wish to download:
    [`YouTube Video Downloader`](https://github.com/ajajaquil03/YouTube-Video-Downloader/tree/6049ecf1d27521e0c93e365dd7411059f95e68ae/CODE) file for the full source code.

2.  **Run the script:**
    Execute the Python script from your terminal:

    ```bash
    python download.py
    ```
    The video will be downloaded to the current directory with its title as the filename.

## ⚙️ Configuration Details

The options passed to the `yt_dlp.YoutubeDL` object are specifically chosen to ensure high-quality and compatibility:

* `"format": "bestvideo[height<=2160]+bestaudio/best"`:
    * `bestvideo[height<=2160]` selects the highest quality video stream up to 2160p (4K).
    * `+bestaudio` selects the highest quality separate audio stream.
    * `/best` is a fallback to download a combined best-quality format if separate streams are not available.
* `"merge_output_format": "mp4"`: Tells `yt-dlp` to use FFmpeg to merge the streams and save the final output as an MP4 file.
* `"outtmpl": "%(title)s.%(ext)s"`: Sets the output filename template to use the video's title.


## 👤 Author

* **Ajaj Mahmud Aquil** - **[Github](https://github.com/ajajaquil03)**
* **Ajaj Mahmud Aquil** - **[LinkedIn Profile](https://www.linkedin.com/in/ajajmahmudaquil/)**

## ⭐ Support

If you find this project helpful, please give it a ⭐ on GitHub!
