#Test Case
#a='PBHHGQxzWV'
#b='WBKAMATISN'
#c='IRLODNUKLM'
#d='DAOBPPEHIJ'
#e='CYNWOCDTNS'
#f='GJPUQRNSGE'
#g='VEKBFQBIAR'
#h='BQFGHMOTXY'
#i='OEPEWDHANy'
#j='LUBZGNDWff'

#puzzle=[a,b,c,d,e,f,g,h,i,j]

#salita1='Kamatis'
#salita2='Kundol'
#salita3='Linga'
#salita4='Sitaw'
#salita5='Upo'

#word=[salita1,salita2,salita3,salita4,salita5]
coord=[]
word=[]
puzzle=[]
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def dimensionInput(dimension):
    size = input('Please input the number of {}: '.format(dimension))
    if size<1 or size>15:
        print('Enter a number not less than 1 and greater than 15!')
        return dimensionInput(dimension)
    else:
        return size

row = dimensionInput('row')
column = dimensionInput('column')

def letterChecker(string):
    for i in range(len(string)):
        if string[i].lower() not in alphabet:
            return True
            break
        else:
            return False


def puzzleInput(counter):
    rowLetter = raw_input('Please enter the letters for row no.{} : '.format(counter))
    if len(rowLetter)!=column:
        print('Make sure that the size is equal to the column length!')
        return puzzleInput(counter)
    if letterChecker(rowLetter):
        print('Please do not input a non-alphabet character!')
        return puzzleInput(counter)
    else:
        return rowLetter.upper()
for i in range(row):
    puzzle.append(puzzleInput(i+1))

numberWords = input('Please input the number of words to find: ')

def wordInput(counter):
    words = raw_input('Please enter the word no.{} : '.format(counter))
    if len(words)>row or len(words)>column:
        print('That word would not fit the box!')
        return wordInput(counter)
    if letterChecker(words):
        print('Please do not input a non-alphabet character!')
        return wordInput(counter)
    else:
        return words 
for i in range(numberWords):
    word.append(wordInput(i+1))

def display(list1):         
    for i in list1:
        print(" ".join(i))
def displaymain():          #main display
    print '10',' ','10'
    display(puzzle)
    print len(word)
    display(word)
def flsearch(list1=[]): #searches for the first letter of the word in the puzzle and appends all coordinates found
    for x in puzzle:
        j=0
        for y in x:
            if y.lower()==list1[0].lower():
                coord.append(puzzle.index(x))
                coord.append(j)
            j=j+1
def rightcheck(x,y,list1=[]): #compares each letter of the word to the characters on the right of where we found the first letter
    r=x 
    c=y
    letter=' '
    count=0
    while r<(len(puzzle)-1) and c<(len(puzzle)-1): #make sure that the row and column iteration wont exceed the length of the puzzle
        for z in list1:
            letter=puzzle[r][c].lower()         #to set aside differences in capitalization
            if z.lower()==letter:
                count=count+1                   
                c=c+1
                if count==len(list1):           #compares counter to the length of word
                    found==True
                    print x+1,' ',y+1            #this whole function is almost the same with the other direction checking 
                    break                       #the difference is movement from row or column only     
            else:
                break
        break
def leftcheck(x,y,list1=[]):    #compares each letter of the word to the characters on the left of where we found the first letter
    r=x
    c=y
    letter=' '
    count=0
    while r<(len(puzzle)-1) and c<(len(puzzle)-1):
        for z in list1:
            letter=puzzle[r][c].lower()
            if z.lower()==letter:
                count=count+1
                c=c-1
                if count==len(list1):
                    found==True
                    print x+1,' ',y+1
                    break
            else:
                break
        break
