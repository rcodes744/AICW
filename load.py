import pandas as pd
data=pd.read_csv('products.csv')
data.read()
data.info()

print(data['Price'])