config = {
    "MFC_N2": { 
        "type": "mfc",
        "input_device": "23UP", # IstSignal
        "input_channel": 0, 
        "output_device": "ZuC",# SollSignal
        "output_channel": 0,
        "unit": "ml/min",
        "gradient": 0.2, # Steigung umrechnung Rohdaten mV in mL/min 
        "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
        "x": 50,    # Position in Gui
        "y": 750,     # Position in Gui
    },
    
    "MFC_Air": { 
        "type": "mfc",
        "input_device": "23UP",
        "input_channel": 1,
        "output_device": "ZuD",
        "output_channel": 0,
        "unit": "ml/min",
        "gradient": 0.2,
        "y-axis":   0,
        "x": 50,
        "y": 750,
    },
    
    "MFC_Ethan": { 
        "type": "mfc",
        "input_device": "23U6",
        "input_channel": 0,
        "output_device": "Tj4",
        "output_channel": 0,
        "unit": "ml/min",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 50,
        "y": 750,
    },
    
    "Verdampfer": { 
        "type": "ExtOutput",
        "output_device": "TiX",
        "output_channel": 1,
        "unit": "ml/min",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 940,
    },
    
    "CO2_1": { 
        "type": "ExtInput",
        "input_device": "27DS",
        "input_channel": 0,
        "unit": "ppm",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 940,
    },
    
    "CO2_2": { 
        "type": "ExtInput",
        "input_device": "27DS",
        "input_channel": 1,
        "unit": "%",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 940,
    },
    
    "V1": { 
        "type": "valve",
        "output_device": "Zt2",
        "output_channel": 0,
        "unit": "mbar",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 940,
    },
    
    "V2": { 
        "type": "valve",
        "output_device": "Zt2",
        "output_channel": 1,
        "unit": "mbar",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 940,
    },
    
    "p_Verdampfer": { 
        "type": "pressure",
        "input_device": "23UK",
        "input_channel": 0,
        "unit": "mbar",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 940,
    },
    
    "p_Anlage": { 
        "type": "pressure",
        "input_device": "23UK",
        "input_channel": 1,
        "unit": "mbar",
        "gradient":1,
        "y-axis":   0,
        "x": 955,
        "y": 890,
    },
    
    "HP_1": { 
        "type": "easy_PI",
        "input_device": "T_R1",
        "output_type": "PWM",
        "output_device": "Tmw",
        "output_channel": 0,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 800,
        "y": 670,
    },
    
    "HP_2": { 
        "type": "easy_PI",
        "input_device": "T_R2",
        "output_type": "PWM",
        "output_device": "Tmw",
        "output_channel": 1,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 800,
        "y": 540,
    },
    
    "HP_3": { 
        "type": "easy_PI",
        "input_device": "T_R3",
        "output_type": "PWM",
        "output_device": "Tmw",
        "output_channel": 2,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 800,
        "y": 410,
    },
    
    "HP_4": { 
        "type": "easy_PI",
        "input_device": "T_R4",
        "output_type": "PWM",
        "output_device": "Tmw",
        "output_channel": 3,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 800,
        "y": 280,
    },
    
    "HP_5": { 
        "type": "easy_PI",
        "input_device": "T_R5",
        "output_type": "PWM",
        "output_device": "TnQ",
        "output_channel": 0,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 925,
        "y": 723,
    },
    
    "HP_6": { 
        "type": "easy_PI",
        "input_device": "T_R6",
        "output_type": "PWM",
        "output_device": "TnQ",
        "output_channel": 1,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 925,
        "y": 593,
    },
    
    "HP_7": { 
        "type": "easy_PI",
        "input_device": "T_R7",
        "output_type": "PWM",
        "output_device": "TnQ",
        "output_channel": 2,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 925,
        "y": 463,
    },
    
    "HP_8": { 
        "type": "easy_PI",
        "input_device": "T_R8",
        "output_type": "PWM",
        "output_device": "TnQ",
        "output_channel": 3,
        "unit": "%",
        "P_Value": 0.018,
        "I_Value": 0.000013,
        "x": 925,
        "y": 333,
    },
    
    "T_R1": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WPP",
        "input_channel": 0,
        "unit": "°C",
        "x": 650,
        "y": 670,
    },
    
    "T_R2": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WQ3",
        "input_channel": 0,
        "unit": "°C",
        "x": 650,
        "y": 540,
    },
    
    "T_R3": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "23jQ",
        "input_channel": 0,
        "unit": "°C",
        "x": 650,
        "y": 410,
    },
    
    "T_R4": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "26WH",
        "input_channel": 0,
        "unit": "°C",
        "x": 650,
        "y": 280,
    },
    
    "T_R5": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WQh",
        "input_channel": 0,
        "unit": "°C",
        "x": 1055,
        "y": 723,
    },
    
    "T_R6": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "23jP",
        "input_channel": 0,
        "unit": "°C",
        "x": 1055,
        "y": 593,
    },
    
    "T_R7": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "23iy",
        "input_channel": 0,
        "unit": "°C",
        "x": 1055,
        "y": 463,
    },
    
    "T_R8": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "23ja",
        "input_channel": 0,
        "unit": "°C",
        "x": 1055,
        "y": 333,
    },
    
    "T_1": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WjR",
        "input_channel": 0,
        "unit": "°C",
        "x": 955,
        "y": 890,
    },
    
    "T_2": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WQT",
        "input_channel": 0,
        "unit": "°C",
        "x": 955,
        "y": 890,
    },
    
    "T_3": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WR8",
        "input_channel": 0,
        "unit": "°C",
        "x": 955,
        "y": 890,
    }
}
