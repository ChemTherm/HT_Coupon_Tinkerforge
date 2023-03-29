import tkinter as tk
import time
import argparse
import json
import customtkinter as ctk
from PIL import Image,ImageTk
from datetime import datetime, timedelta
from ChemTherm_library.tinkerforge_lib import *
from ChemTherm_library.Coupon_lib import *



def tk_loop():


    if running_Json == 1:
        T_set, MFC_set = json_timing(config,section,t0)
        for i in set_T:
            set_T[i].delete(0, tk.END)
            set_T[i].insert(0,str(T_set[i]))
            #set_T[i].set(str(T_set[i]))
        for i in set_MFC:
            set_MFC[i].delete(0, tk.END)
            set_MFC[i].insert(0,str(MFC_set[i]))
    
    if running_setFunction == 1:     
        T_set, MFC_set,t_end = set_function(t0)    
        for i in set_T:
            set_T[i].delete(0, tk.END)
            set_T[i].insert(0,str(T_set[i]))
            #set_T[i].set(str(T_set[i]))
        for i in set_MFC:
            set_MFC[i].delete(0, tk.END)
            set_MFC[i].insert(0,str(MFC_set[i]))                


            
    #for i in lable_T_ist:
    for tc_obj_name in tc_list:
        lable_T_ist[tc_obj_name].configure(text = str(tc_list[tc_obj_name].t)+" °C")
    for p_obj_name in patronen_list:   
        progressbar[p_obj_name].set(patronen_list[p_obj_name].pwroutput/100)
    
    MFC_N2.get()
    MFC_Air.get()
    MFC_Ethan.get()
    value_MFC[0].configure(text = str(MFC_N2.Voltage) + " mV") 
    value_MFC[1].configure(text = str(MFC_Air.Voltage) + " mV") 
    value_MFC[2].configure(text = str(MFC_Ethan.Voltage) + " mV") 
    pressure1.get()
    pressure2.get()
    #pressure3.get()
    value_pressure1.config(text = str(pressure1.Voltage) + " mV") 
    value_pressure2.config(text = str(pressure2.Voltage) + " mV") 
    #value_pressure3.config(text = str(pressure3.Voltage) + " mV")


    with open(filename, 'a') as f:
        line = ' ' + datetime.now().strftime("%H:%M:%S:\t")
        for tc_obj_name in tc_list:
            line += str(tc_list[tc_obj_name].t) + '\t'
        for p_obj_name in patronen_list:
            line += str(patronen_list[p_obj_name].pwroutput) + '\t'
        line += str(set_MFC[0].get()) + ' \t '+ str(MFC_N2.Voltage) + ' \t '
        line += str(set_MFC[1].get()) + ' \t '+ str(MFC_Air.Voltage) + ' \t '
        line += str(set_MFC[2].get()) + ' \t '+ str(MFC_Ethan.Voltage) + ' \t '
        line += str(pressure1.Voltage) + ' \t '
        #line += ' /n'
        f.writelines(line)

    patrone_1.regeln()
    patrone_2.regeln()
    patrone_3.regeln()
    patrone_4.regeln()
    patrone_5.regeln()
    patrone_6.regeln()
    patrone_7.regeln()
    patrone_8.regeln()

    window.after(500, tk_loop)

def getdata():    

    if set_T[0].get() != '':
        patrone_1.set_t_soll(float(set_T[0].get()))
    if set_T[1].get() != '':
        patrone_2.set_t_soll(float(set_T[1].get()))
    if set_T[2].get() != '':
        patrone_3.set_t_soll(float(set_T[2].get()))
    if set_T[3].get() != '':
        patrone_4.set_t_soll(float(set_T[3].get()))
    if set_T[4].get() != '':
        patrone_5.set_t_soll(float(set_T[4].get()))
    if set_T[5].get() != '':
        patrone_6.set_t_soll(float(set_T[5].get()))
    if set_T[6].get() != '':
        patrone_7.set_t_soll(float(set_T[6].get()))
    if set_T[7].get() != '':
        patrone_8.set_t_soll(float(set_T[7].get()))


    MFC_N2.set(int(set_MFC[0].get()))
    MFC_Air.set(int(set_MFC[1].get()))
    MFC_Ethan.set(int(set_MFC[2].get()))

def Start_Button_callback():
    global section, running_json, t0
    running_json = 1
    section = 1
    t0 = time.time()
    Start_Button.configure(state = "disabled")

def Stop_Button_callback():
    global section, running_json, t0
    running_json = 0
    Start_Button.configure(state = "enabled")

