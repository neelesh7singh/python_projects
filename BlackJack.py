import random

class Account():
    
    def __init__(self,balance):
        self.balance = balance
    
    def borrow(self,amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            return self.balance
        else:
            return False 

cards={
        1:'Ace of Spades',
        2:'2 of Spades',
        3:'3 of Spades',
        4:'4 of Spades',
        5:'5 of Spades',
        6:'6 of Spades',
        7:'7 of Spades',
        8:'8 of Spades',
        9:'9 of Spades',
        10:'10 of Spades',
        11:'Jack of Spades',
        12:'Queen of Spades',
        13:'King of Spades',
        
        14:'Ace of Hearts',
        15:'2 of Hearts',
        16:'3 of Hearts',
        17:'4 of Hearts',
        18:'5 of Hearts',
        19:'6 of Hearts',
        20:'7 of Hearts',
        21:'8 of Hearts',
        22:'9 of Hearts',
        23:'10 of Hearts',
        24:'Jack of Hearts',
        25:'Queen of Hearts',
        26:'King of Hearts',
        
        27:'Ace of Diamonds',
        28:'2 of Diamonds',
        29:'3 of Diamonds',
        30:'4 of Diamonds',
        31:'5 of Diamonds',
        32:'6 of Diamonds',
        33:'7 of Diamonds',
        34:'8 of Diamonds',
        35:'9 of Diamonds',
        36:'10 of Dimonds',
        37:'Jack of Diamonds',
        38:'Queen of Diamonds',
        39:'King of Diamonds',
        
        40:'Ace of Clubs',
        41:'2 of Clubs',
        42:'3 of Clubs',
        43:'4 of Clubs',
        44:'5 of Clubs',
        45:'6 of Clubs',
        46:'7 of Clubs',
        47:'8 of Clubs',
        48:'9 of Clubs',
        49:'10 of Clubs',
        50:'Jack of Clubs',
        51:'Queen of Clubs',
        52:'King of Clubs',
    }

def points_cal(points,card):

    if card == 'Ace of Clubs' or card == 'Ace of Diamonds' or card == 'Ace of Spades' or card == 'Ace of Hearts':
        points = points + value_of_ace
    if card == '2 of Clubs' or card == '2 of Diamonds' or card == '2 of Spades' or card == '2 of Hearts':
        points = points + 2
    if card == '3 of Clubs' or card == '3 of Diamonds' or card == '3 of Spades' or card == '3 of Hearts':
        points = points + 3
    if card == '4 of Clubs' or card == '4 of Diamonds' or card == '4 of Spades' or card == '4 of Hearts':
        points = points + 4
    if card == '5 of Clubs' or card == '5 of Diamonds' or card == '5 of Spades' or card == '5 of Hearts':
        points = points + 5
    if card == '6 of Clubs' or card == '6 of Diamonds' or card == '6 of Spades' or card == '6 of Hearts':
        points = points + 6
    if card == '7 of Clubs' or card == '7 of Diamonds' or card == '7 of Spades' or card == '7 of Hearts':
        points = points + 7
    if card == '8 of Clubs' or card == '8 of Diamonds' or card == '8 of Spades' or card == '8 of Hearts':
        points = points + 8
    if card == '9 of Clubs' or card == '9 of Diamonds' or card == '9 of Spades' or card == '9 of Hearts':
        points = points + 9
    if card == '10 of Clubs' or card == '10 of Diamonds' or card == '10 of Spades' or card == '10 of Hearts':
        points = points + 10
    if card == 'King of Clubs' or card == 'King of Diamonds' or card == 'King of Spades' or card == 'King of Hearts':
        points = points + 10
    if card == 'Queen of Clubs' or card == 'Queen of Diamonds' or card == 'Queen of Spades' or card == 'Queen of Hearts':
        points = points + 10
    if card == 'Jack of Clubs' or card == 'Jack of Diamonds' or card == 'Jack of Spades' or card == 'Jack of Hearts':
        points = points + 10
    return points

balance = 3000

while balance != 0:
    while True:
        player_amount = int(input(f'You have {balance} coins in your account. Enter the amount of coins you want to use'))
        player_account = Account(balance)
        balance = player_account.borrow(player_amount)    
        if balance == False:
            print('You dont have enough balance')
            print(f'Your balance is {balance}')
        else:
            print(f'Your balance is {balance}')
            break

    ls = random.sample(range(1, 53), 10)
    dealers_cards = [ ls[0] , ls[1] , ls[2] , ls[3] , ls[4] ]
    player_cards = [ ls[5] , ls[6] , ls[7] , ls[8] , ls[9] ]

    while True:
        value_of_ace = int( input ('Please enter the value of ace either 11 or 1') )
        if value_of_ace == 1 or   value_of_ace == 11:
            break
        else:
            print('Please enter either 1 or 11')

    p_points = points_cal(0 , cards[player_cards[0]])
    p_points = points_cal(p_points , cards[player_cards[1]])
    d_points = points_cal(0 , cards[dealers_cards[0]])
    d_points = points_cal(d_points , cards[dealers_cards[1]])

    print(f'Your cards are {cards[player_cards[0]]} and {cards[player_cards[1]]}.')
    print(f'Your points are {p_points}')
    print(f'Dealers card is {cards[dealers_cards[0]]}')

    i = 0

    game = 'Play'

    while True:
        while True:
            st_or_hi = input('Do you want to hit(h) or stand(s). Press s of h')
            if st_or_hi.upper() != 'H' and st_or_hi.upper() != 'S':
                continue
            else:
                break

        if st_or_hi.upper() == 'H':
            player_card = cards[player_cards[2+i]]
            p_points = points_cal(p_points , player_card)
            print(f'Your new card is {cards[player_cards[2+i]]}')

            if p_points > 21:
                print(f'Player lost your total points were more than 21 ')
                i = i+1
                game = 'End'
                winner = 'Bot'
                break
            else:
                print(f'Your points are {p_points}')
                i = i+1

        if st_or_hi.upper() == 'S':
            break

    i=0

    print(f'Dealers hidden card is {cards[dealers_cards[1]]}')

    while game!='End':
        if d_points > p_points and d_points < 21:
            print('Dealer stands')
            game = 'End'
            winner ='Bot'
            break
        
        if d_points > 21:
            game ='End'
            winner = 'Player'
            break

        if d_points < p_points:
            print('Dealer hits')
            bot_card = cards[dealers_cards[2+i]]
            d_points = points_cal(d_points , bot_card)
            print(f'Dealers card is {cards[dealers_cards[2+i]]}')

    if game == 'End' and winner == 'Player':
        print('Player wins')
        balance = balance + player_amount * 2

    if game == 'End' and winner == 'Bot':
        print('Dealer Wins')

    replay = input('Do you want to continue playing ? Y/N')
    
    if replay.upper() == 'N':
        break
    else:
        continue
    
if balance > 3000:
    print(f'You have won a total of {balance - 3000} coins')

if balance < 3000:
    print(f'You lost a total of {3000 - balance} coins')