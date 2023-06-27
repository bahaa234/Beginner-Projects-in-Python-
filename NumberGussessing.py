import random


flag = True

while flag:
    num = input("type a number for an upper bound: ")
    

    if num.isdigit():
        print("let us play!")
        num = int(num)
        flag = False

    else:
        print("Invalid input! Try Again!")


secert = random.randint(1,num)

guess = None
count = 1

while guess != secert:

    guess = input("Please type a number between 1 and"+ str(num)+":")
    if guess.isdigit():
        guess = int(guess)

    if guess == secert:
        print("you guessed the right number!")

    else:
        print("please try again ")
        count +=1

print("it took you", count,"guesses")
