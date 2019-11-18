#pot odds calculator for one street



pot = float(input("What is the pot size?  " )) 
bet = float(input("What's the bet?  ")) 
#This should give you the equity required to call the bet which is what you want. 

def pot_odds_calc(p, b):
    return b/(p + b*2) 

pot_odds = pot_odds_calc(pot, bet)

print("You need " + str(pot_odds *100) + "% equity to call the bet.") 

#I got the formula from a lot of David Sklansky books, but you can also find the formula on the Poker Bank. 
