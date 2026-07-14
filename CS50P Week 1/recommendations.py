def main():
    difficulty = input("Difficult or Casual? ")
    if not(difficulty == "Difficult" or difficulty == "Casual"):
        print("Please enter a valid difficulty")
        return

    players = input("Multiplayer of Single-player? ")
    if not (difficulty == "Mutliplayer" or difficulty == "Single-player"):
        print("Please enter a valid number of players")
        return
    
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
        
    if difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
            
    if difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
        
    if difficulty == "Casual" and players == "Single-player":
        recommend("Clock")
    
def recommend(game):
    print("You might like", game)
    
main()
