enemies = [
    {"name": "Guard", "hp": 50, "attack": 5},
    {"name": "Turret", "hp": 150, "attack": 20},
    {"name": "Drone", "hp": 100, "attack": 10},
    {"name": "Eliza", "hp": 80, "attack": 25}
]

Head_hero = {"name": "Sanford", "hp": 100, "attack": 15}

атака = ["Guard", "Turret", "Drone", "Eliza"]

stealth = {"name": "stealth", "done": False}

potions = [
    {"name": "Зелье здоровья", "hp": 50},
    {"name": "Зелье маны", "mana": 50}
]


def stealth_check(stealth):
    if not stealth["done"]:
        print("Вы видимы")
    else:
        print("Вы невидимы")


def replenishment(potions):
    for p in potions:
        if "hp" in p:
            print(f"Вы восполнили здоровье на {p['hp']} с помощью {p['name']}")
        elif "mana" in p:
            print(f"Вы восполнили ману на {p['mana']} с помощью {p['name']}")


def attack_enemies(enemies, Head_hero, атака):
    for enemy in enemies:
        if enemy['name'] in атака:
            print(f"\nНа вас нападает {enemy['name']}")
        else:
            continue

        while enemy['hp'] > 0 and Head_hero['hp'] > 0:
            action = input("Выберите действие ('attack', 'block', 'parry', 'retreat', 'stealth'): ").lower()

            if action == 'attack':
                print(f"Вы атаковали {enemy['name']}")
                enemy['hp'] -= Head_hero['attack']
                print(f"У {enemy['name']} осталось {enemy['hp']} HP")

                if enemy['hp'] > 0:
                    print(f"{enemy['name']} атакует вас!")
                    Head_hero['hp'] -= enemy['attack']
                    print(f"У {Head_hero['name']} осталось {Head_hero['hp']} HP")
                else:
                    print(f"{enemy['name']} побеждён!")
                break

            elif action == 'block':
                print(f"Вы блокировали атаку {enemy['name']}")
                break

            elif action == 'parry':
                print(f"Вы парировали атаку {enemy['name']}")
                follow = input(f"{enemy['name']} оглушен. Ваши действия ('attack' или 'retreat'): ").lower()
                if follow == 'attack':
                    print(f"Вы атаковали {enemy['name']}")
                    enemy['hp'] -= Head_hero['attack']
                    print(f"У {enemy['name']} осталось {enemy['hp']} HP")
                elif follow == 'retreat':
                    print("Вы отступили")
                break

            elif action == 'retreat':
                print("Вы отступили от боя")
                return  # Прерываем все бои

            elif action == 'stealth':
                stealth["done"] = True
                stealth_check(stealth)
                break

            else:
                print("Некорректный ввод или комбо-действие. Пропуск хода.")
                break

        if Head_hero["hp"] <= 0:
            print("Вы погибли!")
            return

        # спросить, хочет ли игрок продолжать
        next_action = input("Продолжить бой с другими врагами? (yes/no): ").lower()
        if next_action != 'yes':
            print("Вы решили прекратить бой.")
            break


# Запуск
attack_enemies(enemies, Head_hero, атака)
replenishment(potions)
stealth_check(stealth)
