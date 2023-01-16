import tkinter as tk
import time
import argparse
import json
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

#----------- Canvas ----------- 
canvas_bg = tk.Canvas(window, bg = config['TKINTER']['background-color'], width = scrW, height = scrH)


bg = canvas_bg.create_image(0,0, image = bg_image, anchor = tk.NW)
close_button_canvas = canvas_bg.create_image(scrW - 60, 10 , image = close_img, anchor = tk.NW)
canvas_bg.tag_bind(close_button_canvas, "<Button-1>", close_window) 

lf_MFC = tk.LabelFrame(window, text='MFC Steuerung')
lf_MFC.grid(column=0, row=0, padx=5, pady=5)
Lable_MFC_N2= tk.Label(lf_MFC, text='MFC_N2 ')
#canvas_bg.pack()

window.mainloop()

print("bye bye")

