class AdventureGame:
    def __init__(self):
        self.current_room = "entrance"

    def display_room(self):
        rooms = {
            "entrance": "You are at the entrance of a dark cave. Go deeper or exit.",
            "hall": "You are in a large hall with two exits. One leads to a treasure room, the other to a monster's lair.",
            "treasure": "You found the treasure! You win!",
            "monster": "A monster appears! You are defeated!"
        }
        print(rooms[self.current_room])

    def move(self, direction):
        if self.current_room == "entrance":
            if direction == "deeper":
                self.current_room = "hall"
            else:
                print("You exit the cave.")
                return False
        elif self.current_room == "hall":
            if direction == "treasure":
                self.current_room = "treasure"
            elif direction == "monster":
                self.current_room = "monster"
            else:
                print("Invalid move.")
                return True
        return True

def main():
    game = AdventureGame()
    while True:
        game.display_room()
        action = input("Choose action (deeper, treasure, monster, exit): ").strip().lower()
        if not game.move(action):
            break

if __name__ == "__main__":
    main()
