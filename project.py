from tkinter import Tk
from random import randint
from tkinter import ttk, Label, Button, PhotoImage

root = Tk()
root.title("Rock Paper Scissors Game! ")
root.geometry("400x400")
root.config(bg="white")

# Load images directly with PhotoImage
rock = PhotoImage(file="")
paper = PhotoImage(file="")
scissors = PhotoImage(file="")
image_list = [rock, paper, scissors]

pick_number = randint(0, 2)
image_label = Label(root, image=image_list[pick_number])
image_label.pack(pady=20)

def spin():
    pick_number = randint(0, 2)
    image_label.config(image=image_list[pick_number])
    if user_choice.get() == "Rock":
        user_choice.set("Rock")
        user_value = 0
    elif user_choice.get() == "Paper":
        user_choice.set("Paper")
        user_value = 1
    elif user_choice.get() == "Scissors":
        user_choice.set("Scissors")
        user_value = 2
    else:
        user_value = -1

    if user_value == 0:
        if pick_number == 0:
            win_lose_label.config(text="It's a Tie! Spin again!")
        elif pick_number == 1:
            win_lose_label.config(text="You Lose! Paper beats Rock!")
        elif pick_number == 2:
            win_lose_label.config(text="You Win! Rock beats Scissors!")
    if user_value == 1:
        if pick_number == 1:
            win_lose_label.config(text="It's a Tie! Spin again!")
        elif pick_number == 0:
            win_lose_label.config(text=" Paper covers Rock! You win.")
        elif pick_number == 2:
            win_lose_label.config(text="scissors cuts paper! You lose")
    if user_value == 2:
        if pick_number == 2:
            win_lose_label.config(text="It's a Tie! Spin again!")
        elif pick_number == 0:
            win_lose_label.config(text="rock smashes scissors! You lose")
        elif pick_number == 1:
            win_lose_label.config(text="scissors cuts paper! You win")

user_choice = ttk.Combobox(root, values=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=10)
spin_button = Button(root, text="Spin", command=spin)
spin_button.pack(pady=10)
win_lose_label = Label(root, text="")
win_lose_label.pack(pady=50)
root.mainloop()