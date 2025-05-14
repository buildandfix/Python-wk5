
# Base Superhero class
class Superhero:
    def __init__(self, name, power_level, city):
        self._name = name  # Encapsulated attribute
        self._power_level = power_level
        self._city = city
        self._is_active = True

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for power_level with validation
    @property
    def power_level(self):
        return self._power_level

    @power_level.setter
    def power_level(self, value):
        if value < 0:
            raise ValueError("Power level cannot be negative")
        self._power_level = value

    # Method to toggle active status
    def toggle_active(self):
        self._is_active = not self._is_active
        status = "active" if self._is_active else "retired"
        print(f"{self._name} is now {status}")

    # Method to display superhero info
    def display_info(self):
        return f"Name: {self._name}, Power Level: {self._power_level}, City: {self._city}, Active: {self._is_active}"

    # Polymorphic move method (to be overridden)
    def move(self):
        pass  # Abstract-like method

# Derived class for speed-based superheroes
class Speedster(Superhero):
    def __init__(self, name, power_level, city, max_speed):
        super().__init__(name, power_level, city)
        self.max_speed = max_speed

    def move(self):
        return f"{self._name} is running at {self.max_speed} km/h!"

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Max Speed: {self.max_speed} km/h"

# Derived class for flying superheroes
class Flyer(Superhero):
    def __init__(self, name, power_level, city, flight_altitude):
        super().__init__(name, power_level, city)
        self.flight_altitude = flight_altitude

    def move(self):
        return f"{self._name} is flying at {self.flight_altitude} meters!"

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Flight Altitude: {self.flight_altitude} meters"

# Derived class for strength-based superheroes
class Tank(Superhero):
    def __init__(self, name, power_level, city, strength):
        super().__init__(name, power_level, city)
        self.strength = strength

    def move(self):
        return f"{self._name} is smashing through obstacles with {self.strength} tons of force!"

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Strength: {self.strength} tons"

# Demonstration
def main():
    # Create superhero instances
    flash = Speedster("Flash", 90, "Central City", 1200)
    superman = Flyer("Superman", 95, "Metropolis", 10000)
    hulk = Tank("Hulk", 85, "New York", 50)

    # List of superheroes for polymorphism
    heroes = [flash, superman, hulk]

    # Demonstrate polymorphism with move()
    print("Superheroes on the move:")
    for hero in heroes:
        print(hero.move())

    # Display full info for each superhero
    print("\nSuperhero Profiles:")
    for hero in heroes:
        print(hero.display_info())

    # Demonstrate encapsulation and methods
    print("\nTesting superhero actions:")
    flash.toggle_active()
    try:
        superman.power_level = -10  # Should raise error
    except ValueError as e:
        print(f"Error: {e}")
    superman.power_level = 98
    print(f"Superman's updated power level: {superman.power_level}")

if __name__ == "__main__":
    main()