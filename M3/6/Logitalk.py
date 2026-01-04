from socket import socket, AF_INET, SOCK_STREAM

from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("LogiTalk")
        self.label = None

        # --- БОКОВЕ МЕНЮ ---
        self.menu_frame = CTkFrame(self, width=30, height=300,fg_color='purple')
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x= 0,y = 0)

        self.is_show_menu = False
        self.speed_animate_menu = -5

        self.btn  = CTkButton(self, text="▶️", command=self.toggle_show_menu,width=30, fg_color="purple" )
        self.btn.place(x=0,y=0)
        # --- ОСНОВНА ОБЛАСТЬ ЧАТУ ---

        self.chat_field = CTkScrollableFrame(self, fg_color="#ffa6ff")
        self.chat_field.place(x=0, y=0)

        self.message_entry = CTkEntry(self, placeholder_text='Введіть повідомлення:', height=40)  # Поле вводу
        self.message_entry.place(x=0, y=0)

        self.send_button = CTkButton(self, text='>', width=50, height=40)  # Кнопка «Надіслати»
        self.send_button.place(x=0, y=0)

        # Запускаємо адаптивне компонування
        self.adaptive_ui()

        self.username = "GEORGE"

        try:
            self.sock = socket(AF_INET,SOCK_STREAM)
            self.sock.connect(("localhost",8080))
            hello = f"TEXT@{self.username}@[SYSTEM] {self.username} приєднався(лась) до чату!\n"
            self.sock.send(hello.encode('utf-8'))

        except Exception as e:
            self.add_message(f"Не вдалося підключитись до сервера {e}")


        self.add_message("Початок роботи")


    # --- ЛОГІКА ПЕРЕМИКАННЯ МЕНЮ ---
    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animate_menu *= -1
            self.btn.configure(text = '▶️')
            self.show_menu()

            if self.label :
                self.label.destroy()
            if getattr(self, 'entry', None):
                self.entry.destroy()
            if getattr(self, 'save_button', None):
                self.save_button.destroy()

        else:
            self.is_show_menu = True
            self.speed_animate_menu *= -1
            self.btn.configure(text='◀️')
            self.show_menu()

            self.label = CTkLabel(self.menu_frame, text='Імʼя')
            self.label.pack(pady=30)
            self.entry = CTkEntry(self.menu_frame)
            self.entry.pack()
            self.save_button = CTkButton(self.menu_frame, text="Зберегти")
            self.save_button.pack()

    # --- АНІМАЦІЯ ВІДКРИТТЯ/ЗАКРИТТЯ МЕНЮ ---
    def show_menu(self):
        self.menu_frame.configure(width=self.menu_frame.winfo_width() + self.speed_animate_menu)

        if self.menu_frame.winfo_width() <= 200 and self.is_show_menu:
            self.after(10, self.show_menu)

        if self.menu_frame.winfo_width() >= 40 and self.is_show_menu == False:
            self.after(10, self.show_menu)

    # --- АДАПТИВНЕ КОМПОНУВАННЯ ---
    def adaptive_ui(self):
        # Висота меню завжди дорівнює висоті вікна
        self.menu_frame.configure(height=self.winfo_height())
        self.chat_field.place(x=self.menu_frame.winfo_width())
        self.chat_field.configure(
            width=self.winfo_width() - self.menu_frame.winfo_width() - 20,
            height=self.winfo_height() - 40
        )

        self.send_button.place(x=self.winfo_width() - 50, y=self.winfo_height() - 40)
        self.message_entry.place(x=self.menu_frame.winfo_width(), y=self.send_button.winfo_y())

        self.message_entry.configure(
            width=self.winfo_width() - self.menu_frame.winfo_width() - self.send_button.winfo_width()
        )

        self.after(100, self.adaptive_ui)

    # показ повідомлення або зображення
    def add_message(self, message, img=None):
        message_frame = CTkFrame(self.chat_field, fg_color="grey")
        message_frame.pack(pady=5, anchor="w")
        wrapleng_size = self.winfo_width()-self.chat_field.winfo_width()-40

        if not img:
            CTkLabel(message_frame,text=message,wraplength=wrapleng_size,
                     text_color='white',justify='left').pack(padx =10,pady=10)
        else:
            CTkLabel(message_frame, text=message, wraplength=wrapleng_size,
                     text_color='white', image=img, compound='top',
                     justify='left').pack(padx=10, pady=5)

# --- ЗАПУСК ---
MainWindow().mainloop()
