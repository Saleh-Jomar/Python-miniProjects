from random import randint
import time
adj=0
nope=0
start = "1" 
game= ["1","0"]
haha=[]
for z in range(1,101): 
        haha.append(str(z)) 
while start=="1": 
    for i in range(1,3):
        haha.remove(str(i))
    timestart = time.clock()
    counter= 0 
    board=[] 
    mine=[] 
    tracker=[] 
    invalid=[]
    k=0
    while True:
        boardm = raw_input("Enter no. of rows and columns (3-100): ")
        if boardm in haha:
           break 
        else:
            print "Invalid Input"
    for i in range(1,3):
        haha.append(str(i))
    while True:
        bombs = raw_input("Enter no. of bombs: ")
        if bombs not in haha:
            print "Invalid Input"
        else:
            if int(bombs) > int(boardm):
                print "No. of bombs must not exceed no. of rows and columns"
            else:
                break
    for i in range(int(boardm)):
        board.append(["X"]*int(boardm))
    for l in range(int(boardm)):
        invalid.append(str(k))
        k=k+1
    if int(bombs) <= int(boardm):
        x=randint(0,int(boardm)-1)
        y=randint(0,int(boardm)-1)
        while len(mine) != int(bombs):
            if (x,y) in mine:
                x=randint(0,int(boardm)-1)
                y=randint(0,int(boardm)-1)
            else:
                mine.append((x,y))
    def draw(x):
        for i in board:
                print(" ".join(i))
    def mines(r,c):
        adj = 0
        if (int(r)+1,int(c)) in mine:
            adj=adj+1
        if (int(r)-1,int(c)) in mine:
            adj=adj+1
        if (int(r),int(c)+1) in mine:
            adj=adj+1
        if (int(r),int(c)-1) in mine:
            adj=adj+1
        if (int(r)+1,int(c)+1) in mine:
            adj=adj+1
        if (int(r)+1,int(c)-1) in mine:
            adj=adj+1
        if (int(r)-1,int(c)+1) in mine:
            adj=adj+1
        if (int(r)-1,int(c)-1) in mine:
            adj=adj+1
        return adj
    draw(board)
    while int(bombs) != int(boardm)*int(boardm)-counter:
        while int(bombs) != int(boardm)*int(boardm)-counter:
            print "Input must be from 0 to",int(boardm)-1
            r= raw_input("Row Coordinate: ")
            c= raw_input("Column Coordinate: ")
            if r not in invalid or c not in invalid:
                print "Invalid Input"
                draw(board)
            elif (r,c) in tracker:
                print "Already Opened"
                draw(board)
            else:
                break
        if nope == 0:
            if (int(r),int(c)) in mine:
                print "GAME OVER"
                break
            else:
                board[int(r)][int(c)] = str(mines(int(r),int(c)))
                tracker.append((r,c))
                draw(board)
                counter=counter+1
    if int(bombs) == int(boardm)*int(boardm)-counter:
        timestop=time.clock()
        print "CONGRATULATIONS! YOU WON!"
        print "Time lapse:",timestop-timestart,"seconds"
    l=0
    for r in range(int(boardm)):
        m=0
        for c in range(int(boardm)):
            if (r,c) in mine:
                board[l][m]= "*"
                m=m+1
            else:
                board[l][m] = "X"
                m=m+1
        l=l+1
    draw(board) 
    while True:
        start= raw_input("Enter 1 if you want to play again and 0 if not: ")
        if start not in game:
            print "Invalid input"
        else:
            break
print "Thank you for playing"
