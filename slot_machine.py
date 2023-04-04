import random

symbols = ['@', '#', '$', '%', '&', '\/']


print('--------Welcome to the One-Armed Bandit!--------\n')


while True:
    deposit = input('Please deposit number of tokens: ')
    if not deposit.isdigit():
        print('Please enter valid amount.')
    elif int(deposit) <= 0:
        print('Please enter valid amount.')
    else:
        deposit.isdigit()
        tokens = int(deposit)

        while True:
            play = input('(P)lay or (Q)uit?: ')
            if play == 'Q' or play == 'q':
                print('You are leaving with', tokens, 'Tokens!')
                print('Goodbye')
                exit()
            elif play == 'P' or play == 'p':
                print("Let's play!")

                if tokens > 0:
                    print('You have', tokens, 'Tokens.')
                    wager = input('How many tokens would you like to wager?: ')
                    if not wager.isdigit():
                        print('Please enter valid amount')

                    elif wager.isdigit():
                        bet = int(wager)

                        if bet <= 0:
                            print('Please enter valid amount')

                        elif bet > tokens:
                            print('You do not have enough tokens.')

                        else:
                            slot1 = random.choice(symbols)
                            slot2 = random.choice(symbols)
                            slot3 = random.choice(symbols)

                            print('---------')
                            print('|', slot1, '|', slot2, '|', slot3, '|')
                            print('---------')

                            if slot1 == slot2 and slot2 == slot3:
                                winnings = bet*2
                                tokens += winnings
                                print('You won', winnings, 'Tokens!')
                                print('You have', tokens, 'Tokens.')

                            elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
                                winnings = bet
                                tokens += winnings
                                print('You won', winnings, 'Tokens!')
                                print('You have', tokens, 'Tokens.')

                            else:
                                tokens -= bet
                                print('No matches, you lose!')
                                print('You have', tokens, 'Tokens.')
                                if tokens <= 0:
                                    print('You have no more tokens!')
                                    print('Come back when you have more tokens.')
                                    exit()

            else:
                print('Invalid option')
