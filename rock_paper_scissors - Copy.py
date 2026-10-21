from random import choice
game={
  "r":"rock",
  "p":"paper",
  "s":"scissors"
}
wins_against={
  "r":"s",
  "p":"r",
  "s":"p"
}
choices=["r","p","s"]
player_score=0
computer_score=0
while True:
  player=input("enter \"r\" for rock \n \"p\" for paper \n \"s\" for scissors \n and \"break\" to stop: \n")
  if player not in choices and player!="break":
    print("not a valid input!")
    continue
  if player=="break" :
    print("stop!")
    break
  print(f"you chose {game[player]}")
  computer=choice(choices)
  print(f"computer chose {game[computer]}")
  if player==computer:
    print("draw")
  elif wins_against[player]==computer:
    print("you win")
    player_score+=1
  else :
    print("you lose")
    computer_score+=1
  print("your total score: ",player_score,"\n computer total score: ",computer_score)

