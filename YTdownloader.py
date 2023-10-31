# daniel gregorio
# 10.31.23
# YTdownloader app

import os

from pytube import YouTube

while True:
    toDownload = str(input("Enter the YouTube link\n➜ "))
    print("Would you like to download MP3 or MP4?")
    print("Enter [1] for MP3 (Audio Only)")
    print("Enter [2] for MP4 (Video + Audio)")
    userInput = int(input("➜ "))
    fromYT = YouTube(url=toDownload)
    if userInput == 1:
        audio = fromYT.streams.get_audio_only()
        outaudio = audio.download(output_path="YTD_Audios")
        base, ext = os.path.splitext(outaudio)
        new_file = base + ".mp3"
        os.rename(outaudio, new_file)
    if userInput == 2:
        video = fromYT.streams.get_highest_resolution()
        video.download(output_path='YTD_videos')
    end = str(input("Would you like to download again? (Y/n)"))
    if end in ['n','N']:
        break