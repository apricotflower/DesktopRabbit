from PIL import Image, ImageTk


def re_size(path, size):
    image = open_image(path)
    img = image.resize(size)
    my_img = ImageTk.PhotoImage(img)
    return my_img


def open_image(path):
    image = Image.open(path)
    return image


def resize_image(image, size):
    img = image.resize(size)
    my_img = ImageTk.PhotoImage(img)
    return my_img
