import yt_dlp
import os

def download_audio_from_video(video_url, download_path='downloads'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def download_audio_from_playlist(playlist_url, download_path='downloads'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def main():
    url = input("Enter YouTube video or playlist URL: ")
    download_path = 'downloads'
    os.makedirs(download_path, exist_ok=True)

    if "playlist" in url:
        download_audio_from_playlist(url, download_path)
    else:
        download_audio_from_video(url, download_path)

if __name__ == "__main__":
    main()
