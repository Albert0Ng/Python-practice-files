print("------Tic-Tac-Toe------\n")

Box = [["","",""],["","",""],["","",""]]
#The box players will be inputting Xs and Os into
Turns = 0

print (Box[0])
print (Box[1])
print (Box[2])

print("\nPlayer 1 input")
r1=input("Insert row Coordinates from 0-2: ")
c1=input("Insert column Coordinates from 0-2: ")

def play1(Row1,Column1):
    #This function inputs Xs for the first player in the game
    global Turns
    if Box[Row1][Column1]=="O" or Box[Row1][Column1]=="X":
        print("Cell already filled in")
    else:
        Box[Row1][Column1]="X"
        Turns += 1          
    print (Box[0])
    print (Box[1])
    print (Box[2])      
    print ("\n")
    print (Turns, "Turns taken")
    
play1(r1,c1)

print("\nPlayer 2 input")
r2=input("Insert row Coordinates from 0-2: ")
c2=input("Insert column Coordinates from 0-2: ")

def play2(Row2,Column2):
    #This function inputs Os for the second player in the game
    global Turns
    if Box[Row2][Column2]=="X" or Box[Row2][Column2]=="O":
        print("Cell already filled in")
    else:
        Box[Row2][Column2]="O"
        Turns += 1    
    print (Box[0])
    print (Box[1])
    print (Box[2])    
    print ("\n")
    print (Turns, "Turns taken")
        
play2(r2,c2)

while Turns<9:    
    if Turns % 2==0:
        print("\nPlayer 1 input")
        r1=input("Insert row Coordinates from 0-2: ")
        c1=input("Insert column Coordinates from 0-2: ")
        play1(r1,c1)
    elif Turns % 2!=0:
        print("\nPlayer 2 input")
        r2=input("Insert row Coordinates from 0-2: ")
        c2=input("Insert column Coordinates from 0-2: ")
        play2(r2,c2)
        
    if Box[0][0]=="X" and Box[0][1]=="X" and Box[0][2]=="X": 
        #First horizontal row in box
        Turns=9
        print("------Player 1 wins!------")
        print("\nGame Over")
        
    elif Box[0][0]=="X" and Box[1][1]=="X" and Box[2][2]=="X": 
        #Diagonal top left to bottom right
        Turns=9
        print("------Player 1 wins!------")
        print("\nGame Over")
        
    elif Box[0][0]=="X" and Box[1][0]=="X" and Box[2][0]=="X": 
        #First vertical row in box
        Turns=9
        print("------Player 1 wins!------")
        print("\nGame Over")
        
    elif Box[0][1]=="X" and Box[1][1]=="X" and Box[2][1]=="X": 
        #Second vertical row in box
        Turns=9
        print("------Player 1 wins!------")
        print("\nGame Over")
        
    elif Box[0][2]=="X" and Box[1][2]=="X" and Box[2][2]=="X":
        #Third vertical row in box
        Turns=9
        print("------Player 1 wins!------")
        print("\nGame Over")
        
    elif Box[0][2]=="X" and Box[1][1]=="X" and Box[2][0]=="X":
        #Diagonal top right to bottom left
        Turns=9
        print("------Player 1 wins!------")
        print("\nGame Over")
        
    elif Box[1][0]=="X" and Box[1][1]=="X" and Box[1][2]=="X":
        #Second horizontal row in box
        Turns=9
        print("------Player 1 wins!------")
        print("\nGame Over")
        
    elif Box[2][0]=="X" and Box[2][1]=="X" and Box[2][2]=="X":
        #Third horizontal row in box
        Turns=9
        print("------Player 1 wins!------")
        print("\nGame Over")
        
    elif Box[0][0]=="Y" and Box[0][1]=="Y" and Box[0][2]=="Y":
        #First horizontal row in box
        Turns=9
        print("------Player 2 wins!------")
        print("\nGame Over")
        
    elif Box[0][0]=="Y" and Box[1][1]=="Y" and Box[2][2]=="Y":
        #Diagonal top left to bottom right
        Turns=9
        print("------Player 2 wins!------")
        print("\nGame Over")
        
    elif Box[0][0]=="Y" and Box[1][0]=="Y" and Box[2][0]=="Y":
        #First vertical row in box
        Turns=9
        print("------Player 2 wins!------")
        print("\nGame Over")
        
    elif Box[0][1]=="Y" and Box[1][1]=="Y" and Box[2][1]=="Y":
        #Second vertical row in box
        Turns=9
        print("------Player 2 wins!------")
        print("\nGame Over")
        
    elif Box[0][2]=="Y" and Box[1][2]=="Y" and Box[2][2]=="Y":
        #Third vertical row in box
        Turns=9
        print("------Player 2 wins!------")
        print("\nGame Over")
        
    elif Box[0][2]=="Y" and Box[1][1]=="Y" and Box[2][0]=="Y":
        #Diagonal top right to bottom left
        Turns=9
        print("------Player 2 wins!------")
        print("\nGame Over")
        
    elif Box[1][0]=="Y" and Box[1][1]=="Y" and Box[1][2]=="Y":
        #Second horizontal row in box
        Turns=9
        print("------Player 2 wins!------")
        print("\nGame Over")
        
    elif Box[2][0]=="Y" and Box[2][1]=="Y" and Box[2][2]=="Y":
        #Third horizontal row in box
        Turns=9
        print("------Player 2 wins!------") 
        print("\nGame Over")
