"""
OOPS stand for object oriented programming system, a s/w design model that
organizes code around real-world "objects" rather than just functions and
logic.

CORE Building Blocks:
-> Class : A blueprint or template used to create objects. It defines
variables and behaviors
-> Object: A real-world instance of a class that holds specific data
and can perform actions

4 Main Pillors of OOPS :
-> Encapsulation
-> Abstraction
-> Inheritance
-> Polymorphism

Why Use OOPS?
Reusability, Scalability, Maintainability

"""


# class syntax - class Class_name:
        # def __init__(self, parameter): (Constructor)
        # def intro(self) {Methods}
class Marvel_heros:    
    def __init__(self, name, power, weapon, nationality="American"):
        self.name = name
        self.power = power
        self.weapon = weapon
        self.nationality = nationality

    def introduction(self):
        return f"Hello I'm {self.name}"
    def hero_powers(self):
        return f"My Power is {self.power}"
    def carrying_weapon(self):
        return f"My Weapon is {self.weapon}"
    def my_nationality(self):
        return f"I'm {self.nationality}"
#creating object for a class
Iron_man = Marvel_heros("Iron Man", "Genius Intellect & Tech","Repulsor beams")
print(Iron_man.introduction())
print(Iron_man.carrying_weapon())
print(Iron_man.hero_powers())
print(Iron_man.my_nationality())