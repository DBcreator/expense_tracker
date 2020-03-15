import matplotlib.pyplot as plt
import pandas as pd
import _sqlite3 as db
import numpy as np

db_connection = db.connect('transaction.db')

df = pd.read_sql_query('SELECT * FROM expenses',db_connection)
print(df.head())
#print((df['category'] == 'food').count())
new_df = df.groupby(['category']).sum()
#labels = df.groupby(['category'])
new_df.plot.pie(y = 'amount', figsize=(18.5, 10.5),autopct='%1.1f%%', startangle=90)
#plt.show()
#fig.set_size_inches(18.5, 10.5)
plt.savefig('test_diagram', dpi=200)




