class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passenger_names(self):
        if self.passengers:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")


nick = Human("Vlod")
kate = Human("Mops")
sexmops = Human("Sexmops")
kizaru = Human("Kizaru")
fedota = Human("Fedota")
car = Auto("Mercedes")
car.add_passenger(nick)
car.add_passenger(kate)
car.add_passenger(sexmops)
car.add_passenger(kizaru)
car.add_passenger(fedota)
car.print_passenger_names()
print('-'*30)
car = Auto("BMW")
car.add_passenger(nick)
car.add_passenger(kate)
car.add_passenger(sexmops)
car.add_passenger(kizaru)
car.add_passenger(fedota)
car.print_passenger_names()
