board={'T1':' ','T2':' ','T3':' ',
       'M1':' ','M2':' ','M3':' ',
       'D1':' ','D2':' ','D3':' ',
}
player=1  #to initialise to player
total_moves=0     # to count the moves
end_check=0
def check():#now checking the conditions to win the game
    if board['T1']=='X' and board['T2']=='X' and board['T3']=='X':
        print("player one won!!!")
        return 1
    elif board['M1']=='X' and board['M2']=='X' and board['M3']=='X':
        print("player one won!!!")
        return 1
    elif board['D1']=='X' and board['D2']=='X' and board['D3']=='X':
        print("player one won!!!")
        return 1
    elif board['T1']=='X' and board['M2']=='X' and board['D3']=='X':
        print("player one won!!!")
        return 1
    elif board['T3']=='X' and board['M2']=='X' and board['D1']=='X':
        print("player one won!!!")
        return 1
    elif board['T1']=='X' and board['M1']=='X' and board['D1']=='X':
        print("player one won!!!")
        return 1
    elif board['T2']=='X' and board['M2']=='X' and board['D2']=='X':
        print("player one won!!!")
        return 1
    elif board['T3']=='X' and board['M3']=='X' and board['D3']=='X':
        print("player one won!!!")
        return 1
   #now checking for O
    elif board['T1']=='O' and board['T2']=='O' and board['T3']=='O':
        print("player two won!!!")
        return 1
    elif board['M1']=='O' and board['M2']=='O' and board['M3']=='O':
        print("player two won!!!")
        return 1
    elif board['D1']=='O' and board['D2']=='O' and board['D3']=='O':
        print("player two won!!!")
        return 1
    elif board['T1']=='O' and board['M2']=='O' and board['D3']=='O':
        print("player two won!!!")
        return 1
    elif board['T3']=='O' and board['M2']=='O' and board['D1']=='O':
        print("player two won!!!")
        return 1
    elif board['T1']=='O' and board['M1']=='O' and board['D1']=='O':
        print("player two won!!!")
        return 1
    elif board['T2']=='O' and board['M2']=='O' and board['D2']=='O':
        print("player two won!!!")
        return 1
    elif board['T3']=='O' and board['M3']=='O' and board['D3']=='O':
        print("player two won!!!")
        return 1
    elif board['T1']=='O' and board['T2']=='X' and board['T3']=='X'  and board['M1']=='X' and board['M2']=='X' and board['M3']=='O'  and board['D1']=='O' and board['D2']=='O' and board['D3']=='X':
        print("DRAW")
        return 1
    elif board['T1']=='O' and board['T2']=='X' and board['T3']=='O'  and board['M1']=='X' and board['M2']=='O' and board['M3']=='X'  and board['D1']=='X' and board['D2']=='O' and board['D3']=='X':
        print("DRAW")
        return 1
    elif board['T1']=='X' and board['T2']=='O' and board['T3']=='O'  and board['M1']=='O' and board['M2']=='X' and board['M3']=='x'  and board['D1']=='X' and board['D2']=='O' and board['D3']=='O':
        print("DRAW")
        return 1
    elif board['T1']=='O' and board['T2']=='X' and board['T3']=='X'  and board['M1']=='X' and board['M2']=='O' and board['M3']=='O'  and board['D1']=='O' and board['D2']=='X' and board['D3']=='X':
        print("DRAW")
        return 1
    elif board['T1']=='X' and board['T2']=='O' and board['T3']=='O'  and board['M1']=='O' and board['M2']=='O' and board['M3']=='X'  and board['D1']=='X' and board['D2']=='X' and board['D3']=='O':
        print("DRAW")
        return 1
    elif board['T1']=='X' and board['T2']=='O' and board['T3']=='O'  and board['M1']=='O' and board['M2']=='X' and board['M3']=='X'  and board['D1']=='X' and board['D2']=='X' and board['D3']=='O':
        print("DRAW")
        return 1
       
print("T1| T2 | T3")
print("----------- ")
print("M1| M2 | M3")
print("-----------")
print("D1| D2 | D3")
print("*************")
while True:
    print(board['T1']+'|'+board['T2']+'|'+board['T3'])
    print("------")
    print(board['M1']+'|'+board['M2']+'|'+board['M3'])
    print("------")
    print(board['D1']+'|'+board['D2']+'|'+board['D3'])
    end_check=check()
    if total_moves==9 or end_check==1:
        break
    while  True:
        if player==1:
            p1_input=input("Player one....")
            if p1_input.upper() in board and board[p1_input.upper()]==' ':
                board[p1_input.upper()]='X'
                player=2
                break
            else:# wrong input from player 1
                print("Invalid input!! try again")
                continue
        else:
            p2_input=input("Player two:...")
            if p2_input.upper() in board and board[p2_input.upper()]==' ':
                board[p2_input.upper()]='O'
                player=1
                break
            else:# wrong input from player 2
                print("Invalid input!! try again")
                continue
    total_moves=total_moves+1
    print("*************************************************")
    print("")