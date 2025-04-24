class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default hunger level (0-10)
        self.energy = 5  # Default energy level (0-10)
        self.happiness = 5  # Default happiness level (0-10)
        self.tricks = []  # List to store tricks learned

    def eat(self):
        """Reduce hunger by 3 points but not below 0 and increase happiness by 1"""
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness += 1
        print(f"{self.name} is eating... Hunger level: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        """Increase energy by 5 points but not above 10"""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping... Energy level: {self.energy}")

    def play(self):
        """Decrease energy by 2, increase happiness by 2, and increase hunger by 1"""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
        print(f"{self.name} is playing... Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")

    def get_status(self):
        """Prints the current state of the pet"""
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks learned: {', '.join(self.tricks) if self.tricks else 'None'}")
        print("------------------------")

    def train(self, trick):
        """Teaches a new trick and stores it in a list"""
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        """Prints all learned tricks"""
        if self.tricks:
            print(f"{self.name}'s Tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
