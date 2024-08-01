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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    my_label.config(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
    my_label1.config(text="", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        my_label.config(text="Break", fg=RED, font=(FONT_NAME,40,"bold"))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        my_label.config(text="Break", fg=PINK, font=(FONT_NAME, 40, "bold"))
        count_down(short_break_sec)
    else:
        my_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 40, "bold"))
        count_down(work_sec)
    # while reps <= 4:
    #     count_down(work_sec)
    #     count_down(short_break_sec)
    #     reps += 1
    # count_down(long_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        my_label1.config(text=marks)
        # if reps % 2 == 0:
        # check_mark += "✔"
        # my_label1.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

my_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(row=0, column=1)

my_label1 = Label(fg=GREEN, bg=YELLOW)
my_label1.grid(row=3, column=1)

start_button = Button(text="Start", fg="black", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", fg="black", command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()
