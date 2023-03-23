import tkinter as tk
import time
import argparse
import json
import customtkinter as ctk
from PIL import Image,ImageTk
from datetime import datetime
from ChemTherm_library.tinkerforge_lib import *

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



app = ctk.CTk()
scrW=app.winfo_screenheight()
scrH = app.winfo_screenheight()
app.geometry(str(scrW) + "x" + str(scrH))
app.title("CustomTkinter simple_example.py")

def button_callback():
    print("Button click", combobox_1.get())


def slider_callback(value):
    progressbar_1.set(value)


frame_1 = ctk.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = ctk.CTkLabel(master=frame_1, justify=ctk.LEFT)
label_1.pack(pady=10, padx=10)

progressbar_1 = ctk.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)

button_1 = ctk.CTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=10, padx=10)

slider_1 = ctk.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=10, padx=10)
slider_1.set(0.5)

entry_1 = ctk.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
entry_1.pack(pady=10, padx=10)

optionmenu_1 = ctk.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = ctk.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("CTkComboBox")

checkbox_1 = ctk.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=10, padx=10)

radiobutton_var = ctk.IntVar(value=1)

radiobutton_1 = ctk.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=10, padx=10)

radiobutton_2 = ctk.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=10, padx=10)

switch_1 = ctk.CTkSwitch(master=frame_1)
switch_1.pack(pady=10, padx=10)

text_1 = ctk.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")

segmented_button_1 = ctk.CTkSegmentedButton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
segmented_button_1.pack(pady=10, padx=10)

tabview_1 = ctk.CTkTabview(master=frame_1, width=200, height=70)
tabview_1.pack(pady=10, padx=10)
tabview_1.add("CTkTabview")
tabview_1.add("Tab 2")

app.mainloop()

""" #window = set_ICVT_landingpage(config)
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



window.mainloop() """

print("bye bye")
