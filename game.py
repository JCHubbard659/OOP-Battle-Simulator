from goblin import Goblin
from hero import Hero

ARENA_NAME = "Tokyo, Japan"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

def main():
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Batman")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    bob = Hero("Batman")
    print(f"{bob.name} the {bob.hero_class} enters the arena with {bob.health} health.")

    battle(bob, goblin)

if __name__ == "__main__":
    main()