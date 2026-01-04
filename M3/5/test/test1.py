from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x300')  # Стартовий розмір вікна
        self.label = None  # Майбутній віджет у меню (підпис)

        # --- БОКОВЕ МЕНЮ ---
        self.menu_frame = CTkFrame(self, width=30, height=300)  # Фрейм для меню зліва
        self.menu_frame.pack_propagate(False)  # Забороняємо авто-розтяг
        self.menu_frame.place(x=0, y=0)  # Фіксуємо у верхньому лівому куті

        self.is_show_menu = False  # Стан меню: відкрите чи закрите
        self.speed_animate_menu = -5  # Крок анімації (px за тик, знак міняється)

        # Кнопка для відкриття/закриття меню
        self.btn = CTkButton(self, text='▶️', command=self.toggle_show_menu, width=30)
        self.btn.place(x=0, y=0)

        # --- ОСНОВНА ОБЛАСТЬ ЧАТУ ---
        self.chat_field = CTkScrollableFrame(self)  # Прокручуваний блок (чат)
        self.chat_field.place(x=0, y=0)

        self.message_entry = CTkEntry(self, placeholder_text='Введіть повідомлення:', height=40)  # Поле вводу
        self.message_entry.place(x=0, y=0)

        self.send_button = CTkButton(self, text='>', width=50, height=40)  # Кнопка «Надіслати»
        self.send_button.place(x=0, y=0)

        # Запускаємо адаптивне компонування
        self.adaptive_ui()


    # --- ЛОГІКА ПЕРЕМИКАННЯ МЕНЮ ---
    def toggle_show_menu(self):
        if self.is_show_menu:
            # Якщо меню було відкрите → закриваємо
            self.is_show_menu = False
            self.speed_animate_menu *= -1  # Міняємо напрям анімації
            self.btn.configure(text='▶️')  # Змінюємо іконку кнопки
            self.show_menu()
        else:
            # Якщо меню було закрите → відкриваємо
            self.is_show_menu = True
            self.speed_animate_menu *= -1
            self.btn.configure(text='◀️')
            self.show_menu()

            # Створюємо внутрішні віджети меню
            self.label = CTkLabel(self.menu_frame, text='Імʼя')
            self.label.pack(pady=30)
            self.entry = CTkEntry(self.menu_frame)
            self.entry.pack()

    # --- АНІМАЦІЯ ВІДКРИТТЯ/ЗАКРИТТЯ МЕНЮ ---
    def show_menu(self):
        # Змінюємо ширину меню
        self.menu_frame.configure(width=self.menu_frame.winfo_width() + self.speed_animate_menu)

        # Продовжуємо анімацію при відкритті (до 200px)
        if not self.menu_frame.winfo_width() >= 200 and self.is_show_menu:
            self.after(10, self.show_menu)

        # Продовжуємо анімацію при закритті (поки більше 40px)
        elif self.menu_frame.winfo_width() >= 40 and not self.is_show_menu:
            self.after(10, self.show_menu)
            # Видаляємо внутрішні віджети, коли меню згортається
            if self.label and self.entry:
                self.label.destroy()
                self.entry.destroy()

    # --- АДАПТИВНЕ КОМПОНУВАННЯ ---
    def adaptive_ui(self):
        # Висота меню завжди дорівнює висоті вікна
        self.menu_frame.configure(height=self.winfo_height())

        # Поле чату займає простір праворуч від меню
        self.chat_field.place(x=self.menu_frame.winfo_width())
        self.chat_field.configure(
            width=self.winfo_width() - self.menu_frame.winfo_width() - 20,
            height=self.winfo_height() - 40
        )

        # Кнопка "Надіслати" фіксується у правому нижньому куті
        self.send_button.place(x=self.winfo_width() - 50, y=self.winfo_height() - 40)

        # Поле вводу займає простір між меню і кнопкою
        self.message_entry.place(x=self.menu_frame.winfo_width(), y=self.send_button.winfo_y())
        self.message_entry.configure(
            width=self.winfo_width() - self.menu_frame.winfo_width() - self.send_button.winfo_width()
        )

        # Оновлюємо кожні 50 мс (щоб реагувати на зміну розміру вікна)
        self.after(50, self.adaptive_ui)


# --- ЗАПУСК ---
win = MainWindow()
win.mainloop()
