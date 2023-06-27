import random
import sys
from termcolor import cprint, colored

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") to print the following characters

# ● ┌ ─ ┐ │ └ ┘


"┌──────────┐"
"│          │"
"│          │"
"│          │"
"└──────────┘"


dice_art = {
    1:("┌──────────┐",
       "│          │", 
       "│    ●     │",
       "│          │",
       "└──────────┘" ),

    2:("┌──────────┐",
       "│ ●        │", 
       "│          │",
       "│        ● │",
       "└──────────┘" ), 

    3:("┌──────────┐",
       "│   ●      │", 
       "│     ●    │",
       "│        ● │",
       "└──────────┘" ), 


    4:("┌──────────┐",
       "│ ●      ● │", 
       "│          │",
       "│ ●      ● │",
       "└──────────┘" ),  

    5:("┌──────────┐",
       "│ ●      ● │", 
       "│     ●    │",
       "│ ●      ● │",
       "└──────────┘" ),   

    6:("┌──────────┐",
       "│ ●      ● │", 
       "│ ●      ● │",
       "│ ●      ● │",
       "└──────────┘" )    
     
}



dice = []


total = 0


num_of_dice = int(input("How many dice? :  "))




for die in range(num_of_dice):
    dice.append(random.randint(1,6))    #Randomaly chooses the shape of the die and appends into
                                        #list dice



#for die in range(num_of_dice):

#    for line in dice_art.get(dice[die]): To print the dice vertically

 #       print(line)

for line in range(5):                                      #To print the dice
    for die in dice:                                       #horizantlly
        print(colored(dice_art.get(die)[line],"blue"),end="")
    print()  # to print a new line  


for die in dice:   # to sum up the values of the dice and print it

    total += die

print(colored(f"total: {total}", "green","on_yellow"))