import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime
from source.icvt.tinkerforge_lib import *

HOST = "localhost"
PORT = 4223

filename = "20221212_EthanH2OTest.dat"
filename2 = "20221212_EthanH2OTest_Tcoupon.dat"

# from source.tinkerforge.ip_connection import IPConnection
# from source.tinkerforge.bricklet_thermocouple_v2 import BrickletThermocoupleV2
# from source.tinkerforge.bricklet_industrial_digital_out_4_v2 import BrickletIndustrialDigitalOut4V2

def regler_loop():

    for tc_obj_name in tc_list:
        lable_t_ist_dict[tc_obj_name].config(text = str(tc_list[tc_obj_name].t)+"°C")
    # lable_t_ist_dict['T2'].config(text = str(tc_2.t)+"°C")
    
    print("Voltage: " + str(MFC_N2.Voltage) + " mV")
    value_MFC_N2.config(text = str(MFC_N2.Voltage) + " mV") 
    value_MFC_Ethan.config(text = str(MFC_Ethan.Voltage) + " mV") 
    sFlag.config(text=str(saveflag))

    with open(filename, 'a') as f:
        line = datetime.now().strftime("%H:%M:%S:\t")
        for tc_obj_name in tc_list:
            line += str(tc_list[tc_obj_name].t) + '\t'
        for p_obj_name in patronen_list:
            line += str(patronen_list[p_obj_name].pwroutput) + '\t'
        line += '/n'
        f.writelines(line)

    """ if saveflag ==1: 
        with open(filename2, 'a') as fid:
            line = datetime.now().strftime("%H:%M:%S:\t")
            line += str(T1_profil.t) + '\t'
            line += str(T2_profil.t) + '\t'
            line += '/n'
            fid.writelines(line) """

    patrone_1.regeln()
    patrone_2.regeln()
    patrone_3.regeln()
    patrone_4.regeln()
    patrone_5.regeln()
    patrone_6.regeln()
    patrone_7.regeln()
    patrone_8.regeln()
    #heater.regeln()


    #Recursively call the function
    root.after(1000, regler_loop)

def getdata():
    for i in set_temp_dict:
        t_soll[i] = set_temp_dict[i].get()
        print(t_soll[i])

    if set_temp_dict['T1'].get() != '':
        patrone_1.set_t_soll(float(set_temp_dict['T1'].get()))
    if set_temp_dict['T2'].get() != '':
        patrone_2.set_t_soll(float(set_temp_dict['T2'].get()))
    if set_temp_dict['T3'].get() != '':
        patrone_3.set_t_soll(float(set_temp_dict['T3'].get()))
    if set_temp_dict['T4'].get() != '':
        patrone_4.set_t_soll(float(set_temp_dict['T4'].get()))
    if set_temp_dict['T5'].get() != '':
        patrone_5.set_t_soll(float(set_temp_dict['T5'].get()))
    if set_temp_dict['T6'].get() != '':
        patrone_6.set_t_soll(float(set_temp_dict['T6'].get()))
    if set_temp_dict['T7'].get() != '':
        patrone_7.set_t_soll(float(set_temp_dict['T7'].get()))
    if set_temp_dict['T8'].get() != '':
        patrone_8.set_t_soll(float(set_temp_dict['T8'].get()))
    #if set_temp_dict['T9'].get() != '':
        #heater.set_t_soll(float(set_temp_dict['T9'].get()))
    
    MFC_N2_soll = int(set_MFC_N2.get())
    MFC_N2.set(MFC_N2_soll)

def savedata():
    global saveflag 
    if saveflag !=1:
        saveflag =1
        button2 = tk.Button(lf,text='Save Data', command=savedata, bg='blue', fg='white')
    else:
        saveflag =0
        button2 = tk.Button(lf,text='Save Data', command=savedata, bg='brown', fg='white')
    return saveflag


with open(filename, 'w') as f:
    headline = "time \t t1 \t t2 \t t3 \t t4 \t t5 \t t6 \t t7 \t t8 \t t9 \t p1 \t p2 \t p3 \t p4 \t p5 \t p6 \t p7 \t p8 \t heater\n"
    f.writelines(headline)

with open(filename2, 'w') as fid:
    headline2 = "time \t T1_profil \t T2_profil\n"
    fid.writelines(headline2)


ipcon = IPConnection() # Create IP connection
ipcon.connect(HOST, PORT) # Connect to brickd
# Don't use device before ipcon is connected

MFC_N2 = MFC(ipcon, "ZuC", "23UP",0)
#MFC_Air = MFC(ipcon, "ZuD")
MFC_Ethan = MFC(ipcon, "ZuD","23UE",1)

tc_1 = tc(ipcon, "WPK", typ='N') #A
tc_2 = tc(ipcon, "WQY", typ='N') #B
tc_3 = tc(ipcon, "WQC", typ='N') #C
tc_4 = tc(ipcon, "WpL", typ='N') #D
tc_5 = tc(ipcon, "WQT", typ='N') #E
tc_6 = tc(ipcon, "WPM", typ='N') #F
tc_7 = tc(ipcon, "WQp", typ='N') #G
tc_8 = tc(ipcon, "WR8", typ='N') #H
#tc_9 = tc(ipcon, "", typ='N') #Heater

