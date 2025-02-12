from abc import ABC, abstractmethod

# Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретные виды оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом.", 20  # Урон 20

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука.", 15  # Урон 15

# Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__}.")

    def attack(self, monster):
        if self.weapon is None:
            print(f"{self.name} безоружен и не может атаковать!")
            return
        attack_message, damage = self.weapon.attack()
        print(attack_message)
        monster.take_damage(damage)

# Класс монстра
class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} побежден!")
        else:
            print(f"У {self.name} осталось {self.health} здоровья.")

# Демонстрация работы игры
fighter = Fighter("Герой")
monster = Monster("Дракон", 40)

# Боец выбирает оружие
fighter.change_weapon(Sword())

# Атака монстра
fighter.attack(monster)
fighter.attack(monster)  # Вторая атака добивает монстра

# Меняем оружие и пробуем снова
monster = Monster("Гоблин", 30)
fighter.change_weapon(Bow())
fighter.attack(monster)
fighter.attack(monster)
fighter.attack(monster)  # Третья атака убивает гоблина