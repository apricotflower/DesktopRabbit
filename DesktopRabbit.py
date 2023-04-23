import base64
import os
import tkinter as tk
import tkinter.font as tkfont
import random
from Tools import *
from images import *


class DesktopRabbit:
    image_switch_job = None
    is_knife_auto_running = False

    def delete_100_text(self):
        self.canvas.delete(self.text_100_id)

    def delete_50_text(self):
        self.canvas.delete(self.text_50_id)

    def delete_10_text(self):
        self.canvas.delete(self.text_10_id)

    def delete_text(self):
        self.canvas.delete(self.text_id)

    def check_killer_counter(self):
        if self.y >= 110:
            if -(self.kill_counter - 1) % 100 == 0:
                self.text_100_id = self.canvas.create_text(70, 35, text="好友拂樱，\n吾不恨你，\n吾原谅你!", fill="red",
                                                           font=tkfont.Font(family="Helvetica", size=16, weight="bold"))
            elif -(self.kill_counter - 1) % 50 == 0:
                self.text_50_id = self.canvas.create_text(70, 50, text="偶开天眼觑红尘，\n可怜身是眼中人……",
                                                          fill="#bf90f7")
            elif -(self.kill_counter - 1) % 10 == 0:
                self.text_10_id = self.canvas.create_text(70, 50, text="地狱无你何等失味！", fill="#bf90f7")
            else:
                self.text_id = self.canvas.create_text(35, 100, text="捅柚 + 1", fill="#bf90f7")

            self.kill_counter = self.kill_counter - 1
            self.kill_counter_label.config(text=" 好友度： " + str(self.kill_counter))

            if -self.kill_counter % 100 == 0:
                self.canvas.after(1000, self.delete_100_text)
            elif -self.kill_counter % 50 == 0:
                self.canvas.after(1000, self.delete_50_text)
            elif -self.kill_counter % 10 == 0:
                self.canvas.after(1000, self.delete_10_text)
            else:
                self.canvas.after(200, self.delete_text)

    def set_common_img(self):
        self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_common)

    def set_knife_img(self, *args):
        self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_knife)
        self.current_image = 2
        self.check_killer_counter()
        self.master.after(300, self.set_common_img)

    def update_image(self):
        if self.current_image == 1:
            self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_knife)
            self.current_image = 2
        else:
            self.canvas.itemconfigure(self.image_rabbit_id, image=self.image_rabbit_green)
            self.check_killer_counter()
            self.current_image = 1
        self.master.update()
        if self.is_knife_auto_running:
            self.image_switch_job = self.master.after(200, self.update_image)

    def knife_auto(self, *args):
        if not self.is_knife_auto_running:
            self.is_knife_auto_running = True
            self.canvas.tag_unbind(self.image_rabbit_id, "<Button-1>")
            self.current_image = 1
            self.update_image()

    def stop_auto(self, *args):
        if self.is_knife_auto_running:
            self.master.after_cancel(self.image_switch_job)
            self.is_knife_auto_running = False
            self.canvas.tag_unbind(self.image_rabbit_id, "<Button-1>")
            self.canvas.tag_bind(self.image_rabbit_id, "<Button-1>", self.set_knife_img)
            self.set_common_img()

    def set_button(self):
        auto_label = tk.Label(self.master, image=self.button_img, text="自动捅柚", compound='center', fg="#008080")
        auto_label.bind("<Button-1>", self.knife_auto)
        auto_label.place(x=10, y=160)

        manual_label = tk.Label(self.master, image=self.button_img, text="手动捅柚", compound='center', fg="#e6b7d0")
        manual_label.bind("<Button-1>", self.stop_auto)
        manual_label.place(x=100, y=160)

    def destroy(self, *args):
        file_paths = ['button.png', 'flower_green.png', 'flower_pink.png', 'pink_rabbit.png', 'rabbit_common.PNG', 'rabbit_knife.PNG', 'yuzu_left.png']
        for file_path in file_paths:
            if os.path.exists(file_path):
                os.remove(file_path)
        self.master.quit()

    def set_quit(self):
        image_quit_id = self.canvas.create_image(0, 0, image=self.quit_img, anchor="nw")
        self.canvas.tag_bind(image_quit_id, "<Button-1>", self.destroy)

    def animate_image(self, angle, dx, dy):
        self.canvas.delete(self.image_yuzu_id)
        with open('yuzu_left.png', 'wb') as w:
            w.write(base64.b64decode(yuzu_left_png))
        self.rotated_image = resize_image(open_image('yuzu_left.png').rotate(angle), (40, 40))
        os.remove('yuzu_left.png')

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
        self.master.geometry("200x230")
        self.canvas_width = 200
        self.canvas_height = 158
        with open('pink_rabbit.png', 'wb') as w:
            w.write(base64.b64decode(pink_rabbit_png))
        self.image_rabbit_common = re_size('pink_rabbit.png', (self.canvas_width, self.canvas_height))
        os.remove('pink_rabbit.png')
        with open('rabbit_knife.PNG', 'wb') as w:
            w.write(base64.b64decode(rabbit_knife_PNG))
        self.image_rabbit_knife = re_size('rabbit_knife.PNG', (self.canvas_width, self.canvas_height))
        os.remove('rabbit_knife.PNG')
        with open('rabbit_common.PNG', 'wb') as w:
            w.write(base64.b64decode(rabbit_common_PNG))
        self.image_rabbit_green = re_size('rabbit_common.PNG', (self.canvas_width, self.canvas_height))
        os.remove('rabbit_common.PNG')
        with open('flower_pink.png', 'wb') as w:
            w.write(base64.b64decode(flower_pink_png))
        self.quit_img = re_size('flower_pink.png', (20, 20))
        os.remove('flower_pink.png')
        with open('button.png', 'wb') as w:
            w.write(base64.b64decode(button_png))
        self.button_img = re_size('button.png', (90, 40))
        os.remove('button.png')
        with open('yuzu_left.png', 'wb') as w:
            w.write(base64.b64decode(yuzu_left_png))
        self.image_yuzu = re_size('yuzu_left.png', (50, 50))
        os.remove('yuzu_left.png')
        with open('flower_green.png', 'wb') as w:
            w.write(base64.b64decode(flower_green_png))
        self.kill_counter_flower = re_size('flower_green.png', (20, 20))
        os.remove('flower_green.png')

        self.rotated_image = None
        self.text_id = None
        self.text_10_id = None
        self.text_50_id = None
        self.text_100_id = None
        self.kill_counter = 0

        self.current_image = 1

        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.image_rabbit_id = self.canvas.create_image(0, 0, image=self.image_rabbit_common, anchor="nw")
        self.canvas.tag_bind(self.image_rabbit_id, "<Button-1>", self.set_knife_img)

        self.kill_counter_label = tk.Label(self.master, image=self.kill_counter_flower,
                                           text=" 好友度： " + str(self.kill_counter), compound='left', fg="#bf90f7",
                                           font=("Helvetica", 14, "bold"))
        self.kill_counter_label.place(x=60, y=205)

        self.x = random.randint(0, 30)
        self.y = random.randint(30, 158)
        self.image_yuzu_id = None
        self.animate_image(0, 3, 3)

        self.set_quit()
        self.set_button()
