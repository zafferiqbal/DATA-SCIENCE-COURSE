import tkinter as tk
import random

def play(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    player_label.config(text=f"You: {player_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")

    if player_choice == computer_choice:
        result = "It's a Draw!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=result)

def reset():
    player_label.config(text="You: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="Choose Rock, Paper or Scissors")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Make your choice", font=("Arial", 14))
instruction_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12),
                        command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12),
                         command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12),
                             command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

player_label = tk.Label(root, text="You: ", font=("Arial", 14))
player_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 14))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Choose Rock, Paper or Scissors",
                        font=("Arial", 16, "bold"))
result_label.pack(pady=20)

reset_button = tk.Button(root, text="Reset", width=12, font=("Arial", 12), command=reset)
reset_button.pack(pady=10)

root.mainloop()