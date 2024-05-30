import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from TinkerForgeHelperLib.tinkerforge_lib import TFH
from TKinter_HelperLib.tkinter_lib import *
from utilities.regler import *
from time import sleep



def main():
    json_GUI = "GUI_settings"

    tfh_obj = TFH("localhost", 4223)
    
    tk_obj = setup_gui(json_GUI)

    tk_obj = create_entries(tk_obj, tfh_obj)    
    tk_obj = create_labels(tk_obj, tfh_obj)
    tk_obj = create_buttons(tk_obj, tfh_obj)
    tk_obj = setup_controller(tk_obj, tfh_obj)

    tk_loopNew(tk_obj, tfh_obj)  
    
    tk_obj.mainloop()
    print("shutting down...")
    time.sleep(2)
    tfh_obj.cleanup()
    print("bye bye") 

if __name__ == "__main__":
    main()