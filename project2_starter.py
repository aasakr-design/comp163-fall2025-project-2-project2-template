"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Abdou Sakr
Date: 11/11/2025

AI Usage: I used AI (ChatGPT) to help me understand how inheritance, method overriding,
and composition work in Python. It also helped me figure out some bugs and how
to organize my classes better. I made sure to go through the code myself and
understand what each part does before finishing it.
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
    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
    

        
    def attack(self, target):
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        # TODO: Implement basic attack
        # Damage should be based on self.strength
        # Use target.take_damage(damage) to apply damage
        pass
        
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage! Health: {self.health}")
        
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        # TODO: Implement taking damage
        # Reduce self.health by damage amount
        # Make sure health doesn't go below 0
        pass
        
    def display_stats(self):
       """Show basic character info."""
        print(f"\nName: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")


class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
        
    def display_stats(self):
        """Show base stats plus class and level."""
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}")

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        # TODO: Call super().__init__() with warrior-appropriate stats
        # Suggested stats: health=120, strength=15, magic=5
        pass
        
    def attack(self, target):
            """Powerful physical attack with a small bonus."""
        damage = self.strength + 5
        print(f"{self.name} slashes fiercely at {target.name} for {damage} damage!")
        target.take_damage(damage)

        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        # TODO: Implement warrior attack
        # Should do more damage than basic attack
        # Maybe strength + 5 bonus damage?
        pass
        
    def power_strike(self, target):
     """Special ability: massive physical attack."""
        damage = self.strength * 2
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")
        target.take_damage(damage)
       

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        # TODO: Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20
        pass
        
    def attack(self, target):
    """Uses magic for attacks instead of strength."""
        damage = self.magic
        print(f"{self.name} casts a magic bolt at {target.name} for {damage} damage!")
        target.take_damage(damage)
      
    def fireball(self, target):
     """Special ability: strong fire attack."""
        damage = self.magic * 2
        print(f"{self.name} hurls a FIREBALL at {target.name} for {damage} damage! 🔥")
        target.take_damage(damage)
        

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)

        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10
        pass
        
    def attack(self, target):
    """Chance for a critical hit (double damage)."""
        crit_chance = random.randint(1, 10)
        if crit_chance <= 3:
            damage = self.strength * 2
            print(f"💥 {self.name} lands a CRITICAL HIT on {target.name} for {damage} damage!")
        else:
            damage = self.strength
            print(f"{self.name} swiftly attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        # TODO: Implement rogue attack
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        pass
        
    def sneak_attack(self, target):
     """Special ability: guaranteed critical hit."""
        damage = self.strength * 2
        print(f"🗡️ {self.name} performs a Sneak Attack on {target.name} for {damage} damage!")
        target.take_damage(damage)
        """
        Special rogue ability - guaranteed critical hit.
        """
        # TODO: Implement sneak attack
        # Should always do critical damage
        pass

class Weapon: 
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus
        """
        Create a weapon with a name and damage bonus.
        """
        # TODO: Store weapon name and damage bonus
        pass
        
    def display_info(self):
        print(f"Weapon: {self.name} (+{self.damage_bonus} Damage)")

        """
        Display information about this weapon.
        """
        # TODO: Print weapon name and damage bonus
        pass

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create characters
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # Display stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Polymorphism test
    print("\n⚔️ Testing Polymorphism:")
    dummy = Character("Training Dummy", 100, 0, 0)
    for c in [warrior, mage, rogue]:
        print(f"\n{c.name} attacks the dummy:")
        c.attack(dummy)
        dummy.health = 100
    
    # Special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 60, 0, 0)
    target2 = Character("Enemy2", 60, 0, 0)
    target3 = Character("Enemy3", 60, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Composition
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
