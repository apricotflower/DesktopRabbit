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
        self.master.after(300, self.set_common_img)

    def knife_auto(self, *args):
        if not self.is_knife_auto_running:
            self.is_knife_auto_running = True
            self.canvas.unbind("<Button-1>")

            def update_image():
                if self.current_image == 1:
                    self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_knife)
                    self.current_image = 2
                else:
                    self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_green)
                    self.current_image = 1
                self.master.update()
                if self.is_knife_auto_running:
                    self.image_switch_job = self.master.after(200, update_image)

            update_image()

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

    def animate_image(self, angle, x, y, delta_x, delta_y):
        self.canvas.delete(self.image_yuzu_id)
        self.rotated_image = resize_image(open_image("image/yuzu_left.png").rotate(angle), (40, 40))

        # 更新图片的位置
        x += delta_x
        y += delta_y

        # 判断图片是否撞墙
        if x <= 0 or x + self.rotated_image.width() >= self.canvas_width:
            delta_x = -delta_x
        if y <= 0 or y + self.rotated_image.height() >= self.canvas_height:
            delta_y = -delta_y

        self.image_yuzu_id = self.canvas.create_image(x, y, image=self.rotated_image)
        self.canvas.after(10, self.animate_image, angle + 10, x, y, delta_x, delta_y)

    def __init__(self, master):
        self.master = master
        self.master.title("兔兔捅柚")
        self.master.geometry("200x210")
        self.image_rabbit_common = re_size('image/pink rabbit.png', (200, 158))
        self.image_rabbit_knife = re_size('image/rabbit_knife.PNG', (200, 158))
        self.image_rabbit_green = re_size('image/rabbit_common.PNG', (200, 158))
        self.quit_img = re_size('image/flower_pink.png', (30, 30))
        self.button_img = re_size('image/button.png', (90, 40))
        self.image_yuzu = re_size('image/yuzu_left.png', (50, 50))
        self.rotated_image = None

        self.current_image = 1

        self.canvas_width = 200
        self.canvas_height = 158

        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.image_rabbit_id = self.canvas.create_image(0, 0, image=self.image_rabbit_common, anchor="nw")
        self.canvas.bind("<Button-1>", self.set_knife_img)

        # self.image_yuzu_id = self.canvas.create_image(0, 0, image=self.image_yuzu, anchor="center")
        x1 = random.randint(30, int(self.canvas_width/2))  # x1 为图片2左上角 x 坐标的随机值
        y1 = random.randint(30, self.canvas_height)  # y1 为图片2左上角 y 坐标的随机值
        dx = random.choice([-3, 3])  # dx 为图片2在 x 方向上的移动步长，随机选择 -5 或 5
        dy = random.choice([-3, 3])  # dy 为图片2在 y 方向上的移动步长，随机选择 -5 或 5
        self.image_yuzu_id = None
        # self.canvas.move(self.image_yuzu_id, x1, y1)  # 移动图片2到随机生成的初始坐标
        self.animate_image(0, x1, y1, dx, dy)

        self.set_quit()
        self.set_button()
