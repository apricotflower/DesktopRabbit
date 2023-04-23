import tkinter as tk
from DesktopRabbit import DesktopRabbit
from DragPet import DragPet
import base64
import os
from images import *

if __name__ == "__main__":
    root = tk.Tk()
    # with open('rabbit_icon.ico', 'wb') as w:
    #     w.write(base64.b64decode(rabbit_icon_ico))
    # root.wm_iconbitmap('rabbit_icon.ico')
    # os.remove('rabbit_icon.ico')
    drag = DragPet(root)
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    # root.wm_attributes("-transparent", True)
    # root.configure(bg='systemTransparent')
    # self.master.attributes("-alpha", 0.1)
    pet = DesktopRabbit(root)
    root.mainloop()
