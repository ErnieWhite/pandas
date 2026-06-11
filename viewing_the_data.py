import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
print('+' * 20)
print(df.tail(10))
