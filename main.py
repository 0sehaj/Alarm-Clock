#Alarm Clock
#author: Sehaj

#import all the modules  needed
from tkinter import *
import datetime
import time
from pygame import mixer
from PIL import Image, ImageTk

#define the specifications of the window
window = Tk()
window.title("ALARM CLOCK")
window.geometry("500x290")

#specify and set the background image
img = Image.open('f.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(window, image=bg)
label.place(x=0,y=0)

#defining a funtion to collect and compare the the actual time to the alarm time and ringing the alarm when the times match 
def alarm(setalarm):
    while True:
      time.sleep(1)
      """
      currentTime = datetime.now()
      picTime = currentTime.strftime("%Y.%m.%d-%H%M%S")
      picTime
      msg= "Date and time: " + str(picTime)
      print(msg)
      """
      current_time = datetime.datetime.now().strftime("%H:%M:%S")
      current_date = datetime.datetime.now().strftime("%d/%m/%Y")
      msg = "Current Time: "+ str(current_time) + " Current Date: " + str(current_date)
      print(msg)
      
#command to play music when the time matches/ring the alarm
      if current_time == setalarm:
        mixer.init()
        mixer.music.load("sound0.mp3")
        mixer.music.set_volume(3.0)
        mixer.music.play()
        break

#define a function to collect and store the time information in a specific pattern and order
def get_time():
  set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"
  alarm(set_alarm)

#specify the time variables to StringVar class so that it can be changed/updated whenever needed
hour = StringVar(window)
minute = StringVar(window)
second = StringVar(window)

#make the labels for hours, minutes and seconds over the text boxes to signinfy what has to be typed inside 
hlabel = Label(window, text=" Hour ", font=("MS Serif", 16), fg="slateblue", bg="lavender").place(x=250,y=40)

mlabel = Label(window, text=" Min   ", font=("MS Serif", 16), fg="slateblue", bg="lavender").place(x=330, y=40)

slabel = Label(window,  text=" Sec   ", font=("MS Serif", 16), fg="slateblue", bg="lavender").place(x=410, y=40)

#labels for notes 
settimelabel = Label(window,text="SET ALARM TIME:",font=("MS Serif", 18),fg="slateblue",bg="lavender").place(x=0, y=80)

notelabel = Label(window, text="Set your time in the 24 hour format :) ", font=("MS Serif", 14, "italic"),fg="slateblue", bg="lightblue1").place(x=70, y=230)

#make seperate text boxes for hours, mins and secs for user to enter the time to be set for alarm
htext = Entry(window, textvariable=hour, bg="lightblue1", width=7,font=(50)).place(x=250, y=85)

mtext = Entry(window, textvariable=minute, bg="lightblue1", width=7, font=(50)).place(x=330, y=85)

stext = Entry(window, textvariable=second, bg="lightblue1", width=7, font=(50)).place(x=410, y=85)

#create a submit button to confirm the setting of alarm
button = Button(window, text="SET!", fg="slateblue", font=("MS Serif",16), borderwidth=6, width=10, command = get_time, bg="lavender").place(x=160, y=150)

#initiate the main loop to start the program
window.mainloop()

#sources used for help:
#https://pythonprogramming.net/adding-sounds-music-pygame/
#https://pythonprogramming.net/adding-sounds-music-pygame/
#https://stackoverflow.com/questions/44977163/python3-tkinter-set-image-size
