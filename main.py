import RPSart
import random

#Initializing variables
Game_count = 0
Choice_array = [0,1,2] #0 for Rock, 1 for Paper, 2 for Scissorsy
User_win = 0
Comp_win = 0

while Game_count <=2: #While loop goes for 3 rounds
  comp_choice = random.choice(Choice_array) #Computer chooses any random number from the array
  user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: ")) #User inputs his choice
  print(f"\nComputer selection = {RPSart.logo_array[comp_choice]}") #From the RPSart file, print the sign of computer's choice for visualization
  print(f"Your selection = {RPSart.logo_array[user_choice]}") #From the RPSart file, print the sign of user's choice for visualization
  
  if(user_choice == 2 and comp_choice == 0): #Incase User selects Scissors and Computer selects Rock
    print("You lost this round\n") #User looses as Rocks crushes Scissors
    Comp_win += 1  #Append one win in the computer's varirable
  elif(user_choice > comp_choice):  #In all the other cases where User's choice is greater than Computer's, User always wins 
    print("You won this round\n")
    User_win +=1
  elif(comp_choice == 2 and user_choice == 0): #If Computer selects Scissors and User selects Rock
    print("You won this round\n") #User wins this round
    User_win += 1
  elif(comp_choice > user_choice): #In all other cases where Computer's choice is greater than User's, Computer always wins
    Comp_win +=1
    print("You lost this round\n")
  else: 
    print("This round is a draw\n") #Otherwise, it is a draw
    
  Game_count +=1 #Increment the number of rounds

if(User_win > Comp_win): #At the end compare to see who won more rounds and print that
  print("You won the tournament")
elif(User_win < Comp_win):
  print("You lost the tournament")
else:
  print("The tournament ended in a draw")

