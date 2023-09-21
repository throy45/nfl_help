import nfl_data_py as nfl
import pandas as pd


# Create a DataFrame of all the turnover plays
df = pd.DataFrame(nfl.import_pbp_data([2023]))

# Filter the DataFrame to only include turnover plays
turnover_plays = df[(df['interception'] == 1) | (df['fumble'] == 1)]

# Group by 'week' and 'game_id' and count the turnovers
turnovers_by_game = turnover_plays.groupby(
    ['week', 'game_id']).size().reset_index(name='turnovers_count')

# Sort the grouped DataFrame by 'turnovers_count' in descending order
sorted_turnovers = turnovers_by_game.sort_values(
    by=['week', 'turnovers_count'], ascending=[True, False])

# Now 'sorted_turnovers' contains the games ranked by most turnovers to least turnovers by week

print(sorted_turnovers)
