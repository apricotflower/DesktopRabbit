def save_last_click_pos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


class DragPet:
    lastClickX = 0
    lastClickY = 0

    def dragging(self, event):
        x, y = event.x - lastClickX + self.master.winfo_x(), event.y - lastClickY + self.master.winfo_y()
        self.master.geometry("+%s+%s" % (x, y))

    def __init__(self, master):
        self.master = master
        self.master.bind('<Button-1>', save_last_click_pos)
        self.master.bind('<B1-Motion>', self.dragging)
