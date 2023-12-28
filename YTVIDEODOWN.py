from pytube import YouTube
from sys import argv

#LinkQuestion and Import Values
link = input("What Video would you like to download? \n")
yt = YouTube(link)

#Video Info
print("Title: ", yt.title)

print("View: ", yt.views)


#Youtube Download Code
yd = yt.streams.get_highest_resolution()

yd.download('D:\YT downloads')

#Final Message
print("All Done!")