import random

class Student:
    def __init__(self, name, money=100, scholarship=50):
        self.name = name
        self.money = money
        self.scholarship = scholarship
        self.knowledge = 0
        self.fatigue = 0

    def study(self):
        self.knowledge += 10
        self.fatigue += 15

    def work(self):
        self.money += 100
        self.fatigue += 20

    def rest(self):
        self.fatigue = max(0, self.fatigue - 30)

    def live_month(self):
        self.money += self.scholarship
        if self.money < 50:
            self.work()
        elif self.knowledge < 100:
            self.study()
        else:
            self.rest()

    def live_year(self):
        for _ in range(12):
            self.live_month()
        print(f"{self.name} завершив год Знання: {self.knowledge}, Гроші{self.money}")


student = Student("Мопс")
student.live_year()
