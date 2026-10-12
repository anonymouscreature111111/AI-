import random

moves = ["rock", "paper", "scissors"]


user_score = 0
bot_score = 0

playing = True

while playing:
    
    bot_move = random.choice(moves)
    
    
    user_move = input("\nPick rock, paper, or scissors: ").strip().lower()
    
    
    if user_move not in moves:
        print("Please enter rock, paper, or scissors.")
        continue  
        
    print(f"Bot chose: {bot_move}")
    
    
    if bot_move == user_move:
        print("It's a tie!")
        
    
    elif (bot_move == "rock" and user_move == "paper") or \
         (bot_move == "paper" and user_move == "scissors") or \
         (bot_move == "scissors" and user_move == "rock"):
        print("Wow you win! 1 point for you!")
        user_score += 1  
        
    
    else:
        print("You lost, 1 point for me!")
        bot_score += 1  

    
    print(f"Score -> You: {user_score} | Bot: {bot_score}")

    
    play_again = input("\nDo you want to keep playing? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("\nThanks for playing! Final Score:")
        print(f"You: {user_score} | Bot: {bot_score}")
        playing = False  
