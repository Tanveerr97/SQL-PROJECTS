import pandas as pd
import pymysql as py
excel_file = r"C:\Users\tanve\Desktop\Data set\shopping_trends.csv"
data = pd.read_csv(excel_file)
connection = py.connect(host="localhost", user="root", password="12345", database="mm")
cursor = connection.cursor()
def sanitize_column(col_name):
    return f'`{col_name.replace(" ", "_").replace("`", "``")}`'
columns = data.columns
type=[]
for col in columns:
    sanitize_col = sanitize_column(col)
    dtype = data[col].dtype
    if dtype == 'int64':
        type.append(f"{sanitize_col} INT")
    elif dtype == 'float64':
        type.append(f"{sanitize_col} FLOAT")
    else:
       type.append(f"{sanitize_col} VARCHAR(255)")

type_str = ', '.join(type)

create_table_query = f"CREATE TABLE IF NOT EXISTS abc ({type_str})"
cursor.execute(create_table_query)
for i, row in data.iterrows():
    sql = f"INSERT INTO abc ({', '.join([sanitize_column(col) for col in columns])}) VALUES ({', '.join(['%s']*len(row))})"
    cursor.execute(sql, tuple(row))
connection.commit()

cursor.close()
connection.close
