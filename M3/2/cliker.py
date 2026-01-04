from customtkinter import *

score = 0

def click():
    global score
    score = score + upgrade
    text.configure(text = "Score: " +str(score))
upgrade = 1
def clickUpgrade():
    global upgrade, score
    if score > 10:
        upgrade = upgrade + 1
        score -= 10
        text.configure(text="Score: " + str(score))
win = CTk()
win.geometry("400x400")
win.title("Clicker")

font = ("verdana", 30, "bold")
text = CTkLabel(win, text = "0", font=font )
text.place(x = 0, y = 0)

btn = CTkButton(win, text = "Click me", width=50, height=50, font=font,   command=click)
btn.place(x = 100, y = 100)
btnUPG = CTkButton(win, text = "Upgrade", width=50, height=50, font=font,  command=clickUpgrade)
btnUPG.place(x = 200, y = 300)




win.mainloop()