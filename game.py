#ChatGPT Python game
import random

# Define the game map
MAP_WIDTH = 5
MAP_HEIGHT = 5

# Define the player's starting position
player_x = 0
player_y = 0

# Define the player's starting stats
player_health = 100
player_attack = 10
player_defense = 5

# Define the monster's starting position
monster_x = random.randint(1, MAP_WIDTH - 1)
monster_y = random.randint(1, MAP_HEIGHT - 1)

# Define the monster's stats
monster_health = 50
monster_attack = 10
monster_defense = 5

# Define the game loop
while True:
    # Draw the map
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if x == player_x and y == player_y:
                print('P', end=' ')
            elif x == monster_x and y == monster_y:
                print('M', end=' ')
            else:
                print('.', end=' ')
        print()
    
    # Get the player's move
    move = input('Enter a direction (up/down/left/right): ')
    
    # Update the player's position
    if move == 'up':
        player_y -= 1
    elif move == 'down':
        player_y += 1
    elif move == 'left':
        player_x -= 1
    elif move == 'right':
        player_x += 1
    
    # Update the monster's position
    if player_x > monster_x:
        monster_x += 1
    elif player_x < monster_x:
        monster_x -= 1
    if player_y > monster_y:
        monster_y += 1
    elif player_y < monster_y:
        monster_y -= 1
    
    # Check for a collision
    if player_x == monster_x and player_y == monster_y:
        
        while True:
            # Player's turn
            player_damage = max(player_attack - monster_defense, 0)
            monster_health -= player_damage
            print('You deal {} damage to the enemy!'.format(player_damage))
            if monster_health <= 0:
                print('You defeated the enemy!')
                quit()
            
            # Enemy's turn
            monster_damage = max(monster_attack - player_defense, 0)
            player_health -= monster_damage
            if player_health <= 0:
                print('You have been defeated by the monster!')
                quit()
