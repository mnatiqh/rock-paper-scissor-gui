from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x500")

def computer():

    computer_choice = random.choice(["Rock" , "Paper" , "Scissors"])

    display_c = Label(root , text="Computer's choice: " , width=20 , bg="red" , fg="white")
    display_c.place(x=300 , y=60)

    computers = Label(root , text=f"{computer_choice}" , width=20 , bg="red" , fg="white")
    computers.place(x=300 , y=80)
    
    return computer_choice


def users(key):

    computer_key = computer()

    display = Label(root , text="User's choice: " , bg="light blue" , width=20)
    display.place(x=60 , y=60)

    if key == "Rock":
        rock = Label(root , text="Rock" , width=20 , bg="light blue")
        rock.place(x=60 , y=80)

    elif key == "Paper":
        paper = Label(root , text="Paper" , width=20 , bg="light blue")
        paper.place(x=60 , y=80)

    elif key == "Scissors":
        scissor = Label(root , text="Scissor" , width=20 , bg="light blue")
        scissor.place(x=60 , y=80)

    check_winner(key , computer_key)


def check_winner(user_key , computer_key):
    
    # print(f"user key is : {user_key}")
    # print(f"computer key is : {computer_key}")
    result = " "

    if user_key ==  computer_key :
       result = "Draw"

    elif user_key == "Rock" and computer_key == "Scissors":
        result = "User wins"

    elif user_key == "Rock" and computer_key == "Paper":
        result = "Computer wins"

  

    elif user_key == "Paper" and computer_key == "Scissors":
        result = "Computer wins"

    elif user_key == "Paper" and computer_key == "Rock":
        result = "User wins"

    
        
    elif user_key == "Scissors" and computer_key == "Rock":
        result = "Computer wins"

    elif user_key == "Scissors" and computer_key == "Paper":
        result = "User wins"

    else:
        result = "Invalid input"

    resultLabel = Label(root , text=f"{result}" , width=20 , bg="green" , fg="white" , font=("arial" , 15))
    resultLabel.place(x=150 , y=200)


rock_user = Button(root , text="Rock" , command=lambda:users("Rock") , width=10)
rock_user.place(x=10 , y=10)

paper_user = Button(root , text="Paper" , command=lambda:users("Paper") , width=10)
paper_user.place(x=90 , y=10)

scissor_user = Button(root , text="Scissors" ,  command=lambda:users("Scissors") , width=10)
scissor_user.place(x=170 , y=10)

branding = Label(root , text="Made by Natiq" , fg="orange")
branding.place(x=200 , y=450)

instructions = Label(root , text="Click rock, paper or scissors and try beat the bot!")
instructions.place(x=150 , y=400)


root.mainloop()


