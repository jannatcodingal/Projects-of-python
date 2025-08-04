from tkinter import Tk  # noqa: F403
from random import randint  # noqa: F403
from tkinter import ttk, Label, Button, PhotoImage
from PIL import Image, ImageTk  # Add this import for image handling
root = Tk()
root.title("Rock Paper Scissors Game! ")
root.geometry("400x400")
root.config(bg="white")
def load_and_resize(path, size=(100, 100)):
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)
rock = load_and_resize("rock.png")
paper = load_and_resize("paper.png")
scissors = load_and_resize("scissors.png")
image_list = [rock, paper, scissors]
pick_number = randint(0, 2)
image_label = Label(root, image=image_list[pick_number])
image_label.pack(pady=20)

def spin(): 
    pick_number = randint(0, 2)
    image_label.config(image=image_list[pick_number])
    if user_choice.get() == "Rock":
        user_choice.set("Rock")  # Correct way to set the value of a Combobox
        user_value = 0
    elif user_choice.get() == "Paper":
        user_choice.set("Paper")  # Correct way to set the value of a Combobox
        user_value = 1
    elif user_choice.get() == "Scissors":
        user_choice.set("Scissors")  # Correct way to set the value of a Combobox
        user_value = 2
    else:
        user_value = -1  # Handle potential errors if the value isn't one of the expected ones

    if user_value == 0:
        if pick_number == 0:  # rock
            win_lose_label.config(text="It's a Tie! Spin again!")
        elif pick_number == 1:  # paper
            win_lose_label.config(text="You Lose! Paper beats Rock!")
        elif pick_number == 2:  # scissors
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


user_choice = ttk.Combobox(root,values=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=10)
spin_button = Button(root, text="Spin", command=spin)
spin_button.pack(pady=10)
win_lose_label = Label(root, text="")
win_lose_label.pack(pady=50)
root.mainloop()