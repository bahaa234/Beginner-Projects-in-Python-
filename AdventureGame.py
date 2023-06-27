answer = input("What you like to play? (yes/no) ")

if answer.lower().strip()== "yes":

    answer= input("You reach a crossroads, would like to left or right?").lower().strip()


    if answer== "left":

       answer=  input("you encounter a monster, would you like to run or attak.")

       if answer == "attack":
           print("That was not the geatest idea, you lost!")

       else:
           print("Good choice, you made it away safely!")

           answer = input("You see a car and a plane, which would like to take? (car/plane)")

           if answer =="plane":
               
               print("Unfortuntly, you don't know how to fly a plane....Game Over")

    elif answer == "right":

        print("""You walk aimlessly to the right and fall on patch of ice.
          You injured your leg and cannot continue. Game Over!!""")

    else:

        print("Invalid choice, you lost!")        



else:
    print("That is too bad!")