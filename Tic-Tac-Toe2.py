#A game of Tic-Tac-Toe between two people
#Created by Albert on 24/06/2017
print("------Tic Tac Toe------\n")

Box=[["","",""],["","",""],["","",""]]

Turns=0

#The box that will contain the Xs and Os
print(Box[0])
print(Box[1])
print(Box[2])


def player1(boxNo):
    #This function inputs Xs for the player
    global Turns
    if boxNo==1:
        if Box[0][0]!="":
            print("Already input data")
        else:   
            Box[0][0]="X"
            Turns+=1
    elif boxNo==2:
        if Box[0][1]!="":
            print("Already input data")
        else:
            Box[0][1]="X"
            Turns+=1
    elif boxNo==3:
        if Box[0][2]!="":
            print("Already input data")
        else:
            Box[0][2]="X"
            Turns+=1
    elif boxNo==4:
        if Box[1][0]!="":
            print("Already input data")
        else:
            Box[1][0]="X"
            Turns+=1
    elif boxNo==5:
        if Box[1][1]!="":
            print("Already input data")
        else:
            Box[1][1]="X"
            Turns+=1
    elif boxNo==6:
        if Box[1][2]!="":
            print("Already input data")
        else:
            Box[1][2]="X"
            Turns+=1
    elif boxNo==7:
        if Box[2][0]!="":
            print("Already input data")
        else:
            Box[2][0]="X"
            Turns+=1
    elif boxNo==8:
        if Box[2][1]!="":
            print("Already input data")
        else:
            Box[2][1]="X"
            Turns+=1
    elif boxNo==9:
        if Box[2][2]!="":
            print("Already input data")
        else:
            Box[2][2]="X"
            Turns+=1
    else:
        print("Insert valid number")
    print(Box[0])
    print(Box[1])
    print(Box[2])
    print("\n",Turns,"Turns taken")


def player2(boxNo):
    #This function inputs Os for the player
    global Turns
    if boxNo==1:
        if Box[0][0]!="":
            print("Already input data")
        else:   
            Box[0][0]="O"
            Turns+=1
    elif boxNo==2:
        if Box[0][1]!="":
            print("Already input data")
        else:
            Box[0][1]="O"
            Turns+=1
    elif boxNo==3:
        if Box[0][2]!="":
            print("Already input data")
        else:
            Box[0][2]="O"
            Turns+=1
    elif boxNo==4:
        if Box[1][0]!="":
            print("Already input data")
        else:
            Box[1][0]="O"
            Turns+=1
    elif boxNo==5:
        if Box[1][1]!="":
            print("Already input data")
        else:
            Box[1][1]="O"
            Turns+=1
    elif boxNo==6:
        if Box[1][2]!="":
            print("Already input data")
        else:
            Box[1][2]="O"
            Turns+=1
    elif boxNo==7:
        if Box[2][0]!="":
            print("Already input data")
        else:
            Box[2][0]="O"
            Turns+=1
    elif boxNo==8:
        if Box[2][1]!="":
            print("Already input data")
        else:
            Box[2][1]="O"
            Turns+=1
    elif boxNo==9:
        if Box[2][2]!="":
            print("Already input data")
        else:
            Box[2][2]="O"
            Turns+=1
    else:
        print("Insert valid number")
    print(Box[0])
    print(Box[1])
    print(Box[2])
    print("\n",Turns,"Turns taken")
    
#The algorithm that runs the game    
while Turns<9:
    if Turns%2==0:
        play1Input=input("Player X please input box coordinates: ")
        player1(play1Input)
    elif Turns%2!=0:
        play2Input=input("Player O please input box coordinates: ")
        player2(play2Input)
    
    #If Player X wins
    if Box[0][0]=="X" and Box[0][1]=="X" and Box[0][2]=="X":
        #First horizontal row
        print("------Player 1 wins!------") 
        Turns=9        
    elif Box[1][0]=="X" and Box[1][1]=="X" and Box[1][2]=="X":
        #Second horizontal row
        print("------Player 1 wins!------")
        Turns=9
    elif Box[2][0]=="X" and Box[2][1]=="X" and Box[2][2]=="X":
        #Third horizontal row
        print("------Player 1 wins!------")
        Turns=9
    elif Box[0][0]=="X" and Box[1][0]=="X" and Box[2][0]=="X":
        #First vertical row
        print("------Player 1 wins!------")
        Turns=9
    elif Box[0][1]=="X" and Box[1][1]=="X" and Box[2][1]=="X":
        #Second vertical row
        print("------Player 1 wins!------")
        Turns=9
    elif Box[0][2]=="X" and Box[1][2]=="X" and Box[2][2]=="X":
        #Third vertical row
        print("------Player 1 wins!------")
        Turns=9
    elif Box[0][0]=="X" and Box[1][1]=="X" and Box[2][2]=="X":
        #Diagonal top left to bottom right
        print("------Player 1 wins!------")
        Turns=9
    elif Box[0][2]=="X" and Box[1][1]=="X" and Box[2][0]=="X":
        #Diagonal top right to bottom left
        print("------Player 1 wins!------")
        Turns=9
    #If Player O wins    
    elif Box[0][0]=="O" and Box[0][1]=="O" and Box[0][2]=="O":
        #First horizontal row
        print("------Player 2 wins!------") 
        Turns=9
    elif Box[1][0]=="O" and Box[1][1]=="O" and Box[1][2]=="O":
        #Second horizontal row
        print("------Player 2 wins!------")
        Turns=9
    elif Box[2][0]=="O" and Box[2][1]=="O" and Box[2][2]=="O":
        #Third horizontal row
        print("------Player 2 wins!------")
        Turns=9
    elif Box[0][0]=="O" and Box[1][0]=="O" and Box[2][0]=="O":
        #First vertical row
        print("------Player 2 wins!------")
        Turns=9
    elif Box[0][1]=="O" and Box[1][1]=="O" and Box[2][1]=="O":
        #Second vertical row
        print("------Player 2 wins!------")
        Turns=9
    elif Box[0][2]=="O" and Box[1][2]=="O" and Box[2][2]=="O":
        #Third vertical row
        print("------Player 2 wins!------")
        Turns=9
    elif Box[0][0]=="O" and Box[1][1]=="O" and Box[2][2]=="O":
        #Diagonal top left to bottom right
        print("------Player 2 wins!------")
        Turns=9
    elif Box[0][2]=="O" and Box[1][1]=="O" and Box[2][0]=="O":
        #Diagonal top right to bottom left
        print("------Player 2 wins!------")
        Turns=9

print("Game Over")