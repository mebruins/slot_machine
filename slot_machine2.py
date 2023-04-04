import random

symbols = ['@', '#', '$', '%', '&', '\/']



def deposit():
  while True:
    deposit = input('Please deposit number of tokens: ')
    if deposit.isdigit():
      deposit = int(deposit)
      if deposit > 0:
        break
      else:
        print('Please enter valid amount')
    else:
      print('Please enter valid amount')
  return deposit

def risk(tokens):
  while True:
    wager = input('How many tokens would you like to wager?: ')
    if wager.isdigit():
      wager = int(wager)
      if wager <= 0:
        print('Please enter a valid amount')
        print(f'You have {tokens} tokens')
      elif wager <= tokens:
        break
      else:
        print('You do not have enough tokens.')
        print(f'You have {tokens} tokens')
    else:
      print('Please enter valid amount')
      print(f'You have {tokens} tokens')

  return wager


  
def slot_machine(tokens):
    while True:
        play = input('(P)lay or (Q)uit?: ')

        if play == 'Q' or play == 'q':
            print('You are leaving with', tokens, 'Tokens.')
            print('Goodbye')
            break
        elif play == 'P' or play == 'p':
            print("Let's play!")
            bet = risk(tokens)

            slot1 = random.choice(symbols)
            slot2 = random.choice(symbols)
            slot3 = random.choice(symbols)
            
            print('')
            print('|', slot1, '|', slot2, '|', slot3, '|')
            print('')
            
            if slot1 == slot2 and slot2 == slot3:
                winnings = bet * 2
                tokens = tokens + winnings
                print('You won', winnings, 'Tokens!')
                print('You have', tokens, 'Tokens.')

            elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
                winnings = bet
                tokens = tokens + winnings
                print('You won', winnings, 'Tokens!')
                print('You have', tokens, 'Tokens.')

            else:
                tokens = tokens - bet
                print('No matches, you lose!')
                print('You have', tokens, 'Tokens.')
                if tokens == 0:
                    print('You have no more Tokens.')
                    print('Come again when you do.')
                    break
        else:
            print('Invalid option')


print('--------Welcome to the One-Armed Bandit!--------\n')
tokens = deposit()
slot_machine(tokens)
