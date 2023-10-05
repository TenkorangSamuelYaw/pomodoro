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
# ---------------------------- GLOBAL VARIABLES ------------------------------- #
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    #  Reset the timer.
    canvas.itemconfig(timer_text, text="00:00")
    #  Reset the title label.
    title_label.config(text="Timer")
    #  Reset the check marks.
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    #  On the 8th repetition.
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)

    #  On the 2nd/4th/6th repetition.
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)

    # On the 1st/3rd/5th/7th repetition.
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"  # Dynamic typing, revisit this lines again.
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Recursion.
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks, font=("Courier", 16, "normal"))
# ---------------------------- UI SETUP ------------------------------- #


#  Create a new window
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)
#  Create a new canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # This line helps to get the right data type the
# keyword argument in the create_image method wants
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#  Create the first label(timer)
title_label = Label(text="Timer", font=("Courier", 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)
#  Create the first button(start)
start_button = Button(text="Start", font=("Courier", 16, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
#  Create the second button(reset)
reset_button = Button(text="Reset", font=("Courier", 16, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
#  Create the second label(checkmark)
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
