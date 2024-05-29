config = {
    "MFC_N2": { 
        "type": "mfc",
        "input_device": "24xB", # IstSignal
        "input_channel": 0, 
        "output_device": "27xE",# SollSignal
        "output_channel": 0,
        "unit": "ml/min",
        "gradient": 0.2, # Steigung umrechnung Rohdaten mV in mL/min 
        "y-axis":   0,  # Y-Achsenabschnitt umrechnung Rohdaten
        "x": 50,    # Position in Gui
        "y": 20,     # Position in Gui
        "permissible_deviation": 0.1,
        "last_deviation": 10 
    },
    
    "MFC_O2": { 
        "type": "mfc",
        "input_device": "24xB",
        "input_channel": 1,
        "output_device": "Tgv",
        "output_channel": 0,
        "unit": "ml/min",
        "gradient": 0.5,
        "y-axis":   0,
        "x": 50,
        "y": 20,
        "permissible_deviation": 0.1,
        "last_deviation": 10 
    }
}
