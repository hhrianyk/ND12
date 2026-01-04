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


    # --- ЛОГІКА ПЕРЕМИКАННЯ МЕНЮ ---
    def toggle_show_menu(self):
        pass

    # --- АНІМАЦІЯ ВІДКРИТТЯ/ЗАКРИТТЯ МЕНЮ ---
    def show_menu(self):
        pass

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


# --- ЗАПУСК ---
MainWindow().mainloop()
