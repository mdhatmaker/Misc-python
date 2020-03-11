import pandas as pd
import os

### https://www.learnpython.org/en/Pandas_Basics


def get_dir():
    return os.path.dirname(os.path.realpath(__file__))


## Creating a DataFrame using a dictionary
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(dict)
print(brics)

## Replace default index values
# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

path = get_dir()

# Import the cars.csv data: cars
cars = pd.read_csv(os.path.join(path, 'cars.csv'))
print(cars)

# Use first column as index
cars = pd.read_csv(os.path.join(path, 'cars.csv'), index_col = 0)
print(cars)

print(cars['Country'])      # get column data as Series
print(cars[['Country']])    # get column data as DataFrame

print(cars[0:4])    # first 4 observations
print(cars[4:7])    # 5th, 6th and 7th observations

print(cars.iloc[2])
print(cars.loc[['Audi']])






