from customtkinter import *

window = CTk()
window.geometry("300x400")
window.title("LOGIKA")
window.configure(fg_color="#123456")

text = CTkLabel(window, text = "HEllo, LOGIKA", text_color="white")
text.pack(pady = 50)

btn = CTkButton(window, text="LOGIKA", fg_color="purple")
btn.pack(pady = 50)
btn2 = CTkButton(window, text="LOGIKA2")
btn2.pack()

window.mainloop()