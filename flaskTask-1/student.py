import sqlite3


connection = sqlite3.connect("student.db")
print("Opened database successfully")
cursor = connection.cursor()
createTable = "CREATE TABLE IF NOT EXISTS students (student_id integer primary key autoincrement, student_name text " \
              "not null, student_email text not null, student_phoneno integer not null, student_dept text not null )"
cursor.execute(createTable)
print("Table created successfully!")
connection.close()
