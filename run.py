import youtube_dl


def run():
    print("===================================================================")
    # Ask the user for the video they want to download
    video_url = input("Please enter the YouTube Video URL: ")
    #Ask the user for where they wanna download it
    SAVE_PATH = input("Please enter the download location: ") + "/"
    # Download and convert to mp3 and store in downloads folder
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': SAVE_PATH + filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download Finished")
    print("===================================================================")

if __name__ == '__main__':
    run()
