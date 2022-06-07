import shelve
from os import path
import tkinter as tk
from tkinter import *
import os
from tokenize import PseudoExtras
from PIL import Image, ImageTk
from tkinter import messagebox

custom = path.join(path.dirname(__file__), "admin","custom")

try:
    score_file = shelve.open(custom)   
    avg_light_vehicle_time= score_file['avg_light_vehicle_time']         
    avg_heavy_vehicle_time= score_file['avg_heavy_vehicle_time']         
    no_of_lanes= score_file['no_of_lanes']
    inital_default_time=score_file['inital_default_time']
    max_green_time=score_file['max_green_time']
    mini_green_time=score_file['mini_green_time']
    pedes=score_file['pedes']


except:
    score_file = shelve.open(custom)   
    score_file['avg_light_vehicle_time']=5
    score_file['avg_heavy_vehicle_time']=10
    score_file['no_of_lanes']=2
    score_file['inital_default_time']=5
    score_file['max_green_time']=150
    score_file['mini_green_time']=20
    score_file['pedes']=1
    score_file.close()
    avg_light_vehicle_time=5
    avg_heavy_vehicle_time=10
    no_of_lanes=2
    inital_default_time=5
    max_green_time=150
    mini_green_time=20
    pedes=1



app = tk.Tk()
app.title('Dashboard')
app.geometry('800x600')
app.configure(bg="white")

vg_light_vehicle_time=IntVar()
vg_heavy_vehicle_time=IntVar()
o_of_lanes=IntVar()
nital_default_time=IntVar()
ax_green_time=IntVar()
ini_green_time=IntVar()
edes=IntVar()


vg_light_vehicle_time.set(avg_light_vehicle_time)
vg_heavy_vehicle_time.set(avg_heavy_vehicle_time)
o_of_lanes.set(no_of_lanes)
nital_default_time.set(inital_default_time)
ax_green_time.set(max_green_time)
ini_green_time.set(mini_green_time)
edes.set(pedes)

class A():
  def reset(self):
    vg_light_vehicle_time.set(avg_light_vehicle_time)
    vg_heavy_vehicle_time.set(avg_heavy_vehicle_time)
    o_of_lanes.set(no_of_lanes)
    nital_default_time.set(inital_default_time)
    ax_green_time.set(max_green_time)
    ini_green_time.set(mini_green_time)
    edes.set(pedes)
    messagebox.showinfo("Reset", "Data Not Saved")

  def save(self):
    global avg_light_vehicle_time
    global avg_heavy_vehicle_time
    global no_of_lanes
    global inital_default_time
    global max_green_time
    global mini_green_time
    global pedes

    avg_light_vehicle_time=vg_light_vehicle_time.get()
    avg_heavy_vehicle_time=vg_heavy_vehicle_time.get()
    no_of_lanes=o_of_lanes.get()
    inital_default_time=nital_default_time.get()
    max_green_time=ax_green_time.get()
    mini_green_time=ini_green_time.get()
    pedes=edes.get()

    score_file = shelve.open(custom)   
    score_file['avg_light_vehicle_time']=vg_light_vehicle_time.get()
    score_file['avg_heavy_vehicle_time']=vg_heavy_vehicle_time.get()
    score_file['no_of_lanes']=o_of_lanes.get()
    score_file['inital_default_time']=nital_default_time.get()
    score_file['max_green_time']=ax_green_time.get()
    score_file['mini_green_time']=ini_green_time.get()
    score_file['pedes']=edes.get()

    score_file.close()
    messagebox.showinfo("Success", "Changes Saved")

    
q=A()
qwe=Image.open(path.join(path.dirname(__file__), "admin","back.png"))
imag = ImageTk.PhotoImage(qwe)
lab=Label(app, image=imag)
lab.place(relx=0,rely=0)

app.resizable(False, False)

ent1 = Entry(app, textvariable=vg_light_vehicle_time, width=5,
             font=('Ubuntu', 24), relief=GROOVE)
ent1.place(relx=0.7, rely=0.165, anchor=CENTER)

ent2 = Entry(app, textvariable=vg_heavy_vehicle_time, width=5,
             font=('Ubuntu', 24), relief=GROOVE)
ent2.place(relx=0.7, rely=0.265, anchor=CENTER)

ent3 = Entry(app, textvariable=o_of_lanes, width=5,
             font=('Ubuntu', 24), relief=GROOVE)
ent3.place(relx=0.7, rely=0.365, anchor=CENTER)

ent4 = Entry(app, textvariable=nital_default_time, width=5,
             font=('Ubuntu', 24), relief=GROOVE)
ent4.place(relx=0.7, rely=0.465, anchor=CENTER)

ent5 = Entry(app, textvariable=ax_green_time, width=5,
             font=('Ubuntu', 24), relief=GROOVE)
ent5.place(relx=0.7, rely=0.565, anchor=CENTER)

ent6 = Entry(app, textvariable=ini_green_time, width=5,
             font=('Ubuntu', 24), relief=GROOVE)
ent6.place(relx=0.7, rely=0.665, anchor=CENTER)

ent7 = Entry(app, textvariable=edes, width=5,
             font=('Ubuntu', 24), relief=GROOVE)
ent7.place(relx=0.7, rely=0.765, anchor=CENTER)


msg0 = Label(app, text=' ADMIN PANEL ', font=("Courier", 20), relief=GROOVE)
msg0.place(relx=0.5, rely=0.07, anchor=CENTER)


msg1 = Label(app, text=' Light Vehicle Time   ', font=("Courier", 18), relief=GROOVE)
msg1.place(relx=0.3, rely=0.165, anchor=CENTER)

msg2 = Label(app, text=' Heavy Vehicle Time   ', font=("Courier", 18), relief=GROOVE)
msg2.place(relx=0.3, rely=0.265, anchor=CENTER)

msg3 = Label(app, text=' No of Lanes          ', font=("Courier", 18), relief=GROOVE)
msg3.place(relx=0.3, rely=0.365, anchor=CENTER)

msg4 = Label(app, text=' Default Yellow Time  ', font=("Courier", 18), relief=GROOVE)
msg4.place(relx=0.3, rely=0.465, anchor=CENTER)

msg5 = Label(app, text=' Max Green Time       ', font=("Courier", 18), relief=GROOVE)
msg5.place(relx=0.3, rely=0.565, anchor=CENTER)

msg6 = Label(app, text=' Mini Green Time      ', font=("Courier", 18), relief=GROOVE)
msg6.place(relx=0.3, rely=0.665, anchor=CENTER)

msg6 = Label(app, text=' Pedestrain Detection ', font=("Courier", 18), relief=GROOVE)
msg6.place(relx=0.3, rely=0.765, anchor=CENTER)


user_input_reset = Button(app,text=' Reset', font=("Courier", 18), width=15, height=1,command=q.reset, relief=GROOVE)
user_input_reset.place(relx=0.3, rely=0.875, anchor=CENTER)

user_input_save = Button(app,text=' Save', font=("Courier", 18), width=15, height=1,command=q.save, relief=GROOVE)
user_input_save.place(relx=0.7, rely=0.875, anchor=CENTER)




stop = tk.Button(app, text='close', width=200, command=app.destroy,
                 bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.5, rely=1, anchor=S)

app.mainloop()


