# Import Pandas and NumPy libraries.
import pandas as pd
import numpy as np

# Create the variable colours.
# Pass an array of data.
colours = pd.Series(['green', 'red', 'yellow', 'blue', 'black', 'white'])

# Print the Series.
print(colours)


# Create a list.
example_list = [1, 2, 3, 4, 5, 6]
  
# Create Series from a list.
numbers = pd.Series(example_list)

# Print the Series.
print(numbers)

# Create a dictionary.
# Specify the dictionary as dict_1.
dict_1 = {'AU':'Australian Dollar',
          'US': 'US Dollar',
          'IN': 'Indian Rupee',
          'DK': 'Danish Krone',
          'SW': 'Swiss Franc'}

# Name and create the Series.
economics = pd.Series(dict_1)

# Print the Series.
print(economics)
