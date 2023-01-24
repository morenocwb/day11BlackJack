from art import logo
from cardsDealer import initial_deal_card
from cardsDealer import deal_card
from cardsDealer import calculate_score
from cardsDealer import clean

# MAIN CODE OF THE PROGRAM
print(logo)
game_on = False
computer_cards = []
user_cards = []
mask_computer_cards = []

start_game = input(f"To Start Game press 'Y', to exit press 'N': ").lower()
if start_game == 'y':
    game_on=True

while game_on:
    if computer_cards == [] or user_cards == []:
        computer_cards = initial_deal_card()
        user_cards = initial_deal_card()

    index = len(computer_cards)-1
    for i in range(0, index):
        mask_computer_cards.insert(i, 'X')

    computer_score = calculate_score(computer_cards)
    print(f" This is Computer Score {computer_score}")
    user_score = calculate_score(user_cards)

    print(f'Computer hands is [{computer_cards[0]}' + ", " + ', '.join(mask_computer_cards) + "]")
    print(f'User hands is {user_cards}, the sum is {user_score}')

    if computer_score == 21:
        print('COMPUTER DID BLACK JACK!!!')
        game_on = False

    elif user_score == 21:
        print('YOU DID BLACK JACK!!!')
        game_on = False

    elif user_score > 21:
        for i in range(len(user_cards)):
            if user_cards[i]==11:
                user_cards[1]=1
            else:
                game_on = False
    elif computer_score > 21:
        for i in range(len(computer_cards)):
            if computer_cards[i]==11:
                computer_cards[1]=1
            else:
                game_on = False

    else:
        next_move = input(f'Do you want to Hit another card (H) or you want to pass (P)? ').lower()
        if next_move == "h":
            user_cards.append(deal_card())
        else:
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            game_on = False

    if game_on == False:
        print(f"Computer score is {computer_score}!")
        print(f"Your score is {user_score}!")
        if user_score > 21:
            print("YOU LOSE")
        elif computer_score > 21:
            print("YOU WON")
        elif computer_score > user_score:
            print('YOU LOSE!!!')
        elif computer_score == user_score:
            print(f"IT's a DRAW!!!")
        elif user_score > computer_score:
            print('YOU WON!!!!')