import tkinter as tk
import time
import argparse
import json
import customtkinter as ctk
from PIL import Image,ImageTk
from datetime import datetime, timedelta
from ChemTherm_library.tinkerforge_lib import *


def tk_loop():    
    #section = check_section(config,section)
    if running == 1:
        T_set = json_timing(config,section,t0)
        for i in lable_T_soll:
            lable_T_soll[i].delete(0, tk.END)
            lable_T_soll[i].insert(0,str(T_set[i]))
            
        for i in lable_T_ist:
            #lable_T_ist[i].config(text = str(tc_list[i].t)+"°C")
            lable_T_ist[i].config(text = str(T_set[0])+" °C")
            progressbar[i].set(T_set[0]/1100)

    window.after(500, tk_loop)


def Start_Button_callback():
    global section, running, t0
    running = 1
    section = 1
    t0 = time.time()
    Start_Button.configure(state = "disabled")

def Stop_Button_callback():
    global section, running, t0
    running = 0
    Start_Button.configure(state = "enabled")

'''' 
====================================
SETUP 
====================================
'''
t0 = time.time()
section = 0
running = 0
''''
====================================
ARGUMENT PARSER
====================================
'''
argparser = argparse.ArgumentParser(description='High temperature coupon reactor')

argparser.add_argument(
    '-e',
    '--experiment',
    help = 'Json File for experiment')

json_name = str(argparser.parse_args().experiment)
if json_name == "None":
    json_name="Experiment1"

'''
====================================
LOAD JSON FILE
====================================
'''
with open(json_name +'.json', 'r') as config_file:
    config = json.load(config_file)
'''
====================================
Setting
====================================
'''
with open('img/setting' + str(config['REACTOR']['amount'])  + '.json', 'r') as img_file:
    img = json.load(img_file)


#window = set_ICVT_landingpage(config)
#window = tk.Tk()
window = ctk.CTk()
ctk.set_appearance_mode("light")
scrW = window.winfo_screenwidth()
scrH = window.winfo_screenheight()
window.geometry(str(scrW) + "x" + str(scrH))
window.title(config['REACTOR']['Name'])
window.attributes('-fullscreen',True)

#----------- Images ----------- 
bg_image = ImageTk.PhotoImage(Image.open(img['Background']['name']).resize((int(img['Background']['width']*img['Background']['factor']),int(img['Background']['height']*img['Background']['factor'])),Image.LANCZOS))
close_img = ctk.CTkImage(Image.open(config['PATH']['images'] + 'close.png'),size=(80, 80))
bg_image = ctk.CTkImage(Image.open(img['Background']['name']),size=(int(img['Background']['width']), int(img['Background']['height'])))



#----------- Frames ----------
lf_MFC = ctk.CTkFrame(window, border_color=config['TKINTER']['background-color'], border_width=0, height=scrH, width=scrW)
name_Frame = ctk.CTkLabel(lf_MFC, font = ('Arial',16), text='MFC Steuerung')
name_Frame.grid(column=0, columnspan = 2, row=0, ipadx=5, ipady=5)
lf_MFC.place(x= 50,y= 800)

#----------- Labels -----------
#canvas_bg.pack_forget()
label_background = ctk.CTkLabel(window,image=bg_image,text="")
x_offset = img['Background']['x']
y_offset = img['Background']['y']
label_background.place(x = x_offset,y = y_offset)
label_background.lower()

#lf_MFC = ctk.CTkFrame(frame_MFC, text='MFC Steuerung', font = ('Arial',18))
#lf_MFC.grid(column=0, row=0, padx=5, pady=5)

lable_T_ist ={}
progressbar ={}
for i in range(0,8):
    lable_T_ist[i] = ctk.CTkLabel(window, font = ('Arial',16), text='0 °C')
    lable_T_ist[i].place(x = x_offset + img['T-Reaktor']['x'][i],y = y_offset + img['T-Reaktor']['y'][i])

    progressbar[i] = ctk.CTkProgressBar(master=window, width = 80, progress_color = 'red')
    progressbar[i] .place(x = x_offset + img['T-Reaktor']['x'][i]-8,y = y_offset + img['T-Reaktor']['y'][i]+30)

lable_T_soll ={}
for i in range(0,4):
    lable_T_soll[i] = tk.Entry(window, font = ('Arial',16), width = 6,bg='light blue' )
    lable_T_soll[i].place(x = x_offset + img['T-Set']['x'][i],y = y_offset + img['T-Set']['y'][i])

name_MFC={}; set_MFC={}; unit_MFC={}; value_MFC={}
for i in range(0,3):
    name_MFC[i]= ctk.CTkLabel(lf_MFC, font = ('Arial',16), text=config['MFC']['name'][i])
    name_MFC[i].grid(column=0, row=i+1, ipadx=5, ipady=5)
    set_MFC[i] = tk.Entry(lf_MFC, font = ('Arial',16), width = 6 )
    set_MFC[i].grid(column=1, row=i+1, ipadx=5, ipady=5)
    unit_MFC[i]= ctk.CTkLabel(lf_MFC, font = ('Arial',16), text=' mV')
    unit_MFC[i].grid(column=2, row=i+1, ipadx=5, ipady=5)
    value_MFC[i]= ctk.CTkLabel(lf_MFC, font = ('Arial',16), text='0 mV')
    value_MFC[i].grid(column=3, row=i+1, ipadx=5, ipady=5)

#----------- Buttons -----------
Start_Button = ctk.CTkButton(master=window, command=Start_Button_callback,text="Messung starten", font = ('Arial',16))
Start_Button.place(x=300, y=50)
Stop_Button = ctk.CTkButton(master=window, command=Stop_Button_callback,text="Messung stoppen", font = ('Arial',16))
Stop_Button.place(x=300, y=100)
Exit_Button = ctk.CTkButton(master=window,text="", command=window.destroy, fg_color= 'transparent',  hover_color='#F2F2F2', image= close_img)
Exit_Button.place(x=1700, y=50)

#----------- Entry Fields------
#fileName_Entry = ctk.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
#-----------Check Boxes------
checkbox_1 = ctk.CTkCheckBox(master=window,text = "Verdampfer nn")
checkbox_1.place(x=100, y=50)
checkbox_1 = ctk.CTkCheckBox(master=window,text = "Ventile offen")
checkbox_1.place(x=100, y=100)

window.after(1000, tk_loop())
window.mainloop()

print("bye bye")
