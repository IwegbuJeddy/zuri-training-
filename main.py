# Zuri Training Rock Paper Scissors by Iwegbu Jeddy
import random
#Welcome note
print('Welcome to Rock Paper Scissors. \n Pick R for rock \n P for paper \n S for scissors')
#Fetches player name
name = input("What is your name ")
#definiton of options list
options = ['R','P','S']
##functions used 
#get human's move and validate
def get_move():
     #you have to like input your move twice ...
    action = str(input(name +","+ "pick an option between R,P,S "))
    return action
    while action not in options:
          print("Wrong input, try again")
          get_move()
          break
get_move()
#define computer's move
def cpu_move():
    move = random.choice(options)
    return move


##functions end here
#....let's change the scope of the results with new global variables
h_move = get_move()
c_move = cpu_move()
##displaying the moves
print(name + "("+ h_move + ")" + ":" + "CPU" + "(" + c_move + ")")
#Winner logic
if(h_move == c_move):
    print("It's a draw")
    get_move()
elif(h_move == 'R' and c_move == 'S'):
     print(name +" "+ "wins")
elif(h_move == 'P' and c_move == 'R'):
     print(name +" "+ "wins")
elif(h_move == 'S' and c_move == 'P'):
     print(name +" "+ "wins")
elif(c_move == 'R' and h_move == 'S'):
     print(name +" "+ "wins")
elif(c_move == 'P' and h_move == 'R'):
     print(name +" "+ "wins")
elif(c_move == 'S' and h_move == 'P'):
     print(name +" "+ "wins")

