import tkinter as tk
from DesktopPet import DesktopPet
from DesktopRabbit import DesktopRabbit
from DragPet import DragPet
from RotatedYuzu import RotatedYuzu

if __name__ == "__main__":
    root = tk.Tk()
    drag = DragPet(root)
    root.overrideredirect(True)
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-transparent", True)
    # root.configure(bg='systemTransparent')
    # self.master.attributes("-alpha", 0.1)
    # yuzu = RotatedYuzu(root)
    # pet = DesktopPet(root)
    pet = DesktopRabbit(root)
    root.mainloop()
