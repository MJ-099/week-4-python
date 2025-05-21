# Base class
class Character:
    def __init__(self, name, power, strength):
        self.name = name
        self._power = power      # Protected attribute
        self.strength = strength

    def display_power(self):
        print(f"{self.name} has the power of {self._power}!")

# Subclass
class Superhero(Character):
    def __init__(self, name, power, strength, catchphrase):
        super().__init__(name, power, strength)
        self.catchphrase = catchphrase

    def fight_crime(self):
        print(f"{self.name} says '{self.catchphrase}' and stops the villain!")

# Another subclass
class Villain(Character):
    def __init__(self, name, power, strength, evil_plan):
        super().__init__(name, power, strength)
        self.evil_plan = evil_plan

    def reveal_plan(self):
        print(f"{self.name}'s evil plan is: {self.evil_plan}")

# Create objects
hero = Superhero("Captain Code", "Bug Fixing", 90, "Code is Justice!")
villain = Villain("Dr. Crash", "System Failure", 85, "Crash the mainframe at midnight!")

# Call methods
hero.display_power()
hero.fight_crime()

villain.display_power()
villain.reveal_plan()
