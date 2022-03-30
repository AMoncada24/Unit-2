print("Welcome to Text Monster!" )

floor_1 = ['monster', 'sword', 'upstairs', 'sword', 'nothing']
floor_2 = ['sword', 'magic stone', 'sword', 'upstairs', 'monster']
floor_3 = ['prize', 'boss monster', 'sword', 'monster', 'downstairs']

user_room = 4
user_floor = floor_1
game_over = False 
items = [] 
command = ""

while (game_over==False): 

  user_input = input(" what would you like to do? (left/right/up/down/grab/fight) ")
   
  if user_input == "left":
    if user_room == 0:
      print("There are no more rooms to go to.")
    elif user_floor[user_room] == "monster" and command == "left" :
      print("You lost!")
      game_over = True
    else:
      user_room = user_room - 1
      
  elif user_input == "right":
    if user_room == 4:
      print("There are no more rooms to go to.")
    elif user_floor[user_room] == "monster" and command == "right" :
      print("You lost!")
      game_over = True 
    else:
      user_room = user_room + 1 

  elif user_input == "up":
    if user_floor[user_room] == "upstairs":
      if user_floor == floor_1:
        user_floor = floor_2
      else:
        user_floor = floor_3 
    else:
      print("There is no staircase here.")
        
  elif user_input == "down":
    if user_floor[user_room] == "downstairs":
      if user_floor == floor_3:
        user_floor = floor_2
      else: 
        user_floor = floor_1
    else:
      print("There is no staircase here.")
  
  elif user_input == "grab":
    if len(items) < 3:
      if user_floor[user_room] == "sword" or user_floor[user_room] == "magic stone":
        items.append(user_floor[user_room])
        user_floor[user_room] = "nothing"
      elif user_floor[user_room] == "prize":
        print("You won! Congratulations!")
        game_over = True
        break
      else:
        print("You can't grab right now.")
    else:
      print("You can't grab anything else!")
  
  elif user_input == "fight":
    if user_floor[user_room] == "monster":
      if "sword" in items:
        user_floor[user_room] = "nothing"
        items.remove("sword")
      else: 
        print("You lost!")
        game_over = True 
    if user_floor[user_room] == "boss monster":
      if "sword" in items and "magic stone" in items:
        user_floor[user_room] = "nothing"
        items.remove("sword")
        items.remove("magic stone")
      else: 
        print("you lost")
        game_over = True 
         
  print ("This room has: " + user_floor[user_room])
  
  command = user_input
