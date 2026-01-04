from random import choice

from customtkinter import *

diff_password = 4
def generate_password():

   chars = [char for char in 'qwertyuiopasdfghjklzxcvbnm']
   spec_chars = [char for char in '!@#$%^&*()_+']
   available_value = []
   result = ''
   if l_chars_btn.get():
       available_value += chars
   if up_chars_btn.get():
       available_value += [char.upper() for char in chars]
   if spec_chars_btn.get():
       available_value += spec_chars
   if num_chars_btn.get():
       available_value += [str(i) for i in range(0, 10)]


   for i in range(diff_password):
       result += choice(available_value)
   password_entry.delete(0, 'end')
   password_entry.insert(0, result)


win = CTk()
win.geometry("400x400")
win.title("Password")
win.maxsize(400, 400)
set_default_color_theme("green")
set_appearance_mode("dark")

font = ("verdana", 30, "bold")

password_entry = CTkEntry(win, width=200)
password_entry.grid(row=0, column=0, padx=10, pady=10)

btn_generait = CTkButton(win, text ="Generate",command=generate_password)
btn_generait.grid(row=0, column=1, padx=10, pady=10)

settings_fram = CTkFrame(win,width = 200, fg_color = "gray")
settings_fram.grid(row=1, column=0, padx=10, pady=10)

l_chars_btn = CTkCheckBox(settings_fram, text = "Малі літери",width = 200)
l_chars_btn.pack(pady = 10)

up_chars_btn = CTkCheckBox(settings_fram, text = "Великі літери",width = 200)
up_chars_btn.pack(pady = 10)


spec_chars_btn = CTkCheckBox(settings_fram, text = "Спец символи",width = 200)
spec_chars_btn.pack(pady = 10)

num_chars_btn = CTkCheckBox(settings_fram, text = "Номери символи",width = 200)
num_chars_btn.pack(pady = 10)


win.mainloop()