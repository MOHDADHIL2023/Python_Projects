from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Initialize the main Tkinter window
root = Tk()
root.title("ALEXA TELLS US JOKES APP")
root.geometry("600x400")
root.resizable(0, 0)

# Function to switch between frames
def switch_frame(frame):
    frame.tkraise()

# Function to load jokes from the file
def Load_Jokes():
    try:
        with open("A1 - Skills Portfolio/Exercise 2 Jokes/randomJokes.txt", "r") as file:
            jokes = file.readlines()
        return [joke.strip().split("?") for joke in jokes]
    except FileNotFoundError:
        messagebox.showerror("Error", "Jokes file not found.")
        return []

# Function to show a random joke setup
def Show_Jokes():
    global Correct_Jokes
    if Jokes:
        Correct_Jokes = random.choice(Jokes)
        Setup_Label.config(text=Correct_Jokes[0] + "?")
        Press_Label.config(text="")  # Clear the punchline box
    else:
        Setup_Label.config(text="No jokes available.")
        Press_Label.config(text="")

# Function to display the punchline
def Show_Press():
    if Correct_Jokes:
        Press_Label.config(text=Correct_Jokes[1])
    else:
        Press_Label.config(text="No joke selected.")

# Load jokes
Jokes = Load_Jokes()
Correct_Jokes = None

# Home Frame
Home_Frame = Frame(root)
Home_Frame.place(relheight=1, relwidth=1)

Background_Home = Image.open("A1 - Skills Portfolio/Exercise 2 Jokes/1.png")
Background_Home = Background_Home.resize((600, 400))
Background_Home = ImageTk.PhotoImage(Background_Home)

Home_Label = Label(Home_Frame, image=Background_Home)
Home_Label.place(relwidth=1, relheight=1)

# Task Frame
Task_Frame = Frame(root)
Task_Frame.place(relwidth=1, relheight=1)

Background_Task = Image.open("A1 - Skills Portfolio/Exercise 2 Jokes/2.png")
Background_Task = Background_Task.resize((600, 400))
Background_Task = ImageTk.PhotoImage(Background_Task)

Task_Label = Label(Task_Frame, image=Background_Task)
Task_Label.place(relwidth=1, relheight=1)

# Home Frame Widgets
Start_Button = Button(
    Home_Frame,
    text="START",
    font=("Abril Fatface", 15),
    fg="White",
    bg="Black",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Blue",
    command=lambda: switch_frame(Task_Frame)
)
Start_Button.place(x=272, y=246)

# Task Frame Widgets
ALexa_Button = Button(
    Task_Frame,
    text="GIVE SOME JOKES",
    font=("Abril Fatface", 12),
    fg="White",
    bg="Black",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Green",
    command=Show_Jokes
)
ALexa_Button.place(x=64, y=290)

Press_Button = Button(
    Task_Frame,
    text="PRESS",
    font=("Abril Fatface", 15),
    fg="White",
    bg="Black",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Green",
    command=Show_Press
)
Press_Button.place(x=284, y=287)

Setup_Box = Frame(Task_Frame, bg="Black", bd=2, relief="solid")
Setup_Box.place(x=50, y=50, width=500, height=100)

Setup_Label = Label(Setup_Box, text="", font=("Abril Fatface", 15), fg="White", bg="Black")
Setup_Label.place(relwidth=1, relheight=1)

Press_Box = Frame(Task_Frame, bg="Black", bd=2, relief="solid")
Press_Box.place(x=50, y=120, width=500, height=50)

Press_Label = Label(Press_Box, text="", font=("Abril Fatface", 15), fg="White", bg="Black")
Press_Label.place(relwidth=1, relheight=1)

Exit_Button = Button(
    Task_Frame,
    text="EXIT",
    font=("Abril Fatface", 15),
    fg="White",
    bg="Black",
    borderwidth=0,
    activebackground="Black",
    activeforeground="Green",
    command=root.destroy
)
Exit_Button.place(x=456, y=286)

# Start with the Home Frame
switch_frame(Home_Frame)

# Run the main loop
root.mainloop()