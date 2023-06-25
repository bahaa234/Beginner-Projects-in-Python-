from ast import FloorDiv  # result of to input variables division
from random import randint #randomly selcet strings characters
import copy #copies all the matlibs game together with input

import sys
from termcolor import cprint, colored # used to color, and style the text








print("Welcome to Madlibs Game!")

playing = input(  "lets play, shall we\n "  )

if playing.lower() != 'yes':
    
    text_for_end= colored("We are so sad for that!!!".upper(),"white","on_blue",attrs=["bold"])
    print(text_for_end)
    quit()  #if the answer is no,then the program gonna terminate!

print("Okay, let's play the game: \n ")



noun1 = input("Enter Your Name: ").upper()
noun1 = colored(noun1,"red",attrs=['bold']) # the form of the function colored("text", "color in lowercase","highlight on_color,you wish", style of the text, attrs["style"](bold,italic, etc..))

noun2 = input("Enter your friend's name: ")
noun2 = colored(noun2,"green",attrs=['bold'])

noun3 = input("Enter another friend's name:")
noun3 = colored(noun3,"blue",attrs=['bold'])

place = input("Enter a place name: ")
place = colored(place,"yellow","on_green")

adjecvtive1 = input("Enter an Adjective: ")
adjecvtive1 = colored(adjecvtive1,"white",attrs=["reverse"])

adjective2 = input("Enter another Adjective: ")
adjective2  = colored(adjective2 ,"grey",attrs=["reverse"])

adjective3 = input("Enter on more Adjective: ")
adjective3 = colored(adjective3 ,"magenta",attrs=["reverse"])

adverb1 = input("Ebter an Adverb: ")
adverb1 = colored(adverb1 ,"cyan",attrs=["underline"])

adverb2 = input("Enter another an Adverb: ")
adverb2 = colored(adverb2 ,"magenta",attrs=["underline"])

Exclamation = input("Enter an Emotion: ")



    #print Story


print(

        f"""One day\t {noun1} went to {place}.
        He felt very Lonely, even though the view was {adjecvtive1}.
        He decided to call his two best friends {noun2} and  {noun3}.
        When they came, they told {noun1} something {adjective2} had happend
         {noun1} went there very {adverb1}.
        When he amehe found out that his other friend was falling off a cliff
         {noun1} said Exclamation Inside he was feeling {adjective3}.
        {noun1} managed to save him
        After that they had a{adverb2} celebrates
        They all laughed""")

        
         
                      
  

    