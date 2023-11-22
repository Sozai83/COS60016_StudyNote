import pandas as pd
import numpy as np


# data = pd.DataFrame([
#     ['Andy','Melbourne','30245'],
#     ['Claire','Sydney','30038'],
#     ['Ash','Delhi','10001'],
#     ['Divya','Kolkata','70007'],
#     ['Monika','London','43023']
# ], columns=['Name','City', 'Pin']
# )

# print(data)

# # Create a dictionary.
# data2 = {"Melbourne":"Australia",
#         "Sydney":"Australia",
#         "Delhi":"India",
#         "Kolkata":"India",
#         "London":"United Kingdom"}


# # Adding column
# data['Country'] = data['City'].map(lambda x: data2[x])

# print(data)


# # Filtering data

# data = pd.DataFrame(np.random.randint(5, 1000, size=(1000,4)),
#                     columns=['Col A','Col B','Col C','Col D'])

# # print(data.shape)
# # print(data.head())
# # print(data.describe())


# # data2 = data[data['Col D'] < 400]
# # print(data2.head())


# data3 = data.filter(['Col B', 'Col C'])

# print(data3.shape)
# print(data3.head())

# # This can be only used for index
# # data4 = data[data.loc[['Col B''Col C']]]

# # print(data4.shape)
# # print(data4.head())

# data4 = data.loc[data['Col A'] > 600]
# data5 = data[data['Col A'] > 600]

# print(data4.shape)
# print(data4.head())


# print(data5.shape)
# print(data5.head())


# Remove Dupes

data = pd.DataFrame({
    'k1': ['A']*3 + ['B']* 4,
    'k2': [1,1,2,2,3,3,4]
})

print(data)

print(data.drop_duplicates())

# Remove duplicates in k1
print(data.drop_duplicates('k1'))