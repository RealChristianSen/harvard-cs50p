def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer of Single-player? ")
    
    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        if players == "Single-player":
            recommend("Klondike")
            
    if difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        if players == "Single-player":
            recommend("Clock")
            
    
def recommend(game):
    print("You might like", game)
    
main()
