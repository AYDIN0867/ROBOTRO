import yt_dlp

def Download(link):
    ydl_opts = {
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ").strip()
Download(link)
