#!/usr/bin/python3

import os

def menue():
   heading()
   print("\t1. Play the game\n")
   print("\t2. Instructions\n")
   print("\t3. Exit\n")

def hint_grid():
   print("\t   Hint Grid\n")
   a=[["x=1,y=1"," | ","x=1,y=2"," | ","x=1,y=3"],["x=2,y=1"," | ","x=2,y=2"," | ","x=2,y=3"],["x=3,y=1"," | ","x=3,y=2"," | ","x=3,y=3"]]
   for i in range (0,3):
      for j in range (0,5):
        if j<4:
          print(a[i][j],end=" ")
        elif j==4:
            print(a[i][j])
      if i<2:
         print("-"*32)
   print("\n\n")

def instructions():
   hint_grid()
   print("This is the hint grid for the game . In the game you will be asked to enter the x and y coordinate of the grid as per you can see in the above grid, for example you want your 'o' to be placed in 1st block hence when you are asked to enter the x coordinte then you enter the number 1 and when you are asked to enter the y coordinate then you have to enter the number 1 now your 'o' will be placed in the first block similarly for every block its coordinates are written in the respective block in the above hint grid.\n Now I hope it would be more easier for you to play this game.\nNow go and enjoy your TIC TAC TOE\n\n")

def display(a):
   for i in range(0,3):
      print(" ",end=" ")   
      for j in range (0,3):
         if j<2:
            print(a[i][j], end=" ")
            print("|", end=" ")
         elif j==2:
            print(a[i][j])
      if i<2:
         print(" "+"-"*11)

def final_display(a,p):
    for i in range (0,3):
        for j in range (0,3):
            if a[i][j]!=p:
               a[i][j]=" "
    display(a)

def heading():
   os.system('clear')
   print("\n\n\t\tTIC-TAC-TOE\n\n")

def topic(a,p):
   heading()
   hint_grid()
   display(a)
   print("\n\n")
   print("\nThis is the chance of "+p+"\n")

def result(a):
  if a[0][0]==a[1][1] and a[1][1]==a[2][2] and a[1][1]!=" ":
     return(1)
  elif a[0][2]==a[1][1] and a[1][1]==a[2][0] and a[1][1]!=" ":
     return(1)
  elif a[0][0]==a[1][0] and a[1][0]==a[2][0] and a[1][0]!=" ":
      return(1)
  elif a[0][1]==a[1][1] and a[1][1]==a[2][1] and a[1][1]!=" ":
      return(1)
  elif a[0][2]==a[1][2] and a[1][2]==a[2][2] and a[2][2]!=" ":
      return(1)    
  elif a[0][0]==a[0][1] and a[0][1]==a[0][2] and a[0][0]!=" ":
      return(1)
  elif a[1][0]==a[1][1] and a[1][1]==a[1][2] and a[1][1]!=" ":
      return(1)
  elif a[2][0]==a[2][1] and a[2][1]==a[2][2] and a[2][2]!=" ":
      return(1)
  else:
      return(0)

def game():
   r,c=(3,3)
   a=[[" " for i in range(c)] for j in range(r)]
   r=0
   q="m"
   t=1 
   while q=="m":  
      menue()
      t=int(input("Enter your choice : "))
      while t!=1 and t!=2 and t!=3:
         print("\n\n")
         print("PLease enter the correct choice\n")
         print("Enter 1 to start playing the game")
         print("Enter 2 to read the instructions")
         t= int(input("Enter your choice : "))
      if t==1:
         while(t==1 or q=="y" ):
            for i in range (0,3):
               for j in range(0,3):
                  a[i][j]=" "
            heading()
            p=str(input("who wants to take the first chance ('x' or 'o'): "))
            if p=="x" or p=="o" or p=="X" or p=="O":
               for i in range(0,9):
                  heading()
                  hint_grid()
                  display(a)
                  print("\n\n")
                  print("\nThis is the chance of "+p+"\n")
                  x= int(input("Enter the x coordinate : "))
                  while x<1 or x>3:
                     print("\nplease enter the correct x coordinate (1,2,3)\n")
                     q=str(input("Enter 'y' to continue the game and 'n' to exit : "))
                     if q!="y":
                        break
                     topic(a,p)
                     x= int(input("Enter the x coordinate : "))
                  y= int(input("Enter the y coordinate : "))
                  while y<1 or y>3:
                     print("\nplease enter the correct y coordinate (1,2,3)\n")
                     q=str(input("Enter 'y' to continue the game and 'n' to exit : "))
                     if q!="y":
                        break
                     topic(a,p)
                     print("Enter the x coordinate : ", end="")
                     print(x)
                     y= int(input("Enter the y coordinate : "))
                  while a[x-1][y-1]!=" ":
                     print("\n")
                     print(a[x-1][y-1]+" is already placed there please choose other location ")
                     print("\n")
                     q=str(input("Enter 'y' to continue the game and 'n' to exit : "))
                     if q!="y":
                        break
                     topic(a,p)
                     x=int(input("Enter the x coordinate : "))
                     while x<1 or x>3:
                        print("\nplease enter the correct x coordinate (1,2,3)\n")
                        q=str(input("Enter 'y' to continue the game and 'n' to exit : "))
                        if q!="y":
                           break
                        topic(a,p)
                        x= int(input("Enter the x coordinate : "))
                     y= int(input("Enter the y coordinate : "))
                     while y<1 or y>3:
                        print("\nplease enter the correct x coordinate (1,2,3)\n")
                        q=str(input("Enter 'y' to continue the game and 'n' to exit : "))
                        if q!="y":
                           break
                        topic(a,p)
                        print("Enter the x coordinate : ", end="")
                        print(x)
                        y= int(input("Enter the y coordinate : "))
                  if a[x-1][y-1]==" ":
                     a[x-1][y-1]=p
                  r=result(a)
                  if r!=0:
                     break
                  if p=="x":
                     p="o"
                  elif p=="o":
                     p="x"
                  elif p=="X":
                     p="O"
                  elif p=="O":
                     p="X"
                  heading()
                  hint_grid()
                  display(a)
                  print("\n\n")
               if r==1 and i!=9:
                  heading()
                  print("\t\t  "+p+" won\n\n")
                  final_display(a,p)
               elif r==0 and i==9:
                  heading()
                  print("\t\t\tmatch draw\n\n")  
                  display(a)
               print("\n\n")
               print("Would you like to play the game again ?")
               q=str(input("Enter 'y' to continue the game , 'n' to exit and 'm' for menue : "))
               if q=="m":
                  break
               elif q=="n":
                  break
            else:
               print("\nPlease enter the correct choice ('x' or 'o')\n")
               q=str(input("Enter 'y' to continue and 'n' to exit : "))
               if q!="y":
                  break
               print("\n")
      elif t==2:
         heading()
         instructions()
         q=str(input("Enter 'm' to return back to menue and 'n' to exit "))
         if q=="n":
            break
         print("\n")
      elif t==3:
         q="n"
         break

def regards():
   os.system('clear')
   print("\n\n\nThanks for playing the game\n")
   print("\n\nHope you enjoyed it\n\n\n\n")

game()

regards()

exit()