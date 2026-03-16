from tkinter import *
from PIL import Image, ImageTk
import random

# Initialize main window
root = Tk()
root.title("MATHS QUIZ")
root.geometry("600x400")
root.resizable(0, 0)

# Global variables
Dificult_Level = IntVar()
Attempts = IntVar(value=1)
question_count = 0
score = 0
correct_answer = None

# Frame switching function
def switch_frame(frame):
    frame.tkraise()

#Details Function
def Details():
    global instruct
    instruct = Toplevel(root)
    instruct.title("DETAILS")
    instruct.geometry("600x400")
    instruct.config(bg="Green")

    instruct_Label = Label(instruct,
                           font=("Hobo Normal", 15),
                           fg="white",
                           bg="Black",
                           text = "Math is beautiful. But sometimes, \n this can be hard to see, \n and even harder to convey to students \n who don’t — yet — share your passion. ")
    instruct_Label.pack(pady=20,padx=10)

# Start quiz function
def START_QUIZ(DIFICULT):
    global question_count, score
    question_count = 0
    score = 0
    Dificult_Level.set(DIFICULT)
    CREATE_QUESTION()
    switch_frame(Quiz_Frame3)

# Create question function
def CREATE_QUESTION():
    global correct_answer, question_count
    if question_count < 10:
        if Dificult_Level.get() == 1:
            min_value, max_value = (1, 10)
        elif Dificult_Level.get() == 2:
            min_value, max_value = (10, 99)
        elif Dificult_Level.get() == 3:
            min_value, max_value = (100, 999)
        else:
            return

        num1 = random.randint(min_value, max_value)
        num2 = random.randint(min_value, max_value)
        operation = random.choice(["+", "-"])

        if operation == "+":
            correct_answer = num1 + num2
        else:
            correct_answer = num1 - num2

        Quiz_Label.config(text=f"{num1} {operation} {num2}")
    else:
        Display_Result()

# Clear answer function
def CLEAR_ANSWER():
    global question_count, score
    try:
        user_input = int(Quiz_Answer.get())
        if user_input == correct_answer:
            Quiz_Feedback.config(text="THAT'S CORRECT", fg="Green")
            if Attempts.get() == 1:
                score += 10
            question_count += 1
            Attempts.set(1)
            Quiz_Answer.delete(0, END)
            CREATE_QUESTION()
        else:
            if Attempts.get() == 1:
                Quiz_Feedback.config(text="THAT'S NOT CORRECT, TRY AGAIN", fg="Red")
                Attempts.set(2)
            else:
                Quiz_Feedback.config(text="SORRY, MOVING TO NEXT QUESTION", fg="Red")
                question_count += 1
                Attempts.set(1)
                CREATE_QUESTION()
    except ValueError:
        Quiz_Feedback.config(text="PLEASE ENTER A VALID NUMBER", fg="Blue")

# Display result function
def Display_Result():
    switch_frame(Result_Frame4)
    Quiz_Results.config(text=f"FINAL SCORE: {score}/100")

    if score > 90:
        rank = "A+"
    elif score > 75:
        rank = "A"
    elif score > 60:
        rank = "B"
    elif score > 50:
        rank = "C"
    else:
        rank = "F"

    Quiz_Score.config(text=f"RANK: {rank}")

# Restart quiz function
def Again_Quiz():
    switch_frame(Home_Frame)

# Create frames
Home_Frame = Frame(root)
Home_Frame.place(relwidth=1, relheight=1)

Menu_Frame2 = Frame(root)
Menu_Frame2.place(relwidth=1, relheight=1)

Quiz_Frame3 = Frame(root)
Quiz_Frame3.place(relwidth=1, relheight=1)

Result_Frame4 = Frame(root)
Result_Frame4.place(relwidth=1, relheight=1)

# Load images with exception handling
def load_image(path):
    try:
        img = Image.open(path)
        img = img.resize((600, 400))
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

Background_Home = load_image("A1 - Skills Portfolio/Exercise 1 Maths Quiz/1.png")
Background_Home2 = load_image("A1 - Skills Portfolio/Exercise 1 Maths Quiz/2.png")
Background_Home3 = load_image("A1 - Skills Portfolio/Exercise 1 Maths Quiz/3.png")
Background_Home4 = load_image("A1 - Skills Portfolio/Exercise 1 Maths Quiz/4.png")

# Home Frame
Background_Label = Label(Home_Frame, image=Background_Home)
Background_Label.place(relwidth=1, relheight=1)

I_BUTTON = Button(
    Home_Frame,
    text="DETAILS",
    font=("Abril Fatface", 12),
    bg="black",
    fg="White",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=Details
)
I_BUTTON.place(x=146, y=280)

