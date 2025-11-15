"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Abdou Sakr
Date: 11/11/2025

AI Usage: AI helped me understand the code better and helped me debug stuff when 
I got confused. I still wrote the code myself, but the AI explained things in a 
simple way like how a high school student would ask for help.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    """
    
    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """Basic strength-based attack"""
        damage = self.strength
        print(f"{self.name} hits {target.name} for {damage} damage.")
        target.take_damage(damage)
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    def display_stats(self):
        print(f"--- {self.name} ---")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")

class Player(Character):
    """
    Base class for player characters.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        
    def display_stats(self):
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    """
    
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)
        
    def attack(self, target):
        damage = self.strength + 5
        print(f"{self.name} performs a heavy warrior strike for {damage} damage!")
        target.take_damage(damage)
        
    def power_strike(self, target):
        damage = self.strength + 12
        print(f"💥 {self.name} uses POWER STRIKE for {damage} damage!")
        target.take_damage(damage)

class Mage(Player):
    """
    Mage class - magical spellcaster.
    """
    
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)
        
    def attack(self, target):
        damage = self.magic
        print(f"{self.name} casts a magic bolt for {damage} damage!")
        target.take_damage(damage)
        
    def fireball(self, target):
        damage = self.magic + 10
        print(f"🔥 {self.name} hurls a FIREBALL for {damage} damage!")
        target.take_damage(damage)

import random

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    """
    
    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)
        
    def attack(self, target):
        crit_chance = random.randint(1, 10)
        damage = self.strength
        
        if crit_chance <= 3:
            damage *= 2
            print(f"⚡ {self.name} lands a CRITICAL HIT for {damage} damage!")
        else:
            print(f"{self.name} strikes swiftly for {damage} damage.")
        
        target.take_damage(damage)
        
    def sneak_attack(self, target):
        damage = self.strength * 2
        print(f"🗡️ {self.name} performs a SNEAK ATTACK for {damage} damage!")
        target.take_damage(damage)

class Weapon:
    """
    Weapon class to demonstrate composition.
    """
    
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        print(f"Weapon: {self.name} | Damage Bonus: +{self.damage_bonus}")
# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    print("\n⚔️ Testing Polymorphism:")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # reset
    
    print("\n✨ Testing Special Abilities:")
    enemy1 = Character("Enemy1", 50, 0, 0)
    enemy2 = Character("Enemy2", 50, 0, 0)
    enemy3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(enemy1)
    mage.fireball(enemy2)
    rogue.sneak_attack(enemy3)
    
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
