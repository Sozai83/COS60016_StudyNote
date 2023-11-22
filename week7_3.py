import pandas as pd
import numpy as np


cars = pd.DataFrame(
    {
        'Volkswagen': ['Polo','T-Vross', 'Tiguan', 'Touareg'],
        'Toyota': ['Agya','Corolla','Rav4','Land Cruiser'],
        'Honda' : ['Brio','Jass', 'HRV','CRV'],
        'BMW' : ['BMW1','BMW2','BMW3','BMW4']
    },
    index=[0,1,2,3]
)

mortorcycles = pd.DataFrame(
    {
        'Volkswagen': ['-','-', '-', '-'],
        'Toyota': ['-','-','-','-'],
        'Honda' : ['Schine','Activa', 'Confort Travel','Adventure Sport'],
        'BMW' : ['Sport','Roadstar','Heritage','Adventure']
    }
)

print(cars)
print(mortorcycles)

products = pd.concat([cars, mortorcycles])

print(products)

cars_2 = pd.DataFrame(
    {
        'Volkswagen': ['Polo','T-Vross', 'Tiguan', 'Touareg'],
        'Toyota': ['Agya','Corolla','Rav4','Land Cruiser'],
        'Honda' : ['Brio','Jass', 'HRV','CRV'],
        'BMW' : ['BMW1','BMW2','BMW3','BMW4']
    },
    index=['car1','car2','car3','car4']
)

mortorcycles_2 = pd.DataFrame(
    {
        'Volkswagen': ['-','-', '-', '-'],
        'Toyota': ['-','-','-','-'],
        'Honda' : ['Schine','Activa', 'Confort Travel','Adventure Sport'],
        'BMW' : ['Sport','Roadstar','Heritage','Adventure']
    },
    index=['mcycle1','mcycle2','mcycle3','mcycle4']
)

product_2 = pd.concat([cars_2, mortorcycles_2])

print(product_2)


#Read the CSV files
classlist_a = pd.read_csv('./week7csv/classlist_a.csv')
classlist_b = pd.read_csv('./week7csv/classlist_b.csv')
classlist_c = pd.read_csv('./week7csv/classlist_c.csv')
classlist_d = pd.read_csv('./week7csv/classlist_d.csv')


# The head() method returns the column names and the first five rows.
# The shape() method returns the number of columns and rows of the DataFrame.
print(classlist_a.shape)
print(classlist_a.head())

print(classlist_b.shape)
print(classlist_b.head())

print(classlist_c.shape)
print(classlist_c.head())

print(classlist_d.shape)
print(classlist_d.head())
