"""This module describe simple text game."""

from random import randint

# counter of wins of hero
monster_counter = 0
# state of health of hero
hp = 10
# impact force of hero
attack = 10


# Get random value of health from 1 to 10
def get_count_health() -> int:
    """
    (None) -> int.

    Get random value of health from 1 to 10
    """
    return randint(1, 10)


# Get random impact force from 1 to n
def get_impact_force(n: int) -> int:
    """
    (int) -> int.

    Get random impact force from 1 to n
    """
    return randint(1, n)


# Realization of choice of player
def get_choice(text: str) -> int:
    """
    (str) -> int.

    Realization of choice of player
    """
    while True:
        choice = input(f"{text}")
        if choice in ('1', '2'):
            break
        else:
            print("Некорректный ввод! Введите цифру 1 или 2.")
    return int(choice)


# Calculation parameters of game when attacking
def attacking(creature: dict) -> bool:
    """
    (dict) -> bool.

    Calculation parameters of game when attacking
    """
    global hp, attack, monster_counter

    # fight for a one or several steps
    while creature['health'] > 0 and hp > 0:
        creature['health'] -= attack
        hp -= creature['force']

    if hp > 0:
        monster_counter += 1
        return False
    else:
        return True


# Main function of game
def game() -> None:
    """
    (None) -> None.

    Main function of game
    """
    global hp, attack

    creature = {
        'force': 10,
        'health': 10,
    }

    game_over = False

    print("Начало игры:")
    while True:
        event = randint(0, 2)
        # event health, when the knight found an apple
        if event == 0:
            health_add = get_count_health()
            hp += health_add
            print(f"Вы нашли яблоко, что прибавит вам {health_add} жизней, "
                  f"теперь количество ваших жизней равно {hp}.")
        # event fight
        elif event == 1:
            creature['health'] = get_count_health()
            creature['force'] = get_impact_force(20)

            print(f"БОЙ! Вы встретили чудовище c {creature['health'] } жизнями "
                  f"и с силой удара {creature['force'] }, "
                  f"у вас {hp} жизней и сила удара равна {attack}.")
            choice = get_choice("1 - атаковать чудовище, 2 - убежать,чтобы набраться сил: ")
            # attack
            if choice == 1:
                game_over = attacking(creature)
                if not game_over:
                    print(f"Вы победили в бою, количество ваших жизней равно {hp}, "
                          f"общее количество побед равно {monster_counter}.")
            # run
            elif choice == 2:
                print("Вам повезло и удалось избежать боя.")

        # event when the knight found a new sword
        elif event == 2:
            sword_impact_force = get_impact_force(20)
            print(f"Найден МЕЧ с силой удара {sword_impact_force}, "
                  f"вы же сейчас владеете мечом с силой удара равной {attack}.")
            choice = get_choice("1 - взять меч себе выбросив старый, 2 - пройти мимо меча: ")
            # update the sword
            if choice == 1:
                attack = sword_impact_force
                print(f"Вы обновили свой меч, теперь ваша сила удара = {attack}.")
            # ignore a sword
            elif choice == 2:
                print('Вы не стали брать меч.')

        if game_over or monster_counter == 10:
            break

    if monster_counter == 10:
        print("Вы победили 10 чудовищ и спасли королевство. ПОБЕДА!")
    else:
        print("ПОРАЖЕНИЕ! Игра окончена.")

# Point to start
if __name__ == '__main__':
    game()
