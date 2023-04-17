#ChatGPT Python game
import random

# Define the dungeon size
DUNGEON_WIDTH = 5
DUNGEON_HEIGHT = 5

# Define the player's starting position
player_x = 0
player_y = 0

# Define the monster's starting position
monster_x = random.randint(0, DUNGEON_WIDTH - 1)
monster_y = random.randint(0, DUNGEON_HEIGHT - 1)

# Define the exit's position
exit_x = random.randint(0, DUNGEON_WIDTH - 1)
exit_y = random.randint(0, DUNGEON_HEIGHT - 1)

# Define the player's starting attributes
player_hp = 100
player_attack = 10
player_defense = 5
player_skills = {
    "slash": {"damage": 15, "difficulty": 0.8},
    "stab": {"damage": 10, "difficulty": 0.9},
    "double attack": {"damage": 20, "difficulty": 0.6}
}

# Define the available monsters
monsters = [
    {
        "name": "Goblin",
        "hp": 50,
        "attack": 8,
        "defense": 3
    },
    {
        "name": "Orc",
        "hp": 80,
        "attack": 12,
        "defense": 5
    },
    {
        "name": "Troll",
        "hp": 120,
        "attack": 15,
        "defense": 8
    }
]

# Define a function to print the dungeon map
def print_dungeon():
    for y in range(DUNGEON_HEIGHT):
        for x in range(DUNGEON_WIDTH):
            if x == player_x and y == player_y:
                print("P", end="")
            elif x == monster_x and y == monster_y:
                print("M", end="")
            elif x == exit_x and y == exit_y:
                print("E", end="")
            else:
                print(".", end="")
        print()

# Define a function to move the monster towards the player
def move_monster():
    global monster_x, monster_y
    dx = player_x - monster_x
    dy = player_y - monster_y
    if dx > 0:
        monster_x += 1
    elif dx < 0:
        monster_x -= 1
    if dy > 0:
        monster_y += 1
    elif dy < 0:
        monster_y -= 1

# Define the main game loop
while True:
    # Print the dungeon map
    print_dungeon()
    
    # Ask the player to move
    move = input("Move (n/s/e/w): ")
    
    # Update the player's position based on their move
    if move == "n":
        player_y -= 1
    elif move == "s":
        player_y += 1
    elif move == "e":
        player_x += 1
    elif move == "w":
        player_x -= 1
    
    # Move the monster towards the player
    move_monster()
    
    # Check if the player has encountered the monster
    if player_x == monster_x and player_y == monster_y:
        # Pick a random monster
        monster = random.choice(monsters)
        
        # Define the enemy's starting attributes
        monster_name = monster["name"]
        monster_hp = monster["hp"]
        monster_attack = monster["attack"]
        monster_defense = monster["defense"]
        
        print("You have encountered a", monster_name)
        
        # Define the main battle loop
        while True:
            # Print the current status
            print("Player HP:", player_hp)
            print(monster_name, "HP:", monster_hp)
    
            # Ask the player to choose an action
            action = input("Choose an action (attack/skill/run): ")
        
            # Player attacks
            if action == "attack":
                damage = player_attack - monster["defense"]
                if damage > 0:
                    monster_hp -= damage
                    print("Player dealt", damage, "damage to enemy.")
                else:
                    print("Player's attack was ineffective.")
        
            # Player tries to run
            elif action == "run":
                if random.random() < 0.5:
                    print("Player successfully ran away.")
                    break
                else:
                    print("Player failed to run away.")
        
            # Player uses a skill
            elif action == "skill":
                # Print the available skills
                print("Available skills:")
                for skill, data in player_skills.items():
                    print(skill, "(", data["damage"], "damage, difficulty", data["difficulty"], ")")
        
                # Ask the player to choose a skill
                skill = input("Choose a skill: ")
        
                # Check if the skill is valid
                if skill not in player_skills:
                    print("Invalid skill.")
                    continue
        
                # Use the chosen skill
                difficulty = player_skills[skill]["difficulty"]
                if random.random() < difficulty:
                    damage = player_skills[skill]["damage"] - monster_defense
                    if damage > 0:
                        monster_hp -= damage
                        print("Player used", skill, "and dealt", damage, "damage to", monster_name)
                    else:
                        print("Player's", skill, "was ineffective.")
                else:
                    print("Player failed to use", skill)
        
            # Enemy attacks
            monster_damage = monster_attack - player_defense
            if monster_damage > 0:
                player_hp -= monster_damage
                print("Monster dealt", monster_damage, "damage to player.")
            else:
                print("Monster's attack was ineffective.")
        
            # Check if the battle is over
            if player_hp <= 0:
                print("Player was defeated.")
                exit()
            elif monster_hp <= 0:
                print("Monster was defeated.")
                monster_x = random.randint(0, DUNGEON_WIDTH - 1)
                monster_y = random.randint(0, DUNGEON_HEIGHT - 1)
                break
                
    # Check if the player has reached the exit
    if player_x == exit_x and player_y == exit_y:
        print("You win!")
        break
