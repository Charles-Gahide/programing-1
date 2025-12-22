#first we deal the cards, one is face up and one is face down
#the players go first, the bank only starts after the players are done
#then we ask for a bet(lets say every won bet gives you 2x)
#should decide on a minimum bet
#once a bet is made, reveal the second card
#if over 21 you lose
#if exactly on 21 you win
#if closer to 21 than the bank you win
#bank must always hit on 16 or lower
#bank must always stop on 17 or higher
import random
import time
cont=True
wallet=250

while cont==True:
    bank_turn=False
    

    if random.random() < 0.5:
        card1 = random.randint(1, 3)
    else:
        card1 = random.randint(7, 10)

    msg=(f"Your first card is {card1}")
    print("-" * len(msg))
    print(msg)
    print("-" * len(msg))



    def bet_amount():
        amount=int(input(f"how much would you like to bet? (minimum bet is 1 and your wallet is {wallet}): "))
        if amount < 1:
            print("Bet amount too small")
            return bet_amount()
        
        return amount
    bet=bet_amount()

    wallet-=bet
    if random.random() < 0.5:
        card2 = random.randint(1, 3)
    else:
        card2 = random.randint(7, 10)
        
    msg=(f"Your second card is: {card2}")
    print("-" * len(msg))
    print(msg)

    total=card1+card2
    print(f"Your total is: {total}")
    print("-" * len(msg))

    another_card=""
    while total<21 and another_card!="stop":
        another_card=input("Do you want another card or do you want to stop?\n"
        "If you want another card enter 'y' if you want to stop enter 'stop': ")
        
        print("-" * len(msg))

        if another_card=="y":
            bet_increase=int(input(f"Would you like to increase your bet? (current bet: {bet}, wallet: {wallet})\nIf yes enter the amount you want to add, if no enter '0': "))

            if bet_increase > 0:
                if bet_increase <= wallet: 
                    bet += bet_increase
                    wallet -= bet_increase
                    print(f"Your new bet is: {bet}")
                else:
                    print("You don't have enough money in your wallet!")

            print("-" * len(msg))

            if random.random() < 0.5:
                new_card = random.randint(1, 3)
            else:
                new_card = random.randint(7, 10)
            print(f"Your new card is: {new_card}")
            total+=new_card
            print(f"Your total is: {total}")
            print("-" * len(msg))

    if total > 21:
        print(f"Your total is over 21. You lose your bet of {bet}.Your wallet is now: {wallet}")
    elif total == 21:
        wallet += bet * 2
        print(f"Your total is exactly 21! You win {bet * 2}. Your wallet is now: {wallet}")
    else:
        print(f"You stopped with a total of {total}. Final bet: {bet}. Wallet: {wallet}")
        bank_turn=True
        time.sleep(1)
        print("-" * len(msg))
        print("BANK IS PLAYING")
        print("-" * len(msg))
        time.sleep(1)

    #bank's turn
    while bank_turn==True:

        if random.random() < 0.5:
            bank_card1 = random.randint(1, 3)
        else:
            bank_card1 = random.randint(7, 10)
        if random.random() < 0.5:
            bank_card2 = random.randint(1, 3)
        else:
            bank_card2 = random.randint(7, 10)

        print(f"First card: {bank_card1}")
        print(f"Second card: {bank_card2}")
        total_of_bank=bank_card2+bank_card1
        print(f"The bank's total is: {total_of_bank}")
        print("-" * len(msg))



        if total_of_bank==21:
            print(f"The bank hit exactly 21 and won, you lose your bet of {bet}. Wallet: {wallet}")
            bank_turn=False
        elif total_of_bank>=17:
            print(f"The bank passes with a total of {total_of_bank}\nYou passed with a total of {total}")
            bank_turn=False
            if total>total_of_bank:
                print(f"You win {bet*2}! Your wallet is now: {wallet+bet*2}")
            elif total==total_of_bank:
                print(f"It's a draw, you get your bet of {bet} back. Your wallet is still {wallet}")
            else:
                print(f"The bank wins! You lost your bet of {bet}. Your wallet is now {wallet}")
    
    
        else:               #total_of_bank<=16
            bank_continue=True
            while bank_continue==True:
                print("The bank continues")
                print("-" * len(msg))
                time.sleep(2)

                if random.random() < 0.5:
                    new_bank_card = random.randint(1, 3)
                else:
                    new_bank_card = random.randint(7, 10)  
                total_of_bank+=new_bank_card
                print(f"The bank's new card is {new_bank_card}\nThe new total is {total_of_bank}")
                print("-" * len(msg))

                
                if total_of_bank>21:
                    print(f"You win {bet*2}! Your wallet is now: {wallet+bet*2}")
                    bank_continue=False
                    bank_turn=False

                elif total_of_bank==21:
                    print(f"The bank hit exactly 21 and won, you lose your bet of {bet}. Wallet: {wallet}")
                    bank_continue=False
                    bank_turn=False

                elif total_of_bank>=17:
                    print(f"The bank passes with a total of {total_of_bank}\nYou passed with a total of {total}")
                    bank_continue=False
                    bank_turn=False

                    if total>total_of_bank:
                        print(f"You win {bet*2}! Your wallet is now: {wallet+bet*2}")
                    elif total==total_of_bank:
                            print(f"It's a draw, you get your bet of {bet} back. Your wallet is still {wallet}")
                    else:
                            print(f"The bank wins! You lost your bet of {bet}. Your wallet is now {wallet}")



    print("-" * len(msg))
    cont_y_or_n=input("Do you want to keep playing? Enter 'y' for yes or 'n' for no: ")
    if cont_y_or_n=='y':
        cont=True
        print("\n"*50)
    else:
        cont=False





