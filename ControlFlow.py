#if statements

is_game_over=False
p0xposition=0 #player x position
e0xposition=3 #enemy0 x position
e1xposition=5 #enemy1 x position

p0xposition+=2 #increases player x pos by 2
if p0xposition==e0xposition:
    is_game_over=True  #checks if the enemy0 and player position are equal, and, if so, stops the game
    elif p0xposition==e1xposition: #else if 
        is_game_over=True
        else:e0xposition+=1 
            e1xposition+=1