from  customtkinter import *
from PIL import   Image

class Menu(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('700x400')
        self.title("Вихід")
        self.resizable(True,False)

        #--------  Ліва частина --------
        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side = 'left', fill = "both")

        img = CTkImage(light_image = Image.open("bg.png"),size = (450,400))
        self.img_label = CTkLabel(self.left_frame, image = img, text = "WELCOME", font = ("Helvetica", 60, "bold"), text_color = "white" )
        self.img_label.pack()

        # --------  Права частина --------

        self.right_fram = CTkFrame(self, fg_color="purple")
        self.right_fram.pack_propagate(False)
        self.right_fram.pack(side="right", fill="both", expand="True")

        CTkLabel(self.right_fram, text="LogiTalk", font = ("Helvetica", 30, "bold"), text_color="white").pack(pady=60)
        self.name_entry = CTkEntry(self.right_fram, placeholder_text='☻ ім`я',
                                   height=45, font = ("Helvetica", 30, "bold"), corner_radius=25, fg_color='#eae6ff',
                                   border_color='#eae6ff',
                                   text_color='#6753cc', placeholder_text_color='#6753cc')
        self.name_entry.pack(fill='x', padx=10)

Menu().mainloop()