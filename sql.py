import sqlite3
## connect ot sqllite database
connection = sqlite3.connect('student.db')
## create a cursor object to insert records into the database
cursor = connection.cursor()

## create table 
table_info = '''Create table STUDENT(NAME VARCHAR(25),
CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);'''

cursor.execute(table_info)
## Insert some records into the table
cursor.execute('''INSERT INTO STUDENT VALUES ('John', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Alice', 'Data Science', 'B', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Bob', 'Data Science', 'A', 95)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Eve', 'Data Science', 'B', 80)''')
## display all the records from the table
print('All records from the STUDENT table:')
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)
## connection close
connection.commit()
connection.close()