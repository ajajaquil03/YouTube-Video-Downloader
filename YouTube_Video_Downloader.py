import yt_dlp


yt_dlp.YoutubeDL({"format": "bestvideo[height<=2160]+bestaudio/best", "merge_output_format": "mp4", "outtmpl": "%(title)s.%(ext)s"}).download(["Input Your Video URL Here"])
