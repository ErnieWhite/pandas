import pandas as pd

pd.options.display.max_rows =  9999

print(pd.options.display.max_rows)
print("-" * 20)

df = pd.read_csv('data.csv')

print(df)
