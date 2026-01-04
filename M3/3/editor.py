from customtkinter import *
from PIL import Image, ImageFilter


win = CTk()
win.geometry("600x500")
set_default_color_theme("green")
win.title("EDITOR")

image = Image.open("3.png")
image_ctk = CTkImage(image, size = (300,200))
label_img= CTkLabel(win, image = image_ctk, text="")
label_img.pack(padx = 10, pady = 10)

set_fram = CTkFrame(win)
set_fram.pack(side="bottom", pady = 10)

def do_Rotate():
    global image
    image = image.rotate(90)
    image_ctk.configure(light_image = image)
    label_img.configure(image = image_ctk)

def do_BLUR():
    global image
    image = image.filter(ImageFilter.BLUR)
    image_ctk.configure(light_image = image)
    label_img.configure(image = image_ctk)
def do_BW():
    global image
    image = image.convert("L")
    image_ctk.configure(light_image = image)
    label_img.configure(image = image_ctk)

btn_rotate = CTkButton(set_fram, text = "повоорот на 90",command = do_Rotate)
btn_rotate.grid(row = 0, column = 0, padx = 10, pady = 10)

btn_blur = CTkButton(set_fram, text = "Блюр",command = do_BLUR)
btn_blur.grid(row = 0, column = 1, padx = 10, pady = 10)

btn_bw = CTkButton(set_fram, text = "Ч/Б",command = do_BW)
btn_bw.grid(row = 0, column = 2, padx = 10, pady = 10)

win.mainloop()

