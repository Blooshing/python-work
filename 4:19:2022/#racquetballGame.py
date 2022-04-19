#racquetballGame

def racquetballGame():
    scoreA = 15
    scoreB = 15 
    
    
    
    if scoreA == 15 or scoreB == 15:
        print("The game is over.")
        if scoreA == 15:
            print("Team A won")
        elif scoreB == 15:
            print("Team B won.")
            
    elif not(scoreA ==15 or scoreB ==15):
        print("Continue the game.")




racquetballGame()