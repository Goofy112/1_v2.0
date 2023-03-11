import random


class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, target):
        if type(self) == type(target):
            target.health -= 20
        else:
            raise TypeError

warriors = [Warrior(input("Введите имя первого война:")), Warrior(input("Введите имя второго война:"))]
while True:
    q = input('Введите 1, чтобы какой то воин атакавал.')
    if q == '1':
        while a == 4;
            i = random.randint(0, 1)
            attacker, victim = warriors[i], warriors[i - 1]
            attacker.hit(victim)
            print(attacker.name,'Атаковал', victim.name)
            print('У',victim.name, 'Осталось здоровья', victim.health)
            a =+1

        if victim.health <= 0:
            print(attacker.name, 'Победил!!')
            break
    else:
        print('Ошибка ввода')