from threading import Thread
from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer

from datetime import datetime, time
from time import sleep

#colors
bg_color = '#ffffff'
co1 = "#566FC6" #blue
co2 = "#000000" #black

#window
window = Tk()
window.title("Alarm")
window.geometry('350x150')
window.configure(bg=bg_color)
window.iconbitmap('icon.ico')

#frame up
frame_line = Frame(window, width=400, height=5, bg=co1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=bg_color)
frame_body.grid(row=1, column=0)

#configuring frame body
img = Image.open(r'C:\Users\1zhal\Desktop\all\STUDY\Python\fpv3\iconn.png')
img.resize((128, 128))
img = ImageTk.PhotoImage(img)
app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text = "Alarm", height=1, font=('Ivy 18 bold'), bg=bg_color)
name.place(x=125, y=10)

hour = Label(frame_body, text = "hour", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
hour.place(x=127, y=40)
c_hour = Combobox(frame_body, width=2, font=('arial 15'))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24")
c_hour.current(0)
c_hour.place(x=130, y=58)

min = Label(frame_body, text = "min", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
min.place(x=177, y=40)
c_min = Combobox(frame_body, width=2, font=('arial 15'))
c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_min.current(0)
c_min.place(x=180, y=58)

sec = Label(frame_body, text = "sec", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
sec.place(x=227, y=40)
c_sec = Combobox(frame_body, width=2, font=('arial 15'))
c_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_sec.current(0)
c_sec.place(x=230, y=58)


def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('Deactivated alarm: ', selected.get())
    mixer.music.stop()

selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value = 1, text = "Turn On", bg=bg_color, command=activate_alarm, variable=selected)
rad1.place(x = 125, y=95)

def sound_alarm():
    mixer.music.load('sound.mp3')
    mixer.music.play()
    selected.set(0)

    rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value = 2, text = "Turn off", bg=bg_color, command=deactivate_alarm, variable=selected)
    rad2.place(x = 200, y=95)

def alarm():
    while True:
        time_now =datetime.now().strftime('%H:%M:%S') #Current Time
        print(time_now)
        control = selected.get()
        alarm_hour=c_hour.get()
        alarm_minute = c_min.get()
        alarm_sec = c_sec.get()

        now = datetime.now()

        hour = now.strftime("%H")
        minute = now.strftime("%M")
        second = now.strftime("%S")

        if control == 1:
            if alarm_hour == hour:
                if alarm_minute == minute:
                    if alarm_sec == second:
                        print("Time to wake up!")
                        sound_alarm()
        sleep(1)

mixer.init()


window.mainloop() #Execution