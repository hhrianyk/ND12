from  customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")

        self.btn = CTkButton(self,text="Кнопка", width=50,height=50)
        self.btn.place(x=0,y=0)

        self.btn_adaptive()
    def btn_adaptive(self):
        self.btn.place(x=self.winfo_width()-self.btn.winfo_width(), y = self.winfo_height()-self.btn.winfo_height())
        self.after(10,self.btn_adaptive)


MainWindow().mainloop()