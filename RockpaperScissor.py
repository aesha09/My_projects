import random
from tkinter import *

# Create the main window
root = Tk()
root.geometry("300x300")
root.title("Rock Paper Scissor Game")

# Computer value mapping
computer_value = {0: "Rock", 1: "Paper", 2: "Scissor"}

# Reset the game
def reset_game():
    for button in [b1, b2, b3]:
        button["state"] = "normal"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

# Disable all buttons
def disable_buttons():
    for button in [b1, b2, b3]:
        button["state"] = "disabled"

# Game logic
def play_game(player_choice):
    c_v = computer_value[random.randint(0, 2)]
    if c_v == player_choice:
        match_result = "Match Draw"
    elif (player_choice == "Rock" and c_v == "Scissor") or \
         (player_choice == "Paper" and c_v == "Rock") or \
         (player_choice == "Scissor" and c_v == "Paper"):
        match_result = "Ugh You Win"
    else:
        match_result = "Ha Loser! I win"
    
    l4.config(text=match_result)
    l1.config(text=player_choice)
    l3.config(text=c_v)
    disable_buttons()

# UI Components
Label(root, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame, text="Player", font=10)
l2 = Label(frame, text="VS", font="normal 10 bold")
l3 = Label(frame, text="Computer", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)

l4 = Label(root, text="", font="normal 20 bold", bg="white", width=15, borderwidth=2, relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

# Buttons for player choices
b1 = Button(frame1, text="Rock", font=10, width=7, command=lambda: play_game("Rock"))
b2 = Button(frame1, text="Paper", font=10, width=7, command=lambda: play_game("Paper"))
b3 = Button(frame1, text="Scissor", font=10, width=7, command=lambda: play_game("Scissor"))

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)

# Reset button
Button(root, text="Reset Game", font=10, fg="red", bg="black", command=reset_game).pack(pady=20)

# Run the main loop
root.mainloop()
