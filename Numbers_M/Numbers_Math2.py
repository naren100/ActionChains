import pandas as pd

class Car:
    def __init__(self, make, model, year, depreciation_file):
        self.make = make
        self.model = model
        self.year = year
        self.depreciation_table = self.load_depreciation_table(depreciation_file)

    def load_depreciation_table(self, filepath):
        df = pd.read_excel(filepath)
        df.columns = df.columns.str.strip()  # <-- fix column name issues
        return df  # a DataFrame with start_year, end_year, depreciation_rate

    def get_depreciation_rate(self):
        for _, row in self.depreciation_table.iterrows():
            if row['start_year'] <= self.year <= row['end_year']:
                return row['depreciation_rate']
        return 0.30  # default depreciation

    def cost_after_depreciation(self, price):
        rate = self.get_depreciation_rate()
        value = price * (1 - rate)
        return round(value, 2)
# Make sure depreciation_table.xlsx is in the same directory
car = Car("Toyota", "Camry", 2025, "depreciation_table.xlsx")
print(car.cost_after_depreciation(30000))  # Will use rate from Excel



