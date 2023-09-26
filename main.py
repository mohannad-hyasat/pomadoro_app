from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
maintimer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    global REPS
    REPS = 0
    window.after_cancel(maintimer)
    title.config(text="Timer")
    checkMark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global REPS
    REPS +=1
    wsec = WORK_MIN * 60
    sbsec = SHORT_BREAK_MIN *60
    lbsec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        countdown(lbsec)
        Label.config(title, text='Break', fg=RED)
    elif REPS % 2 == 0:
        countdown(sbsec)
        Label.config(title, text='Break', fg=PINK)
    else:
        countdown(wsec)
        Label.config(title, text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(n):
    global maintimer
    min = math.floor(n/60)
    sec = n%60
    if sec < 10:
        sec= f"0{sec}"
    if min<10 :
        min = f"0{min}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if n>0:
        maintimer = window.after(1000, countdown, n - 1)
    else:
        startTimer()
        marks = ""
        sessions = math.floor(REPS/2)
        for _ in range(sessions):
            marks += "✔"
        checkMark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomadoro")
window.config(padx=100, pady=50, bg=YELLOW)


title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)


start = Button(text="Start", command=startTimer)
start.grid(column=0, row=2)
reset = Button(text="Reset", command= resetTimer)
reset.grid(column=2, row=2)

checkMark = Label(fg=GREEN, bg=YELLOW)
checkMark.grid(column=1, row=3)













window.mainloop()