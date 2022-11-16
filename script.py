from tkinter import *
from turtle import heading
from pytube import YouTube as yt
app=Tk()

# url='https://www.youtube.com/watch?v=ff-FSobShpo&list=RDMM&index=3'
# my_video=yt(url)
# print(my_video.title)
# print(my_video.thumbnail_url)
# for stream in my_video.streams:
#     print(stream)
# my_video = my_video.streams.get_highest_resolution()
# my_video.download() 
app.geometry('800x400')
favicon=PhotoImage(file="C:\programmationcourses\python\Tkinter\youtubevideo\images\icon.png")
app.iconphoto(False,favicon)
app.title('Youtube MP4 DOWNLOADER')

Heading=Label(app,text="Enter The Video Link here ⬇",font=("Poppins",30),fg='red')
Heading.pack()
text=StringVar()
text.set('Enter the video Url')
url = Entry(app,width=100,textvariable=text,font=("Poppins",15))
url.pack(pady=10)
def mainfun():
    urltext=url.get()
    my_video=yt(urltext)
    for stream in my_video.streams:  
      print(stream)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download(output_path="C:\programmationcourses\python\Tkinter\youtubevideo\\videos")
    text1=Label(app,text="Vous avez Telechargé "+"//"+str(my_video.title)+"//")
    text1.pack()
btn=Button(app,text="Download the video",fg="white",bg="red",pady=10,font=("Poppins",12),command=mainfun)
btn.pack(pady=20)





app.mainloop()
