import tkinter as tk
import time
import argparse
import json
import customtkinter
from PIL import Image,ImageTk
from datetime import datetime
from source.icvt.tinkerforge_lib import *

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

#window = set_ICVT_landingpage(config)
window = tk.Tk()
scrW = window.winfo_screenwidth()
scrH = window.winfo_screenheight()
window.geometry(str(scrW) + "x" + str(scrH))
window.title(config['REACTOR']['Name'])
window.attributes('-fullscreen',True)

#----------- Images ----------- 
bg_image = ImageTk.PhotoImage(Image.open(config['PATH']['images'] + 'reactor_background.png').resize((scrW,scrH),Image.LANCZOS))
close_img = ImageTk.PhotoImage(Image.open(config['PATH']['images'] + 'close.png').resize((50,50),Image.LANCZOS))

#----------- Frames ----------

frame_MFC = tk.Frame(window, bg=config['TKINTER']['background-color'], bd=0, height=scrH, width=scrW)


#----------- Labels -----------
#frame_bg = tk.Label(master=window,image=bg_image)


#canvas_bg.pack_forget()
label_background = tk.Label(window,image=bg_image)
label_background.place(x=0,y=0)
label_background.lower()

frame_MFC.place(x= 50,y= 100)
lf_MFC = tk.LabelFrame(frame_MFC, text='MFC Steuerung')
lf_MFC.grid(column=0, row=0, padx=5, pady=5)
Lable_MFC_N2= tk.Label(lf_MFC, text='MFC_N2 ')
Lable_MFC_N2.grid(column=0, row=0, ipadx=5, ipady=5)
set_MFC_N2 = tk.Entry(lf_MFC, width= 20)
set_MFC_N2.grid(column=1, row=0, ipadx=5, ipady=5)
unit_MFC_N2= tk.Label(lf_MFC, text=' mV')
unit_MFC_N2.grid(column=2, row=0, ipadx=5, ipady=5)
value_MFC_N2= tk.Label(lf_MFC, text='NaN mV')
value_MFC_N2.grid(column=3, row=0, ipadx=5, ipady=5)

lable_dict= tk.Label(window, text='T1')
lable_dict.place(x=30,y=200)



window.mainloop()

print("bye bye")
