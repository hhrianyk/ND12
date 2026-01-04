from PIL import Image
from customtkinter import *

image = Image.open("3.png")
#image.show()

print(image.format)
print(image.size)
print(image.mode)


window = CTk()
window.geometry("400x400")

ctk_img = CTkImage(image, size = (200,100))
label = CTkLabel(window, image = ctk_img, text="")
label.pack(padx = 10, pady = 10)

btn = CTkButton(window, image = ctk_img,text="Text")
btn.pack(padx = 10, pady = 10)

window.mainloop()