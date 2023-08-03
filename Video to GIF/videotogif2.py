# pip install moviepy
#Creating a gif file using mp4 or any other video format video, from moviepy.io
from moviepy.editor import *

video = VideoFileClip("ab87b616.mp4")
# video.close()
video.write_gif("VeryDngrs.gif")