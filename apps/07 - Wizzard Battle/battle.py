from creatures import Wizard, Creature, SmallAnimal, Dragon

import random
import time


def main():
    write_header()
    game_loop()


def write_header():
    print('---------------------')
    print('    WIZARD BATTLE')
    print('---------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Red Dragon', 50, 75, True),
        Wizard('Evil Wizard', 150)
    ]

    hero = Wizard('Gandelf', 75)

    while True:

        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appeared from the forest.')

        cmd = input("Do you [a]ttack, [r]un away or [l]ook around? ")
        print()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs away to recover from battle...')
                time.sleep(3)
                print('The wizard returns, ready to fight!')

        elif cmd == 'r':
            print('The Wizard is unsure of his power and runs away!')

        elif cmd == 'l':
            print(f'Wizard {hero.name} takes a long look around and sees:')
            for c in creatures:
                print(f'A {c.name} of level {c.level}')
        else:
            print('Exiting game, bye')
            break

        if not creatures:
            print('You killed all the creatures!')
            break

        print()


if __name__ == '__main__':
    main()
