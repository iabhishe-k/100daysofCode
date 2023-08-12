import replit
import random
import art

restart = True

while (restart):
    replit.clear()
    print(art.logo)

    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card = []
    dealer_card = []

    player_card.append(random.choice(card))
    player_card.append(random.choice(card))
    dealer_card.append(random.choice(card))

    print(f"Your cards: {player_card}")
    print(f"Dealer card: {dealer_card}")

    hit = input("Type 'y' for another card or type 'n' to pass: ")
    if (hit == 'y'):
        player_card.append(random.choice(card))
        player_value = sum(player_card)

    elif (hit == 'n'):
        player_value = sum(player_card)

    dealer_card.append(random.choice(card))
    dealer_value = sum(dealer_card)

    if (player_value > 21):
        if (11 in player_card):
            player_value -= 10
            player_card[player_card.index(11)] = 1
        else:
            print(f"Your cards: {player_card}\tYour Score: {player_value}")
            print(f"Dealer cards: {dealer_card}\tDealer Score: {dealer_value}")
            print("You Lose")

    if (player_value <= 21):
        print(f"Your cards: {player_card}\tYour Score: {player_value}")
        print(f"Dealer cards: {dealer_card}\tDealer Score: {dealer_value}")
        if (player_value > dealer_value):
            print("You Won")
        elif (player_value < dealer_value):
            print("You Lose")
        else:
            print("It is a tie")

    restart_in = input("Type 'y' to restart the game or type 'n' to exit: ")
    if (restart_in == 'y'):
        restart = True
    elif (restart_in == 'n'):
        restart = False
