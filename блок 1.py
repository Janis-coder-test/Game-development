enemies = [ {"name": "Guard", "hp": 50, "attack": 5},
            {"name": "Turret", "hp": 150, "attack": 20},
            {"name": "Drone", "hp": 100, "attack": 10},
            {"name": "Eliza", "hp": 80, "attack": 25}
]
Head_hero = {"name": "Sunford", "hp": 100, "attack": 15}

атака = ["Guard", "Turret", "Drone", "Eliza"]

def attack_enemies(enemies, Head_hero, атака):
    for enemy in enemies:
        if enemy['name'] in атака:
            print(f"На вас нападает {enemy['name']}")
        while enemy['hp'] > 0 and Head_hero['hp'] > 0:
            acts = input("Выберите действие('attack' 'block' 'parry' 'retreat' 'stealth': ").lower()
            if acts == 'attack':
                print(f"вы атаковали {enemy['name']}")
                enemy['hp'] -= Head_hero['attack']
                print(f"у {enemy['name']} осталось {enemy['hp']}")
                if enemy['hp'] > 0:
                    print(f"вы получили урон от {enemy['name']} ")
                    Head_hero['hp'] -= enemy['attack']
                    print(f"у {Head_hero['name']} осталось {Head_hero['hp']} ")
                    break
            elif acts == 'block':
                print(f"Вы блокировали {enemy['name']}")
                break
            elif acts == 'parry':
                print("Вы парировали {enemy['name']}")
                act = input("enemy['name'] оглушен. Ваши действия('attack' 'retreat': ").lower()
                if act == 'attack':
                    print(f"Вы атаковали {enemy['name']}")
                    enemt['hp'] -= Head_hero['attack']
                    print("у {enemy['name']} осталось {enemy['hp']}")
                    break
            elif acts == 'retreat':
                print("Вы отступили")
                break
            elif acts == 'stealth':
                print("Вы скрылись")
                break
            else:
                print("Вы выполнили комбо,либо неккоректный ввод")
                break

potions = [{"name": "Зелье здоровья", "hp": 50},
           {"name": "Зелье маны", "mana": 50}
]

def replenishment(potions):
    for p in potions:
        if  p['name'] in potions and p['name'] == 'Зелье здоровья'.lower():
            return "Вы восполнили здоровье", p['name'], p['hp']
        else:
            return "Вы восполнили ману", p['name'], p['mana']

stealth = {"name": "stealth", "done": False}

def stealth_check(stealth):
    if stealth['done'] == False:
        print("Вы видимы")
    else:
        print("Вы невидимы")
            
attack_enemies(enemies, Head_hero, атака)
replenishment(potions)
stealth_check(stealth)
