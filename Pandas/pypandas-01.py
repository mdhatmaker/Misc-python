import pandas as pd
import sys





pathname_data = r'D:\Users\mhatm\Downloads\survey_results_public.csv'
pathname_schema = r'D:\Users\mhatm\Downloads\survey_results_schema.csv'

print('Reading data...')
dfs = pd.read_csv(pathname_schema)
print(dfs)
print(dfs.columns)
filt = dfs['Column'].str.startswith('Dep')
print(dfs.loc[filt])
sys.exit()
df = pd.read_csv(pathname_data)
#print(df)
print('Sorting data...')
df.sort_values(by='Country', inplace=True)
print(df.head(20))

df.sort_values(by=['Country','ConvertedSalary'], ascending=[True,False], inplace=True)
print(df.head(20))

print(df['ConvertedSalary'].nlargest(10))
print(df.nlargest(10, 'ConvertedSalary'))       # largest values of specified column
#print(df.nsmallest(10, 'ConvertedSalary'))      # smallest values of specified column


# GROUPING AND AGGREGATING

dfx = df['ConvertedSalary'].head(15)
print(dfx)
print(df['ConvertedSalary'].median())
print(df['ConvertedSalary'].mean())

print(df.median())
print(df.describe())

print(df['ConvertedSalary'].count())

print(df['Hobby'].value_counts())
print(df['Hobby'].value_counts(normalize=True))


sys.exit()


people = {
    "first": ['Corey', 'Jane', 'John', 'Adam'],
    "last": ['Schafer', 'Doe', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', 'Adam@email.com']
}

df = pd.DataFrame(people)
print(df)

# SORTING
print(df.sort_values(by='last', ascending=True))
print(df.sort_values(by=['last','first'], ascending=False))
print(df.sort_values(by=['last','first'], ascending=[False,True]))
print(df)
print(df.sort_values(by=['last','first'], ascending=[False,True], inplace=True))
print(df)

df.sort_index(inplace=True)
print(df)

print(df['last'].sort_values())



sys.exit()


pathname = r'C:\GitHub\Misc-csharp\MLPredictHousing\data\Housing_Data.csv'
df = pd.read_csv(pathname)

print(df.shape)
#df.info()

# show more columns/rows
#pd.set_option('display.max_columns', 85)
#pd.set_option('display.max_rows', 85)

print(df.head(5))
print(df.tail(5))

print(df.iloc[0])
print(df.iloc[1])

print(df.columns)

df1 = df[df.RAD == 1]
print(df1)
print(df1.shape)

print(df1['RAD'])
print(type(df1['RAD']))             # return a Series
print(df1.iloc[0])
print(df1.iloc[1])
print(df1.RAD)
print(df1[['CHAS','RAD']])
print(type(df1[['CHAS','RAD']]))    # return a DataFrame
try:
    print(df1.loc[195])
except:
    print('An exception occurred.')


print(df.iloc[[0,1], [3]])          # 1st and 2nd rows, 4th column
print(df['RAD'])
print(df['RAD'].value_counts())

print(df.loc[0, 'NOX'])
print(df.loc[[0,1,2], 'NOX'])
print(df.loc[0:2, 'NOX'])
print(df.loc[0:2, 'NOX':'AGE'])     # remember: slicing is inclusive


df2 = df.set_index('CRIM')
print(df2)
print(df2.index)
print(df2.loc[0.10959])

df.set_index('CRIM', inplace=True)
print(df)
df.reset_index(inplace=True)
print(df)


# FILTERS
filt = (df['RAD'] == 1)
print(df[filt])
print(df.loc[filt])
print(df.loc[filt, 'NOX'])

# & for and, | for or
filt2 = (df['RAD'] == 1) | (df['RAD'] == 2)
print(df.loc[filt2, 'RAD'])

# opposite of a filter
print(df.loc[~filt2, 'RAD'])






sys.exit()



# Formatting with f-strings
a = 10
b = 20
print(f'a is {a} and b is {b}')

# Filter filenames in a folder
import os, glob
os.chdir('C:/GitHub')
for file in glob.glob('*.jpg'):
    print(file)

# Fizzbuzz

# Fibonacci
a, b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a+b

# Dictionary
my_dict = {'name': 'Bronx', 'age': '2', 'occupation': 'Coreys Dog'}
for key,val in my_dict.items():
    #val = my_dict[key]
    print("My {} is {}".format(key,val))

# Set
my_set = {10, 20, 30, 10, 20, 40, 10}
print(my_set)

# Tuples vs Lists (tuples are immutable)
t1 = (1, 2, 3, 4)
l1 = [1, 2, 3, 4]
l1[0] = 0
#t1[0] = 0      # ERROR!

# List Comprehension
my_list = [1,2,3,4,5,6,7,8,9,10]
squares = [num*num for num in my_list]
print(squares)

# Generators
def fib(num):
    a,b = 0,1
    for i in range(0, num):
        yield "{}: {}".format(i+1, a)
        a,b = b,a+b
for item in fib(10):
    print(item)

# OOP
class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print("My name is {}".format(self.name))

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("...And I am {}".format(self.hero_name))

corey = Person('Corey')
corey.reveal_identity()
wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_identity()


# Assert
a = 10
assert (a == 10), 'a is not 10!'
print(type(corey))
assert (type(corey)=='__main__.Person'), 'Not a person!'





