while True:
    def pot_odds_calc(p, b):
        return b/(p + b)
    try:
        pot = float(input("What's the current pot size?  " ))
    except Exception:
        print("Oh no! You're not a donk, but you accidently didn't use a number. Try again.  ")
   
    try:
        bet = float(input("What's the current bet?  "))
    except Exception:
        print("Pot odds can only be calculated with numbers. Try again.  ")
        #I need to fix this^^^ i need to raise the exception or something.  It will correct the first error but then it breaks with a second error.
    if pot == 0.00:
        break
    elif bet == 0.00:
        break
    else:
        pot_odds = pot_odds_calc(pot, bet)
        #
    print("You need " + str(pot_odds *100) + "% equity to call the bet.")
    #how to end the program
    if pot == 0.00:
        break
    elif bet == 0.00:
        break