def upcheck(x,y,list1=[]):  #compares each letter of the word to the characters on the upward direction of  where we found the first letter
    r=x
    c=y
    letter=' '
    count=0
    while r<(len(puzzle)-1) and c<(len(puzzle)-1):
        for z in list1:
            letter=puzzle[r][c].lower()
            if z.lower()==letter:
                count=count+1
                r=r-1
                if count==len(list1):
                    found==True
                    print x+1,' ',y+1
                    break
            else:
                break
        break
def downcheck(x,y,list1=[]):    #compares each letter of the word to the characters on the downward direction of where we found the first letter
    r=x
    c=y
    letter=' '
    count=0
    while r<(len(puzzle)-1) and c<(len(puzzle)-1):
        for z in list1:
            letter=puzzle[r][c].lower()
            if z.lower()==letter:
                count=count+1
                r=r+1
                if count==len(list1):
                    found==True
                    print x+1,' ',y+1
                    break
            else:
                break
        break
def rightupcheck(x,y,list1=[]): #compares each letter of the word to the characters on the diagonal direction(upright) of where we found the first letter
    r=x
    c=y
    letter=' '
    count=0
    while r<(len(puzzle)-1) and c<(len(puzzle)-1):
        for z in list1:
            letter=puzzle[r][c].lower()
            if z.lower()==letter:
                count=count+1
                c=c+1
                r=r-1
                if count==len(list1):
                    found==True
                    print x+1,' ',y+1
                    break
            else:
                break
        break
def leftupcheck(x,y,list1=[]):  #compares each letter of the word to the characters on the diagonal direction(upleft) of where we found the first letter
    r=x
    c=y
    letter=' '
    count=0
    while r<(len(puzzle)-1) and c<(len(puzzle)-1):
        for z in list1:
            letter=puzzle[r][c].lower()
            if z.lower()==letter:
                count=count+1
                c=c-1
                r=r-1
                if count==len(list1):
                    found==True
                    print x+1,' ',y+1
                    break
            else:
                break
        break
def rightdowncheck(x,y,list1=[]):   #compares each letter of the word to the characters on the diagonal direction(downright) of where we found the first letter
    r=x
    c=y
    letter=' '
    count=0
    while r<(len(puzzle)-1) and c<(len(puzzle)-1):
        for z in list1:
            letter=puzzle[r][c].lower()
            if z.lower()==letter:
                count=count+1
                c=c+1
                r=r+1
                if count==len(list1):
                    found==True
                    print x+1,' ',y+1
                    break
            else:
                break
        break
def leftdowncheck(x,y,list1=[]):    #compares each letter of the word to the characters on the diagonal direction(downleft) of where we found the first letter
    r=x
    c=y
    letter=' '
    count=0
    while r<(len(puzzle)-1) and c<(len(puzzle)-1):
        for z in list1:
            letter=puzzle[r][c].lower()
            if z.lower()==letter:
                count=count+1
                c=c-1
                r=r+1
                if count==len(list1):
                    found==True
                    print x+1,' ',y+1
                    break
            else:
                break
        break

displaymain()       #display function
for i in word:   #main code
    coord=[]        #list of coordinates of the first letter of the word in the puzzle
    found=False     #tells us that the word is not yet found
    flsearch(i)     
    j=0             #we set finder to zero for checking later on 
    for k in range((len(coord))/2): #range is one half of the range because the list coord contains both row and column coordinates
        if found==False:
            rightcheck(coord[j],coord[j+1],i)
        if found==False:
            leftcheck(coord[j],coord[j+1],i)
        if found==False:
            upcheck(coord[j],coord[j+1],i)
        if found==False:
            downcheck(coord[j],coord[j+1],i)          #this whole thing is checking all the direction from the first letter of the word
        if found==False:
            rightupcheck(coord[j],coord[j+1],i)
        if found==False:
            rightdowncheck(coord[j],coord[j+1],i)
        if found==False:
            leftupcheck(coord[j],coord[j+1],i)
        if found==False:
            leftdowncheck(coord[j],coord[j+1],i)
        if found==False:
            j=j+2


    
    
        

                
                
                
            
                
    
    
    
    
