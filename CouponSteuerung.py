from TinkerForgeHelperLib.tinkerforge_lib import TFH
from TKinter_HelperLib.tkinter_lib import *
from time import sleep



def main():
    json_GUI = "GUI_settings"

    tfh_obj = TFH("localhost", 4223, debug_mode = 1)
    
    window, frames, config = setup_gui(json_GUI)

    entries = create_entries(tfh_obj, frames)    
    labels = create_labels(tfh_obj, frames, config)
    
    tk_loopNew(window, tfh_obj, labels, entries)  
    
    window.mainloop()
    print("shutting down...")
    time.sleep(2)
    tfh_obj.cleanup()
    print("bye bye") 

if __name__ == "__main__":
    main()