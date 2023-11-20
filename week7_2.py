# Import Pandas and NumPy libraries.
import pandas as pd
import numpy as np

# Create a Pandas Series.
data = pd.Series(np.random.uniform(size=9),
index=[["a", "a", "a", "b", "b", "c", "c", "d", "d"],
       [1, 2, 3, 1, 3, 1, 2, 2, 3]])

# View the output.
# print(data.index)
# print(data)
# print(data["b"])
# print(data["b":"c"])
# print(data.loc[["a","c"]])
# print(data.loc[:,3])

print(data)
print(data.unstack())
print(data.unstack().stack())