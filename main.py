from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    start_button.config(state="disabled")
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        count_down(work_sec)
    elif reps % 8 == 0:
        count_down(long_break_sec)
    else:
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
    global timer
    count_min = time // 60
    count_sec = time % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02}")
    if time > 0:
        if reps == 1:
            timer_label.config(text="Work", fg=GREEN)
        timer = window.after(1000, count_down, time - 1)
    else:
        start_button.config(state="normal")
        mark = ""
        for _ in range(reps // 2):
            mark += checkmark_symbol
        if reps % 8 == 0:
            mark = ""
        checkmarks.config(text=mark)
        if reps % 2 == 1 and reps % 7 != 0:
            canvas.itemconfig(timer_text, text=f"{SHORT_BREAK_MIN}:00")
            timer_label.config(text="Break", fg=PINK)
        elif reps % 2 == 1:
            timer_label.config(text="Break", fg=RED)
            canvas.itemconfig(timer_text, text=f"{LONG_BREAK_MIN}:00")
        else:
            timer_label.config(text="Work", fg=GREEN)
            canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=75, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=PINK, command=start_timer, state="normal")
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=PINK, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_symbol = '✓'
checkmarks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "bold"))
checkmarks.grid(row=3, column=1)

window.mainloop()
