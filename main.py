# this will be a sqlite connection
from pathlib import Path
import sqlite3
import pandas as pd

# Create db file. Change "my_data" to a name of your choice
Path('my_data.db').touch()

# Create a database connection and cursor to execute queries.
conn = sqlite3.connect('my_data.db')
c = conn.cursor()

# Execute a query that’ll create a users table with user_id and username columns.
c.execute('''CREATE TABLE boxscore_goalie (Game_Id int,	Player_Id int, Team_Id int, Game_Rating int, SA int, GA int, SV int, SV_percent text, TOI int, PIM int)''')


# load the data into a Pandas DataFrame
users = pd.read_csv('boxscore_goalie_summary.csv')
# write the data to a sqlite table/schema with the "boxscore_goalie" name
users.to_sql('boxscore_goalie', conn, if_exists='append', index=False)

c.execute('''SELECT * FROM boxscore_goalie''').fetchall()
