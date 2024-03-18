import random

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

class Room:
    def __init__(self, description, monster=None, treasure=None):
        self.description = description
        self.monster = monster
        self.treasure = treasure

    def has_monster(self):
        return self.monster is not None

    def has_treasure(self):
        return self.treasure is not None

    def describe(self):
        print(self.description)

def combat(player, monster):
    print(f"A wild {monster.name} appears!")
    while player.is_alive() and monster.is_alive():
        print(f"{player.name}'s health: {player.health}")
        print(f"{monster.name}'s health: {monster.health}")
        print("1. Fight")
        print("2. Flee")
        choice = input(">> ")
        if choice == "1":
            # Player attacks monster
            damage_to_monster = random.randint(1, 20)
            monster.take_damage(damage_to_monster)
            print(f"{player.name} attacks {monster.name} for {damage_to_monster} damage!")
            if not monster.is_alive():
                print(f"{monster.name} defeated!")
                return True
            # Monster attacks player
            damage_to_player = random.randint(1, 20)
            player.take_damage(damage_to_player)
            print(f"{monster.name} attacks {player.name} for {damage_to_player} damage!")
            if not player.is_alive():
                print(f"{player.name} has been defeated...")
                return False
        elif choice == "2":
            print("You fled from the battle.")
            return False
        else:
            print("Invalid choice. Try again.")

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    print(f"Welcome, {player.name}!")

    dungeon = [
        Room("You are at the entrance of the dungeon."),
        Room("You are in a dark corridor."),
        Room("You entered a large hall.", Monster("Orc", 50, 10), "gold"),
        Room("You found a treasure chest!", None, "gems"),
        Room("You are in a narrow passage.", Monster("Goblin", 40, 8)),
        Room("You stumbled upon a trap!", None, None)
    ]

    current_room = dungeon[0]
    while True:
        current_room.describe()
        if current_room.has_monster():
            if not combat(player, current_room.monster):
                break
        elif current_room.has_treasure():
            print(f"You found {current_room.treasure}!")
            # Handle treasure collection
            # Increment score or add to inventory
            current_room.treasure = None
        else:
            print("You explore the room but find nothing of interest.")

        # Handle movement
        print("Choose your next move: north, south, east, west")
        move = input(">> ")
        if move == "north":
            current_room = dungeon[random.randint(0, len(dungeon)-1)]
        # Handle other directions similarly

if __name__ == "__main__":
    main()
