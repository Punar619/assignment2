import random

def roll_dice(sides=6):
    """Rolls a dice with the given number of sides (default is 6)."""
    return random.randint(1, sides)

def calculate_damage(attacker_strength):
    """Calculates damage based on attacker's strength."""
    return random.randint(1, attacker_strength)

def display_health_status(hero_hp, monster_hp):
    """Displays the current health of the hero and monster."""
    print(f"Hero HP: {hero_hp} | Monster HP: {monster_hp}")

def check_winner(hero_hp, monster_hp):
    """Checks if there is a winner in the battle."""
    if hero_hp <= 0:
        print("The hero has been defeated! Game Over.")
        return "Monster Wins"
    elif monster_hp <= 0:
        print("The monster has been defeated! Hero Wins!")
        return "Hero Wins"
    return None
