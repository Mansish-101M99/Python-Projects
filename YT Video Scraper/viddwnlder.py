# pip install pytube
from pytube import YouTube

link = input("Enter the url of YT video you want to download : ")
dwnld_video_link = YouTube(link)
tle = dwnld_video_link.title
print("Title of video : ", tle)

nvws = dwnld_video_link.views
print("Number of views for the video : ", nvws)

lng_vid = dwnld_video_link.length   # -->> It gives in terms of seconds
print("Length of video : ", lng_vid, " Seconds")

authr_vid = dwnld_video_link.author
print("Video publisher : ", authr_vid)

dwnld_video_link.streams.get_highest_resolution().download()
print("Video downloaded...")