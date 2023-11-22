# Import libraries.
import pandas as pd
import numpy as np

# Create the DataFrame.
animals = pd.DataFrame([('bird', 'Falconiformes', 389.),
                        ('bird', 'Psittaciformes', 24.0),
                        ('mammal', 'Carnivora', 80.2),
                        ('mammal', 'Primates'),
                        ('mammal', 'Carnivora', 58)],
                    # Specify the index.
                    index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                    # Specify the columns.
                    columns=['class', 'order', 'max_speed'])

# View the DataFrame.
print(animals)


grp_class = animals.groupby('class')
grp_class_order = animals.groupby(['class', 'order'])


print(grp_class)
print(grp_class_order)

print(grp_class.sum())
print(grp_class_order.sum())


print(grp_class.max())
print(grp_class_order.max())


print(grp_class.min())
print(grp_class_order.min())