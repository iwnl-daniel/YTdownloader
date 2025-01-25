# YTdownloader

Daniel Gregorio-Torres

10/31/23

Personal Project

## Description

The purpose of this Python application is for the user to be able to download YouTube videos and save them locally to their computer as either `.MP3` or `.MP4` files. The application uses the following libraries: os, tkinter, customtkinter, packaging, and pytube to generate a little application window with a user-friendly interface. Within the UI, there is a text box that prompts the user to enter a valid YouTube link. Below that there are 2 buttons asking if the user would like to save the YouTube link as `.MP3` or `.MP4`. Once the user decides and clicks a button it will attempt to download the video from the provided link. When it is done downloading the video, in the same directory as the application, It will create a file named either `YTD_Audios` or `YTD_videos`. If the video/ link is invalid it will display `Downloading Error` otherwise when it finishes downloading it will display `<title of video> Downloaded`

## Navigation

- [Running Code](#running-code)
- [Running App](#running-app)
- [Documentation Used](#documentation-used)

## Running Code

###### Unix(macOS):

```shell
python3 -m venv env
source env/bin/activate
pip3 install --upgrade -r requirements.txt
python3 app.py
```

###### Lunix(Ubuntu):
```shell
sudo apt update
sudo apt install python3-venv python3-pip
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

###### Windows:

```shell
py -m venv env
.\env\Scripts\activate
pip install --upgrade -r requirements.txt
python3 app.py
```

## Running App

|                                                                                                           macOS                                                                                                            |                                                                                                          Windows                                                                                                           |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                       download [latest release](https://github.com/iwnl-daniel/YTdownloader/releases)<br>![](/imgs/download_mac.png)                                                       |                                                       download [latest release](https://github.com/iwnl-daniel/YTdownloader/releases)<br>![](/imgs/download_win.png)                                                       |
|                                                                       unzip file, open application, and click 'cancel'<br>![](/imgs/pcrisk_mac.png)                                                                        |                                                                      unzip file, open application, and click 'more info'<br>![](/imgs/pcrisk_win.png)                                                                      |
|                                                               right click application, click 'open', and click 'open' again<br>![](/imgs/run_anyway_mac.png)                                                               |                                                                                    click 'run anyway'<br>![](/imgs/run_anyway_win.png)                                                                                     |
|                                                                     close the app and place .app file anywhere you want except the 'downloads' folder                                                                      |                                                             app should be ready to go. place .exe file anywhere you want if an error occurs, close and reopen.                                                             |
|                                                                                    UI should look like this<br>![](/imgs/appUI_mac.png)                                                                                    |                                                                                    UI should look like this<br>![](/imgs/appUI_win.png)                                                                                    |
|                                                     insert YouTube video link into the text box and click `MP3`(audio) or `MP4`(video)<br>![](/imgs/enterlink_mac.png)                                                     |                                                     insert YouTube video link into the text box and click `MP3`(audio) or `MP4`(video)<br>![](/imgs/enterlink_win.png)                                                     |
|                                      once the video has been downloaded it will display a downloaded message stating `<video title> downloaded`<br>![](/imgs/vid_downloaded_mac.png)                                       |                                      once the video has been downloaded it will display a downloaded message stating `<video title> downloaded`<br>![](/imgs/vid_downloaded_win.png)                                       |
| once the video has been downloaded, in the same directory, a new folder (unless it already exists) will be created to store the file. `YTD_Audios` for `MP3` and `YTD_videos` for `MP4`<br>![](/imgs/createdfiles_mac.png) | once the video has been downloaded, in the same directory, a new folder (unless it already exists) will be created to store the file. `YTD_Audios` for `MP3` and `YTD_videos` for `MP4`<br>![](/imgs/createdfiles_win.png) |
|                                              if the link is invalid or the video can't be downloaded it will display a downloading error<br>![](/imgs/download_error_mac.png)                                              |                                              if the link is invalid or the video can't be downloaded it will display a downloading error<br>![](/imgs/download_error_win.png)                                              |

# Documentation Used

1. [pytube](https://pytube.io/en/latest/api.html#pytube.YouTube.title)

1. [customtkinter](https://customtkinter.tomschimansky.com/documentation/)

1. [py2app.01](https://py2app.readthedocs.io/en/latest/)

1. [py2app.01](https://py2app.readthedocs.io/_/downloads/en/stable/pdf/)

1. [py2app.01](https://www.marinamele.com/from-a-python-script-to-a-portable-mac-application-with-py2app)

1. [pyinstaller](https://pyinstaller.org/en/stable/)
