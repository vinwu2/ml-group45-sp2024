import pandas as pd


file_path = r"C:\Users\rohit\Downloads\teams.csv"


df = pd.read_csv(file_path)


df.drop(columns=['LEAGUE_ID', 'MIN_YEAR', 'MAX_YEAR', 'ABBREVIATION', 'YEARFOUNDED', 'CITY', 'ARENA', 'ARENACAPACITY', 'OWNER', 'GENERALMANAGER', 'HEADCOACH', 'DLEAGUEAFFILIATION'], inplace=True)


df.to_excel(r'C:\Users\rohit\Downloads\TeamNames.xlsx', index=False, engine='openpyxl')
