# pip install pyshorteners
import pyshorteners

shortn = pyshorteners.Shortener()
long_url = input("Enter your long link : ")
sm_url = shortn.tinyurl.short(long_url)
print(sm_url)
