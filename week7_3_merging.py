# Import Pandas. 
import pandas as pd

# Create the DataFrames.
cars_3 = pd.DataFrame({'VW': ['Polo', 'T-Cross', 'Tiguan', 'Toureg'],
                       'Toyota': ['Agya', 'Corolla', 'Rav4', 'Land Cruiser'],
                       'Honda': ['Brio', 'Jazz', 'HRV', 'CRV'], 
                       'BMW': ['BMW1', 'BMW2', 'BMW3', 'BMW4']}, 
                      index=[0, 1, 2, 3])

motorcycles_3 = pd.DataFrame({'VW': ['-', '-', '-', '-'],
                              'Toyota': ['-', '-', '-', '-'],
                              'Honda': ['Shine', 'Activa',
                                        'Comfort Travel',
                                        'Adventure Sport'], 
                              'BMW': ['Sport', 'Roadster',
                                      'Heritage', 'Adventure']}, 
                             index=[0, 1, 2, 3])

# View the DataFrame.
print(cars_3)
print(motorcycles_3)


products_3 = cars_3.merge(motorcycles_3)

print(products_3)


#Read the CSV files
classlist_a = pd.read_csv('./week7csv/classlist_a.csv')
classlist_b = pd.read_csv('./week7csv/classlist_b.csv')
classlist_c = pd.read_csv('./week7csv/classlist_c.csv')
classlist_d = pd.read_csv('./week7csv/classlist_d.csv')


classlist_ab = pd.merge(classlist_a,classlist_b,
                        how='inner', on='Student number')

                        
classlist_ab_outer = pd.merge(classlist_a,classlist_b,
                        how='outer', on='Student number')


classlist_cd_outer = pd.merge(classlist_c,classlist_d,
                        how='outer', on='Student number')


classlist_final = pd.merge(classlist_ab_outer,classlist_cd_outer,
                        how='outer', on='Student number')
                        


# The shape() method returns the number of columns and rows of the DataFrame.
print(classlist_final.shape)

print(classlist_final)