import pandas as pd
import pymysql as py

# Load Excel data
excel_file = "C:/Users/tanve/Desktop/New Microsoft Excel Worksheet.xlsx"
df = pd.read_excel(excel_file, sheet_name="Sheet3")  # Load data from sheet3

# Connect to MySQL
connection = py.connect(
    host="localhost",
    user="root",
    password="12345",
    database="radha"
)
cursor = connection.cursor()

# Automatically create table based on the DataFrame columns
columns = ", ".join(df.columns)  # Get column names
types = ", ".join([f"{col} VARCHAR(255)" for col in df.columns])  # Assuming text data for simplicity
create_table_query = f"CREATE TABLE your_table ({types});"
cursor.execute(create_table_query)

# Insert data into MySQL table
for i, row in df.iterrows():
    sql = f"INSERT INTO your_table ({columns}) VALUES ({', '.join(['%s' for _ in row])})"
    cursor.execute(sql, tuple(row))

connection.commit()
cursor.close()
connection.close()

print("Table created and data inserted successfully!")
