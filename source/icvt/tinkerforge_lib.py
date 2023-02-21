#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import tkinter as tk
from PIL import Image,ImageTk
import time
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_thermocouple_v2 import BrickletThermocoupleV2
from tinkerforge.bricklet_industrial_digital_out_4_v2 import BrickletIndustrialDigitalOut4V2
from tinkerforge.bricklet_industrial_analog_out_v2 import BrickletIndustrialAnalogOutV2
from tinkerforge.bricklet_analog_in_v3 import BrickletAnalogInV3
from tinkerforge.bricklet_industrial_dual_analog_in_v2 import BrickletIndustrialDualAnalogInV2



class regler:
    t_soll = 0
    ki = 0
    kp = 0
    i = 0
    time_last_call = datetime.now()
    pwroutput = 0

    def __init__(self, ido_handle, channel, tc_handle, frequency = 10) -> None:
        self.running = False
        self.tc = tc_handle
        self.channel = channel
        self.ido = ido_handle
        self.frequency = frequency
        self.ido.set_pwm_configuration(channel, self.frequency, 0)

    def config(self, ki, kp):
        self.ki = ki
        self.kp = kp

    def start(self, t_soll):
        self.t_soll = t_soll
        self.running = True
        self.time_last_call = datetime.now()

    def stop(self):
        self.running = False
        self.regeln()
    
    def set_t_soll(self, t_soll):
        self.t_soll = t_soll

    def regeln(self):
        if self.running == True:
            dT = self.t_soll - self.tc.t
            p = self.kp*(dT)
            now = datetime.now()
            dtime = (now - self.time_last_call).total_seconds()
            self.time_last_call = now
            self.i = self.i + dT*self.ki*(dtime)
            
            pi = p+self.i
            if pi > 1:
                pi = 1
                self.i = pi - p
            elif pi < 0:
                pi = 0
            if self.i < 0:
                self.i = 0
            duty = 10000*(pi)
            self.pwroutput = duty/10000
            self.ido.set_pwm_configuration(self.channel, self.frequency, duty)
            #print("duty = " + str(duty))
            #print("pi = " + str(pi))
        else:
            duty = 0
            self.ido.set_pwm_configuration(self.channel, self.frequency, duty)

class tc:
    UID = ''
    t = -300
    def __init__(self,ipcon,ID,typ='K') -> None:
        self.UID = ID
        self.obj = BrickletThermocoupleV2(ID, ipcon)
        
        type_dict = {'B' : 0, 'E' : 1, 'J' : 2, 'K' : 3, 'N' : 4, 'R' : 5, 'S' : 6, 'T' : 7}

        thermocouple_type = type_dict[typ]
        self.obj.set_configuration(16, thermocouple_type, 0)

        self.start()
    
    def start(self):
        self.obj.register_callback(self.obj.CALLBACK_TEMPERATURE, self.cb_read_t)
        self.obj.set_temperature_callback_configuration(1000, False, "x", 0, 0)

    def cb_read_t(self,temperature):
        #print("Temperature: " + str(temperature/100.0) + " °C")
        ##print(self.UID)
        self.t = temperature/100    

class MFC:
    UID = ''
    Voltage = 0
    def cb_voltage(self,voltages):
        print(self.AinName )
        print("Voltage1: " + str(voltages[0]/1000.0) + " Voltage2: " + str(voltages[1]/1000.0))
        #if self.channel == channel:
            #self.Voltage = voltage/1.0
            #print("Channel: " + str(channel) +" Voltage: " + str(voltage/1.0) + " mV")

    def __init__(self,ipcon,ID_out,ID_in,channel) -> None:
        self.UID = ID_out
        self.Aout = BrickletIndustrialAnalogOutV2(ID_out, ipcon)
        #self.Ain = BrickletAnalogInV3(ID_in, ipcon) old Version, not for Industrial Analog in
        self.Ain = BrickletIndustrialDualAnalogInV2(ID_in, ipcon)
        self.Aout.set_voltage(0)
        self.Aout.set_enabled(True)
        self.Aout.set_out_led_status_config(0, 5000, 1)
        self.Ain.register_callback(self.Ain.CALLBACK_ALL_VOLTAGES, self.cb_voltage)
        self.AinName = ID_in + " " + str(channel )
        self.channel = channel
        #self.Ain.set_voltage_callback_configuration(1000, False, "x", 0, 0) old Version, not for Industrial Analog in
        #self.Ain.set_voltage_callback_configuration(channel, 500, False, "x", 0, 0)
        self.Ain.set_all_voltages_callback_configuration(500, False)
        #self.Ain.set_voltage_callback_configuration(1, 500, False, "x", 0, 0)
        #self.obj.set_configuration(0,0)


    def set(self,value):
        self.Aout.set_voltage(value)
    
    def stop(self):
        self.Aout.set_voltage(0)
        self.Aout.set_enabled(False)


