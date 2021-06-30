from tkinter import *
import math
from typing import Counter 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(time_lap, text = "00:00")
    label.config(text="timer")
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN  * 60
    shork_break_min = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60 

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg = RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60 
    if count_sec < 10:
        count_sec = F"0{count_sec}"


    canvas.itemconfig(time_lap, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer

        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks  += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


label = Label(text="Timer", fg=GREEN, bg = YELLOW, font=(FONT_NAME, 50))
label.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_png)
time_lap = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)



start_button = Button(text="Start", highlightthickness=0, command = start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command = timer_reset)
reset_button.grid(column=2, row=2)

check_marks = Label( bg = YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)




window.mainloop()
