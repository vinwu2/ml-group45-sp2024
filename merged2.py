import pandas as pd


team_names_path = r'C:\Users\rohit\Downloads\TeamNames.xlsx'
team_names_df = pd.read_excel(team_names_path)


games_path = r'C:\Users\rohit\Downloads\games.csv'
games_df = pd.read_csv(games_path)
games_df.drop(columns=['GAME_DATE_EST','GAME_ID', 'GAME_STATUS_TEXT', 'HOME_TEAM_ID', 'TEAM_ID_home'], inplace=True)


merged_df = pd.merge(games_df, team_names_df, left_on='VISITOR_TEAM_ID', right_on='TEAM_ID', how='inner')

df_sorted = merged_df.sort_values(by='NICKNAME')


merged_df.to_csv(r'C:\Users\rohit\Downloads\merged_away_games_teams.csv', index=False)
