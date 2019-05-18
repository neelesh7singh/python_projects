def grid():
                            #For printing the grind
    
    print('    ||    ||    ')
    print(f'  {seven} ||  {eight} ||  {nine} ')
    print('    ||    ||    ')
    print('================')
    print('    ||    ||    ')
    print(f'  {four} ||  {five} ||  {six} ')      
    print('    ||    ||    ')
    print('================')
    print('    ||    ||    ')
    print(f'  {one} ||  {two} ||  {three} ')
    print('    ||    ||    ')


def initiation():
    
                          #For the starting message and getting the sign of Player1(either 'X' or 'O')
     
    print('Welcome to Tic Tac Toe.\n')        
    print(' The positions of X or O on grid will be same as on your numpad,press the respective number to play\n')
    player1sign=input('Player1 which one do you want -> X/O\n')
    return player1sign



game=True

while game:
    
                              #MAIN GAME LOOP
        
    
                              #Setting all the positions blank

    one=' '
    two=' '
    three=' '
    four=' '
    five=' '
    six=' '             
    seven=' '
    eight=' '
    nine=' '
    
    
    move='Player1'
    game=True
    grid()
    letgo=True
    while letgo:
        sign=initiation()
        if sign.upper()!='X' and sign.upper()!='O':
            print('Enter either x or o.\n')
            letgo=True
        else:
            letgo=False
    
    while game:
        
        inpu=input(f'{move} enter you number\n')
        
        
        
                            # Checking if the position in empty
        
        
        if inpu=='1':
            if one!=' ':
                print('Position in occupied.Try another number.\n')
                continue
        if inpu=='2':
            if two!=' ':
                print('Position in occupied.Try another number.\n')
                continue
        if inpu=='3':
            if three!=' ':
                print('Position in occupied.Try another number.\n')
                continue
        if inpu=='4':
            if four!=' ':
                print('Position in occupied.Try another number.\n')
                continue
        if inpu=='5':
            if five!=' ':
                print('Position in occupied.Try another number.\n')
                continue
        if inpu=='6':
            if six!=' ':
                print('Position in occupied.Try another number.\n')
                continue
        if inpu=='7':
            if seven!=' ':
                print('Position in occupied.Try another number.\n')
                continue
        if inpu=='8':
            if eight!=' ':
                print('Position in occupied.Try another number.\n')
                continue
        if inpu=='9':
            if nine!=' ':
                print('Position in occupied.Try another number.\n')
                continue
                
                         
                        #Assigning the values 
        
        
        if (inpu=='1') and (move=='Player1') and (sign.upper()=='X'):
            one='X'
        if inpu=='1' and move=='Player1' and sign.upper()=='O':
            one='O'
        if inpu=='1' and move=='Player2' and sign.upper()=='O':
            one='X'
        if inpu=='1' and move=='Player2' and sign.upper()=='X':
            one='O'
    
        if inpu=='2' and move=='Player1' and sign.upper()=='X':
            two='X'
        if inpu=='2' and move=='Player1' and sign.upper()=='O':
            two='O'
        if inpu=='2' and move=='Player2' and sign.upper()=='O':
            two='X'
        if inpu=='2' and move=='Player2' and sign.upper()=='X':
            two='O'
        
        if inpu=='3' and move=='Player1' and sign.upper()=='X':
            three='X'
        if inpu=='3' and move=='Player1' and sign.upper()=='O':
            three='O'
        if inpu=='3' and move=='Player2' and sign.upper()=='O':
            three='X'
        if inpu=='3' and move=='Player2' and sign.upper()=='X':
            three='O'
    
        if inpu=='4' and move=='Player1' and sign.upper()=='X':
            four='X'
        if inpu=='4' and move=='Player1' and sign.upper()=='O':
            four='O'
        if inpu=='4' and move=='Player2' and sign.upper()=='O':
            four='X'
        if inpu=='4' and move=='Player2' and sign.upper()=='X':
            four='O' 
    
        if inpu=='5'and move=='Player1' and sign.upper()=='X':
            five='X'
        if inpu=='5' and move=='Player1' and sign.upper()=='O':
            five='O'
        if inpu=='5' and move=='Player2' and sign.upper()=='O':
            five='X'
        if inpu=='5' and move=='Player2' and sign.upper()=='X':
            five='O' 
        
        if inpu=='6' and move=='Player1' and sign.upper()=='X':
            six='X'
        if inpu=='6' and move=='Player1' and sign.upper()=='O':
            six='O'
        if inpu=='6' and move=='Player2' and sign.upper()=='O':
            six='X'
        if inpu=='6' and move=='Player2' and sign.upper()=='X':
            six='O' 
        
        if inpu=='7' and move=='Player1' and sign.upper()=='X':
            seven='X'
        if inpu=='7' and move=='Player1' and sign.upper()=='O':
            seven='O'
        if inpu=='7' and move=='Player2' and sign.upper()=='O':
            seven='X'
        if inpu=='7' and move=='Player2' and sign.upper()=='X':
            seven='O' 
        
        if inpu=='8' and move=='Player1' and sign.upper()=='X':
            eight='X'
        if inpu=='8' and move=='Player1' and sign.upper()=='O':
            eight='O'
        if inpu=='8' and move=='Player2' and sign.upper()=='O':
            eight='X'
        if inpu=='8' and move=='Player2' and sign.upper()=='X':
            eight='O' 
    
        if inpu=='9' and move=='Player1' and sign.upper()=='X':
            nine='X'
        if inpu=='9' and move=='Player1' and sign.upper()=='O':
            nine='O'
        if inpu=='9' and move=='Player2' and sign.upper()=='O':
            nine='X'
        if inpu=='9' and move=='Player2' and sign.upper()=='X':
            nine='O'        
        
        
        
        grid()
       
    
                        
                         #Checking the winning conditions
        
        
        
        if seven==five and five==three and five!=' ':
            game=False
            break
        elif seven==four and four==one and seven!=' ':
            game=False
            break
        elif nine==five and five==one and nine!=' ':
            game=False
            break
        elif eight==five and five==two and nine!=' ':
            game=False
            break
        elif nine==six and six==three and nine!=' ':
            game=False
            break
        elif seven==eight and eight==nine and nine!=' ':
            game=False
            break
        elif four==five and five==six and five!=' ':
            game=False
            break
        elif one==two and two==three and one!=' ':
            game=False
            break
            
            
                        #Checking the Draw condition
            
            
        if one!=' 'and two!=' 'and three!=' 'and four!=' 'and five!=' 'and six!=' 'and seven!=' 'and eight!=' 'and nine!=' ':
            move='Draw'
            break
        
        
                       #Changing the player 
            
        if move=='Player1':
            move='Player2'
        else:
            move='Player1'
            
                       #MAIN GAME LOOP ENDS
    
    
            
        
                      #Checking the conditions for Winner or Draw
    if move=='Player1' or move=='Player2':
        print(f'{move} is the winner\n')
    if move=='Draw':
        print('Match is draw.\n')
    
    
    
                      #For restaring the game
    condition=input('Do you want to play again Yes/No')
    if condition.capitalize()=='Yes':
        game=True
    if condition.capitalize()=='No':
        game=False
        