#T1_profil = tc(ipcon, "", typ='K') #H
#T2_profil  = tc(ipcon, "", typ='K') #H

#tc_list = {'T1':tc_1,'T2':tc_2,'T3':tc_3,'T4':tc_4,'T5':tc_5,'T6':tc_6,'T7':tc_7,'T8':tc_8,'T9':tc_9}
tc_list = {'T1':tc_1,'T2':tc_2,'T3':tc_3,'T4':tc_4,'T5':tc_5,'T6':tc_6,'T7':tc_7,'T8':tc_8}

saveflag= 0

ido_1 = BrickletIndustrialDigitalOut4V2("TpA", ipcon)
ido_2 = BrickletIndustrialDigitalOut4V2("TnQ", ipcon)
ido_3 = BrickletIndustrialDigitalOut4V2("Tmw", ipcon)
p_val = 0.005
i_val = 0.00001

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

#heater = regler(ido_3,0,tc_9)
#heater.config(i_val, p_val)
#heater.start(-300)

#patronen_list = {'p1':patrone_1,'p_2':patrone_2,'p_3':patrone_3,'p_4':patrone_4,'p_5':patrone_5,'p_6':patrone_6,'p_7':patrone_7,'p_8':patrone_8,'heat':heater}
patronen_list = {'p1':patrone_1,'p_2':patrone_2,'p_3':patrone_3,'p_4':patrone_4,'p_5':patrone_5,'p_6':patrone_6,'p_7':patrone_7,'p_8':patrone_8}


root = tk.Tk()
root.title("HT Couponanlage")
root.resizable(True, True)
root.columnconfigure(0, weight=7)
root.rowconfigure(0, weight=2)
root.geometry("1600x800")
sg = ttk.Sizegrip(root)
sg.grid(row=2, sticky=tk.SE)


lf_MFC = ttk.LabelFrame(root, text='MFC Steuerung')
lf_MFC.grid(column=0, row=0, padx=5, pady=5)
Lable_MFC_N2= ttk.Label(lf_MFC, text='MFC_N2 ')
Lable_MFC_N2.grid(column=0, row=0, ipadx=5, ipady=5)
set_MFC_N2 = ttk.Entry(lf_MFC, width= 20)
set_MFC_N2.grid(column=1, row=0, ipadx=5, ipady=5)
unit_MFC_N2= ttk.Label(lf_MFC, text=' mV')
unit_MFC_N2.grid(column=2, row=0, ipadx=5, ipady=5)
value_MFC_N2= ttk.Label(lf_MFC, text='NaN mV')
value_MFC_N2.grid(column=3, row=0, ipadx=5, ipady=5)

set_MFC_Air = ttk.Entry(lf_MFC, width= 20)
set_MFC_Air.grid(column=1, row=1, ipadx=5, ipady=5)

set_MFC_Ethan = ttk.Entry(lf_MFC, width= 20)
set_MFC_Ethan.grid(column=1, row=2, ipadx=5, ipady=5)

value_MFC_Ethan= ttk.Label(lf_MFC, text='NaN mV')
value_MFC_Ethan.grid(column=3, row=2, ipadx=5, ipady=5)


set_temp_dict = {}
lable_dict = {}
lable_t_ist_dict = {}
#option = ['T1','T2','T3','T4','T5','T6','T7','T8','T9']
option = ['T1','T2','T3','T4','T5','T6','T7','T8']

lf = ttk.LabelFrame(root, text='Reactor 1')
lf.grid(column=0, row=1, padx=20, pady=20)

alignment_var = tk.StringVar()

for num, i in enumerate(option):
    lable_dict[i]= ttk.Label(lf, text=i)
    lable_dict[i].grid(column=0, row=num, ipadx=10, ipady=10)
    #lable_dict[i].pack(side="left")
    set_temp_dict[i] = ttk.Entry(lf, width= 20, textvariable=i)
    set_temp_dict[i].grid(column=1, row=num, ipadx=10, ipady=10)
    #set_temp_dict[i].pack(side="right")
    lable_t_ist_dict[i]= ttk.Label(lf, text='NaN °C')
    lable_t_ist_dict[i].grid(column=3, row=num, ipadx=10, ipady=10)

t_soll = {}

sFlag =ttk.Label(lf, text=str(saveflag))
sFlag.grid(column=2, row=10, ipadx=10, ipady=10)

button1 = tk.Button(lf,text='set values', command=getdata, bg='brown', fg='white')
button1.grid(column=3, row=9, ipadx=10, ipady=10)

button2 = tk.Button(lf,text='Save Data', command=savedata, bg='brown', fg='white')
button2.grid(column=2, row=9, ipadx=10, ipady=10)


root.after(1000, regler_loop())
root.mainloop()

### exit routine
print("shutting down...")

patrone_1.stop()
patrone_2.stop()
patrone_3.stop()
patrone_4.stop()
patrone_5.stop()
patrone_6.stop()
patrone_7.stop()
patrone_8.stop()
#heater.stop()
MFC_N2.stop()
MFC_Ethan.stop()

time.sleep(2)

ipcon.disconnect()
print("bye bye")