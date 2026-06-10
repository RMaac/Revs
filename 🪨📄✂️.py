import random 
# basics details and intro 
print("Rock 🪨 , Paper 📜, Scissor ✂️ ")
print("Before continue the game we'll like to know about yourself")
rules = "📑 Each section have 3 rounds. Whoever get the higher points will win the game" 
qs = input("Would you like to continue?😉 (y/n)")
match qs.lower():
  case "y" | "yes":
    name = input("what is your name buddy?")
    print(f"Ahh nice to meet you {name.capitalize()} ✨, let's start the game. Good luck🤞")
    print(rules)
  case "n" | "no":
    print(f"it's ok buddy! see you next time.")
    exit()
  case _:
    print ("ahh! you have to refresh again or run the code again.")
    exit()
# Game start from here
game = 1
while True:
  if game ==1:
    rep="Y"
  else:
    rep = input("⁉️Want to play again?(Y/N)")
    
  if rep.capitalize()=="Y":
    print(f"🎯 Game {game}")
    modes =["Rock", "Paper", "Scissor"]
    utotal=0
    ctotal=0
    round=0
    invalid = 0
    for round in range(0,3):
      print (f"🔰 Round {round+1}")
      upick =input("👉 Rock/Paper/Scissor\n   (Choose one and write)")
      cpick=random.choice(modes)
      print(f"💁 Your: {upick}\n"
        f"      vs\n" 
        f"👾 Bot: {cpick}")
      if upick.capitalize() == "Rock":
        match cpick:
          case "Rock":
            pass
          case "Paper":
            ctotal+=1
          case "Scissor":
            utotal+=1
            
      elif upick.capitalize()== "Paper":
        match cpick:
          case "Rock":
            utotal+=1
          case "Paper":
            pass
          case "Scissor":
            ctotal+=1
            
      elif upick.capitalize() == "Scissor":
        match cpick:
          case "Rock":
            ctotal+=1
          case "Paper":
            utotal+=1
          case "Scissor":
            pass
            
      else:
        print("This round is dismissed for invalid input 😐")
        invalid+=1
      if utotal>ctotal:
        print("💠 Result: You Win the Round ✅")
      elif utotal<ctotal:
        print("💠 Result: Opps!you lose the round ✅")
      elif utotal==ctotal and invalid==0:
        print("💠 Result: Round Draw ✅") 
        
    # final output 
    if invalid>=3:
      print("The Game is dismissed for multiple invalid inputs👺")
    elif utotal>ctotal:
      print(f"🎉 Congratulations {name}, You Win the Game 🎯")
    elif utotal<ctotal:
      print(f"🤕 Opps! {name}, you lose the Game 🍌")
    elif utotal==ctotal:
      print("Game Draw 🍻")
    game+=1
  elif rep.capitalize() == "N":
        print(f"Have a nice day {name}\nsee you later 👋 ")
        break
  else:
      print("invalid statement 🤖 ")
      break
