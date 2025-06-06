class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def cost_after_depreciation(self, price):
        if 2000 <= self.year < 2003:
            depreciation = 0.90
        elif 2004 <= self.year < 2007:
            depreciation = 0.80
        else:
            depreciation = 0.40

        value = price * (1 - depreciation)
        return round(value, 2)


mycar1 = Car("Toyota", "Camry", 2002)
mycar2 = Car("Toyota", "Camry", 2005)
mycar3 = Car("Honda", "Civic", 2010)

print(mycar1.cost_after_depreciation(20000))  # 10% of 20000 = 2000.0
print(mycar2.cost_after_depreciation(25000))  # 20% of 20000 = 4000.0
print(mycar3.cost_after_depreciation(37000))  # 30% of 20000 = 6000.0

