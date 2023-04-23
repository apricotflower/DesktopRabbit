import tkinter as tk
import random
from Tools import *


class DesktopRabbit:
    image_switch_job = None
    is_knife_auto_running = False

    def set_common_img(self):
        self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_common)

    def set_knife_img(self, *args):
        self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_knife)
        self.current_image = 2
        if self.y >= 110:
            self.text_id = self.canvas.create_text(35, 100, text="捅柚 + 1", fill="#800080")
            self.kill = self.kill + 1
            self.canvas.after(15, self.delete_text)
        self.master.after(300, self.set_common_img)

    def update_image(self):
        if self.current_image == 1:
            self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_knife)
            self.current_image = 2
        else:
            self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_green)
            if self.y >= 110:
                self.text_id = self.canvas.create_text(35, 100, text="捅柚 + 1", fill="#800080")
                self.kill = self.kill + 1
                self.canvas.after(15, self.delete_text)
            self.current_image = 1
        self.master.update()
        if self.is_knife_auto_running:
            self.image_switch_job = self.master.after(200, self.update_image)

    def knife_auto(self, *args):
        if not self.is_knife_auto_running:
            self.is_knife_auto_running = True
            self.canvas.unbind("<Button-1>")
            self.current_image = 1
            self.update_image()

    def stop_auto(self, *args):
        if self.is_knife_auto_running:
            self.master.after_cancel(self.image_switch_job)
            self.is_knife_auto_running = False
            self.canvas.unbind("<Button-1>")
            self.canvas.bind("<Button-1>", self.set_knife_img)
            self.set_common_img()

    def set_button(self):
        auto_label = tk.Label(self.master, image=self.button_img, text="自动捅柚", compound='center', fg="#008080")
        auto_label.bind("<Button-1>", self.knife_auto)
        auto_label.place(x=10, y=160)

        manual_label = tk.Label(self.master, image=self.button_img, text="手动捅柚", compound='center', fg="#e6b7d0")
        manual_label.bind("<Button-1>", self.stop_auto)
        manual_label.place(x=100, y=160)

    def destroy(self, *args):
        self.master.destroy()

    def set_quit(self):
        image_quit_id = self.canvas.create_image(0, 0, image=self.quit_img, anchor="nw")
        self.canvas.tag_bind(image_quit_id, "<Button-1>", self.destroy)

    def delete_text(self):
        # 从 canvas 中删除文本对象
        self.canvas.delete(self.text_id)

    def animate_image(self, angle, dx, dy):
        self.canvas.delete(self.image_yuzu_id)
        self.rotated_image = resize_image(open_image("image/yuzu_left.png").rotate(angle), (40, 40))

        # 更新图片的位置
        self.x += dx
        self.y += dy

        # 判断图片是否撞墙
        if self.x <= 0 or self.x >= 50:
            dx = -dx
        if self.y <= 30 or self.y >= self.canvas_height:
            dy = -dy

        self.image_yuzu_id = self.canvas.create_image(self.x, self.y, image=self.rotated_image)
        self.canvas.after(20, self.animate_image, angle + 10, dx, dy)

    def __init__(self, master):
        self.master = master
        self.master.title("兔兔捅柚")
        self.master.geometry("200x210")
        self.canvas_width = 200
        self.canvas_height = 158
        self.image_rabbit_common = re_size('image/pink rabbit.png', (self.canvas_width, self.canvas_height))
        self.image_rabbit_knife = re_size('image/rabbit_knife.PNG', (self.canvas_width, self.canvas_height))
        self.image_rabbit_green = re_size('image/rabbit_common.PNG', (self.canvas_width, self.canvas_height))
        self.quit_img = re_size('image/flower_pink.png', (30, 30))
        self.button_img = re_size('image/button.png', (90, 40))
        self.image_yuzu = re_size('image/yuzu_left.png', (50, 50))
        self.rotated_image = None
        self.text_id = None
        self.kill = 0

        self.current_image = 1

        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.image_rabbit_id = self.canvas.create_image(0, 0, image=self.image_rabbit_common, anchor="nw")
        self.canvas.bind("<Button-1>", self.set_knife_img)

        self.x = random.randint(0, 30)
        self.y = random.randint(30, 158)
        self.image_yuzu_id = None
        self.animate_image(0, 3, 3)

        self.set_quit()
        self.set_button()
