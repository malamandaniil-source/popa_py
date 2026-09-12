class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self) -> str:
        return f"{self.year} {self.make} {self.model}"


my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_info())