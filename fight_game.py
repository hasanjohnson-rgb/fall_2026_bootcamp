
import random

def fight_game():
    player_health = 100
    enemy_health = 100

    print("Welcome to the Python Fight Game!")
    print("Defeat your opponent to win!")

    while player_health > 0 and enemy_health > 0:
        print("\n--------------------")
        print(f"Your health: {player_health}")
        print(f"Enemy health: {enemy_health}")
        print("--------------------")

        print("1. Punch")
        print("2. Kick")
        print("3. Heal")

        choice = input("Choose your move (1-3): ")

        if choice == "1":
            damage = random.randint(10, 20)
            enemy_health -= damage
            print(f"You punched the enemy for {damage} damage!")

        elif choice == "2":
            damage = random.randint(5, 30)
            enemy_health -= damage
            print(f"You kicked the enemy for {damage} damage!")

        elif choice == "3":
            healing = random.randint(10, 20)
            player_health = min(100, player_health + healing)
            print(f"You recovered {healing} health points!")

        else:
            print("Invalid choice. Try again.")
            continue

        if enemy_health <= 0:
            print("\nCongratulations! You won the fight!")
            break

        enemy_damage = random.randint(5, 15)
        player_health -= enemy_damage
        print(f"The enemy attacks for {enemy_damage} damage!")

        if player_health <= 0:
            print("\nGame Over! The enemy defeated you.")

    print("Thanks for playing!")


if __name__ == "__main__":
    fight_game()
