import pandas as pd


file_path = r"C:\Users\rohit\Downloads\TeamStats2020-2024.xls"


df = pd.read_excel(file_path)

df_sorted = df.sort_values(by='Team')

df_sorted.to_excel(r'C:\Users\rohit\Downloads\TeamStats2020-2024_sorted.xls', index=False, engine='openpyxl')