C_BUTTON = Button(
    Home_Frame,
    text="PLAY",
    font=("Abril Fatface", 12),
    bg="black",
    fg="White",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=lambda: switch_frame(Menu_Frame2)
)
C_BUTTON.place(x=384, y=278)

# Menu Frame
Background_Label2 = Label(Menu_Frame2, image=Background_Home2)
Background_Label2.place(relwidth=1, relheight=1)

Quiz_Name = Label(
    Menu_Frame2,
    text="DIFFICULTY",
    font=("Abril Fatface", 28),
    fg="black",
    bg="#d9d9d9"
)
Quiz_Name.place(x=200, y=68)

Quiz_Name2 = Label(
    Menu_Frame2,
    text="LEVEL",
    font=("Abril Fatface", 28),
    fg="black",
    bg="#d9d9d9"
)
Quiz_Name2.place(x=250, y=110)

M_BUTTON1 = Button(
    Menu_Frame2,
    text="1. EASY",
    bg="Black",
    font=("Abril Fatface", 12),
    fg="White",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=lambda: START_QUIZ(1)
)
M_BUTTON1.place(x=268, y=175)

M_BUTTON2 = Button(
    Menu_Frame2,
    text="2. MODERATE",
    bg="Black",
    font=("Abril Fatface", 12),
    fg="White",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=lambda: START_QUIZ(2)
)
M_BUTTON2.place(x=246, y=224)

M_BUTTON3 = Button(
    Menu_Frame2,
    text="3. ADVANCED",
    bg="Black",
    font=("Abril Fatface", 12),
    fg="White",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=lambda: START_QUIZ(3)
)
M_BUTTON3.place(x=246, y=275)

B_BUTTON = Button(
    Menu_Frame2,
    text="BACK",
    bg="Black",
    font=("Abril Fatface", 12),
    fg="White",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=lambda: switch_frame(Home_Frame)
)
B_BUTTON.place(x=270, y=318)

# Quiz Frame
Background_Label3 = Label(Quiz_Frame3, image=Background_Home3)
Background_Label3.place(relwidth=1, relheight=1)

Quiz_Label = Label(
    Quiz_Frame3,
    text="",
    font=("Abril Fatface", 12),
    bg="White",
    fg="Black",
    width=14
)
Quiz_Label.place(x=199, y=100)

Quiz_Answer = Entry(
    Quiz_Frame3,
    font=("Abril Fatface", 12),
    width=10,
    borderwidth=0
)
Quiz_Answer.place(x=220, y=190)

Quiz_Feedback = Label(
    Quiz_Frame3,
    text="",
    font=("Abril Fatface", 12),
    bg="White",
    fg="Black"
)
Quiz_Feedback.place(x=150, y=148)

S_BUTTON = Button(
    Quiz_Frame3,
    text="SUBMIT",
    font=("Abril Fatface", 12),
    bg="White",
    fg="Black",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=CLEAR_ANSWER
)
S_BUTTON.place(x=180, y=250)

N_BUTTON = Button(
    Quiz_Frame3,
    text="NEXT",
    font=("Abril Fatface", 12),
    bg="White",
    fg="Black",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=CREATE_QUESTION
)
N_BUTTON.place(x=300, y=250)

B_BUTTON2 = Button(
    Quiz_Frame3,
    text="BACK",
    font=("Abril Fatface", 12),
    bg="White",
    fg="Black",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=lambda: switch_frame(Menu_Frame2)
)
B_BUTTON2.place(x=240, y=300)

# Result Frame
Background_Label4 = Label(Result_Frame4, image=Background_Home4)
Background_Label4.place(relwidth=1, relheight=1)

Quiz_Results = Label(
    Result_Frame4,
    text="",
    font=("Abril Fatface", 20),
    bg="White",
    fg="Black"
)
Quiz_Results.place(x=180, y=150)

Quiz_Score = Label(
    Result_Frame4,
    text="",
    font=("Abril Fatface", 20),
    bg="White",
    fg="Black"
)
Quiz_Score.place(x=180, y=200)

R_BUTTON = Button(
    Result_Frame4,
    text="RETRY",
    font=("Abril Fatface", 12),
    bg="White",
    fg="Black",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=Again_Quiz
)
R_BUTTON.place(x=180, y=300)

Q_BUTTON = Button(
    Result_Frame4,
    text="QUIT",
    font=("Abril Fatface", 12),
    bg="White",
    fg="Black",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=root.quit
)
Q_BUTTON.place(x=300, y=300)

# Start main loop
switch_frame(Home_Frame)
root.mainloop()