def Heating_Button_callback():
    global t0, set_function, running_setFunction
    t0 = time.time()
    running_setFunction = 1
    set_function = heating
    Start_Button.configure(state = "disabled")
    Heating_Button.configure(state = "disabled")

'''' 
====================================
SETUP 
====================================
'''
t0 = time.time()
section = 0
running_Json = 0
running_setFunction = 0

#filename = "20230324_Coking_lowResidence_28_23.dat"
filename = "Test.dat"

with open(filename, 'a') as f:
    headline = "time \t t1 \t t2 \t t3 \t t4 \t t5 \t t6 \t t7 \t t8  \t p1 \t p2 \t p3 \t p4 \t p5 \t p6 \t p7 \t p8  \t MFC_N2_soll \t MFC_N2_ist \t MFC_Air_soll \t MFC_Air_ist \t MFC_Ethan_soll \t MFC_Ethan_ist \t Druck1 \n"
    f.writelines(headline)

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
LOAD JSON FILEs
====================================
'''
with open(json_name +'.json', 'r') as config_file:
    config = json.load(config_file)

with open('img/setting' + str(config['REACTOR']['amount'])  + '.json', 'r') as img_file:
    img = json.load(img_file)

# Set Devices
HOST = "localhost"
PORT = 4223

ipcon = IPConnection() # Create IP connection
ipcon.connect(HOST, PORT) # Connect to brickd


tc_1 = tc(ipcon, "WR8", typ='N') #A
tc_2 = tc(ipcon, "WQp", typ='N') #B
tc_3 = tc(ipcon, "WPM", typ='N') #C
tc_4 = tc(ipcon, "23jX", typ='N') #D
tc_5 = tc(ipcon, "WpL", typ='N') #E
tc_6 = tc(ipcon, "WQC", typ='N') #F
tc_7 = tc(ipcon, "WQY", typ='N') #G
tc_8 = tc(ipcon, "WPK", typ='N') #H
tc_list = {'T1':tc_1,'T2':tc_2,'T3':tc_3,'T4':tc_4,'T5':tc_5,'T6':tc_6,'T7':tc_7,'T8':tc_8}

ido_1 = BrickletIndustrialDigitalOut4V2("TpP", ipcon)
ido_2 = BrickletIndustrialDigitalOut4V2("Tq2", ipcon)
ido_3 = BrickletIndustrialDigitalOut4V2("ToX", ipcon)
p_val = 0.005
i_val = 0.000007

patrone_1 = regler(ido_1,0,tc_1)
patrone_1.config(i_val, p_val)
patrone_1.start(-300)

patrone_2 = regler(ido_1,1,tc_2)
patrone_2.config(i_val, p_val)
patrone_2.start(-300)

patrone_3 = regler(ido_1,2,tc_3)
patrone_3.config(i_val, p_val)
patrone_3.start(-300)

patrone_4 = regler(ido_1,3,tc_4)
patrone_4.config(i_val, p_val)
patrone_4.start(-300)

patrone_5 = regler(ido_2,0,tc_5)
patrone_5.config(i_val, p_val)
patrone_5.start(-300)

patrone_6 = regler(ido_2,1,tc_6)
patrone_6.config(i_val, p_val)
patrone_6.start(-300)

patrone_7 = regler(ido_2,2,tc_7)
patrone_7.config(i_val, p_val)
patrone_7.start(-300)

patrone_8 = regler(ido_2,3,tc_8)
patrone_8.config(i_val, p_val)
patrone_8.start(-300)

patronen_list = {'p1':patrone_1,'p2':patrone_2,'p3':patrone_3,'p4':patrone_4,'p5':patrone_5,'p6':patrone_6,'p7':patrone_7,'p8':patrone_8}


option = ['T1','T2','T3','T4','T5','T6','T7','T8']
option_Heat = ['p1','p2','p3','p4','p5','p6','p7','p8']


window = ctk.CTk()
ctk.set_appearance_mode("light")
scrW = window.winfo_screenwidth()
scrH = window.winfo_screenheight()
window.geometry(str(scrW) + "x" + str(scrH))
window.title(config['REACTOR']['Name'])
window.configure(bg= config['TKINTER']['background-color'])
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
label_background = ctk.CTkLabel(window,image=bg_image,text="")
x_offset = img['Background']['x']
y_offset = img['Background']['y']
label_background.place(x = x_offset,y = y_offset)
label_background.lower()


lf_pressure = tk.LabelFrame(window, text='Druck')
lf_pressure.grid(column=3, row=2, padx=20, pady=20)
lf_pressure.place(x= 1050,y= 400)

Lable_pressure1= tk.Label(lf_pressure, text='Druck_1 ')
Lable_pressure1.grid(column=0, row=0, ipadx=5, ipady=5)
value_pressure1= tk.Label(lf_pressure, text='NaN mV')
value_pressure1.grid(column=1, row=0, ipadx=5, ipady=5)

Lable_pressure2= tk.Label(lf_pressure, text='Druck_2 ')
Lable_pressure2.grid(column=0, row=1, ipadx=5, ipady=5)
value_pressure2= tk.Label(lf_pressure, text='NaN mV')
value_pressure2.grid(column=1, row=1, ipadx=5, ipady=5)

Lable_pressure3= tk.Label(lf_pressure, text='Druck_3 ')
Lable_pressure3.grid(column=0, row=2, ipadx=5, ipady=5)
value_pressure3= tk.Label(lf_pressure, text='NaN mV')
value_pressure3.grid(column=1, row=2, ipadx=5, ipady=5)



lf_control = tk.LabelFrame(window, text='Steuerung')
lf_control.grid(column=0, row=1, padx=20, pady=20)

lable_T_ist ={}
progressbar ={}
for num, i in enumerate(option):
    lable_T_ist[i] = ctk.CTkLabel(window, font = ('Arial',16), text='0 °C')
    lable_T_ist[i].place(x = x_offset + img['T-Reaktor']['x'][num],y = y_offset + img['T-Reaktor']['y'][num])

for num, i in enumerate(option_Heat):
    progressbar[i] = ctk.CTkProgressBar(master=window, width = 80, progress_color = 'red')
    progressbar[i] .place(x = x_offset + img['T-Reaktor']['x'][num]-8,y = y_offset + img['T-Reaktor']['y'][num]+30)

set_T ={}
for i in range(0,4):
    set_T[i] = tk.Entry(window, font = ('Arial',16), width = 6,bg='light blue' )
    set_T[i].place(x = x_offset + img['T-Set']['x'][i],y = y_offset + img['T-Set']['y'][i])

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
button1 = tk.Button(lf_control,text='set values', command=getdata, bg='brown', fg='white')
button1.grid(column=3, row=9, ipadx=10, ipady=10)
Start_Button = ctk.CTkButton(master=window, command=Start_Button_callback,text="Messung starten", font = ('Arial',16))
Start_Button.place(x=300, y=50)
Stop_Button = ctk.CTkButton(master=window, command=Stop_Button_callback,text="Messung stoppen", font = ('Arial',16))
Stop_Button.place(x=300, y=100)
Heating_Button = ctk.CTkButton(master=window, command=Heating_Button_callback,text="Heating", font = ('Arial',16))
Heating_Button.place(x=300, y=150)
Exit_Button = ctk.CTkButton(master=window,text="", command=window.destroy, fg_color= 'transparent',  hover_color='#F2F2F2', image= close_img)
Exit_Button.place(x=1700, y=50)

#----------- Entry Fields------
#fileName_Entry = ctk.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
#-----------Check Boxes------
check_Verdampfer = ctk.CTkCheckBox(master=window,text = "Verdampfer an")
check_Verdampfer.place(x=100, y=50)
check_Ventile = ctk.CTkCheckBox(master=window,text = "Ventile offen")
check_Ventile.place(x=100, y=100)



#frame_T_Reactor1 = tk.LabelFrame(window, text='T-Reactor 1')
#frame_T_Reactor1.grid(column=0, row=1, padx=20, pady=20)
#frame_T_Reactor1.place(x=100,y= 200)


MCFDual1 = TF_IndustrialDualAnalogIn(ipcon, "23UP")
MFCDual2 = TF_IndustrialDualAnalogIn(ipcon, "23U6")
MFC_N2 = MFC(ipcon, "ZuC", MCFDual1,0)
MFC_Air = MFC(ipcon, "ZuD",MCFDual1,1)
MFC_Ethan = MFC(ipcon, "Tj4",MFCDual2,0)
    
pressureDual = TF_IndustrialDualAnalogIn(ipcon, "23UE")
pressure1 = pressure(pressureDual,0)
pressure2 = pressure(pressureDual,1)


window.after(1000, tk_loop())
window.mainloop()

print("shutting down...")

patrone_1.stop()
patrone_2.stop()
patrone_3.stop()
patrone_4.stop()
patrone_5.stop()
patrone_6.stop()
patrone_7.stop()
patrone_8.stop()
MFC_N2.stop()
MFC_Air.stop()
MFC_Ethan.stop()

time.sleep(2)

ipcon.disconnect()
print("bye bye")
