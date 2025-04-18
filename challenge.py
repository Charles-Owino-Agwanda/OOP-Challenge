class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats happily! 🍖")
        
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is now well-rested! 😴")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had so much fun playing! 🐾")
        else:
            print(f"{self.name} is too tired to play. Let them rest!")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}! 🧠")

    def show_tricks(self, trick):
        if trick in self.tricks:
            print(f" Yes! {self.name} knows how to {trick}. 🐾")
        else:
            print(f"{self.name} doesn't know how to {trick} yet.")
        

    def get_status(self):
        print(f"🐶 {self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")
        print("-" * 25)
     
        
if __name__ == "__main__":
    pet = Pet("Buddy")
    pet.eat()
    pet.get_status()
    pet.train("roll over")
    pet.train("sit")
    pet.show_tricks("roll over")
    pet.show_tricks("fetch")