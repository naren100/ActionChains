class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_depreciation_rate(self):
        depreciation_table = [
            (range(1975, 1980), 0.98),  # 98% depreciation
            (range(1980, 1985), 0.95),
            (range(1985, 1990), 0.92),
            (range(1990, 1995), 0.90),
            (range(1995, 2000), 0.85),
            (range(2000, 2004), 0.80),
            (range(2004, 2008), 0.75),
            (range(2008, 2012), 0.70),
            (range(2012, 2016), 0.60),
            (range(2016, 2020), 0.50),
            (range(2020, 2026), 0.40),  # up to year 2025
        ]

        for year_range, rate in depreciation_table:
            if self.year in year_range:
                return rate

        return 0.30  # default depreciation if year is out of defined range

    def cost_after_depreciation(self, price):
        rate = self.get_depreciation_rate()
        value = price * (1 - rate)
        return round(value, 2)

car1 = Car("Toyota", "Celica", 1979)
car2 = Car("Ford", "Taurus", 1997)
car3 = Car("Honda", "Accord", 2019)
car4 = Car("Tesla", "Model 3", 2024)

print(car1.cost_after_depreciation(30000))  # 2% value left → $600.0
print(car2.cost_after_depreciation(30000))  # 15% value left → $4500.0
print(car3.cost_after_depreciation(30000))  # 50% value left → $15000.0
print(car4.cost_after_depreciation(30000))  # 60% value left → $18000.0
