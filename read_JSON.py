import pandas as pd

df = pd.read_json('data.js')

print(df.to_string())

print('=' * 20)

print(df)