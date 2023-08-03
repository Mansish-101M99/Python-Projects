# pip install moviepy
import moviepy.editor as mpe

clip = mpe.VideoFileClip("ab87b616.mp4")
clip.audio.write_audiofile("Verydng.mp3")