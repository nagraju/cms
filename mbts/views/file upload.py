import sqlite3
import pandas as pd
file=pd.read_csv('tmp\\attendence.csv')
#file.columns=file.columns.str.strip()
con=sqlite3.connect('db.sqlite3')
file.to_sql('students',con,if_exists='replace')

import sqlite3
import pandas as pd
file=pd.read_csv('tmp\\Marks.csv')
#file.columns=file.columns.str.strip()
con=sqlite3.connect('db.sqlite3')
file.to_sql('students',con,if_exists='replace')


file=pd.read_csv('tmp\\Unit1marks.csv')
#file.columns=file.columns.str.strip()
con=sqlite3.connect('db.sqlite3')
file.to_sql('students',con,if_exists='replace')




