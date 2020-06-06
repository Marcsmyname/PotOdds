#Pot Odds Calculator
#Autor: Marc Leon
#Python 3.7.3

#This program will calculate your pot odds.
#To end the program, enter the number 0.00

import tkinter

from tkinter import *

#main:

#window = Tk()
#window.title("Pot Odds Calculator")
#example. There are 10 BB in the pot. Someone bets 5 BB. Now there are 15BB in the pot.
#program asks What is new the pot size? This means you can only put the pot size in after the last bet.
#program takes your pot odds and converts them into your equity percentage.
# suppose your required equity is 25%.
# You're on the flop with 10 outs. multiply your outs by 2 and you determine you need 20% equity to call
# according to your immediate odds, you should fold, but you can probably make more than the 20% if you hit your hand
#You’re on the flop with 10 outs. Villain goes all in. Your equity required is 25% you have about a 40% chance of hitting
#you should call
#The point of this program is not to use it in a live game, but I wrote it to think through the logic of basic poker math.
#For the record, it is not that difficult to do this math in your head, but writing the code helps me understand the logic.
#I am also using it as a framework to learn some things in python like GUI.
while True:
    def pot_odds_calc(p, b):
        return b/(p + b)
    try:
        pot = float(input("What's the new pot size?  " ))
    except NameError:
        print("You didn't use a number. Try again.  ")
    except ValueError:
        print("I need a number. Try again.  ")
    try:
        bet = float(input("How much do you need to call?  "))
    except NameError:
        print("Number please. Try again ")
        raise
    except ValueError:
        print("I need a number. Try again. ")
        raise
    if pot == 0.00:
        break
    elif bet == 0.00:
        break
    else:
        pot_odds = pot_odds_calc(pot, bet)
    print("You need " + str(pot_odds *100) + "% equity to call the bet.")

    #run the main looop
    #window.mainloop()


