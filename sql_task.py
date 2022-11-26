import sqlite3
def get_connection():
    connection = sqlite3.connect('teachers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()


def create_table_school():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = """CREATE TABLE School 
( 
School_Id INTEGER NOT NULL PRIMARY KEY,
School_Name TEXT NOT NULL,
Place_Count INTEGER NOT NULL
); """
        cursor.execute(query)
        connection.commit()
        connection.close()
    except (Exception, sqlite3.Error) as error:
        print('Ошибка при создании таблицы:', error)

create_table_school

def fill_table_school():
    try:
        connection = sqlite3.connect()
        cursor = connection.cursor()
        query = """INSERT INTO School (School_Id, School_Name
        VALUES
('1', 'Протон', 200),
('2', 'Преспектива', 300),
('3', 'Спектр', 400),
('4', 'Содружество', 500);"""
        cursor.execute(query)
        connection.commit()
        connection.close()
    except (Exception, sqlite3.Error) as error:
        print('Ошибка при наполнении таблицы:', error)


fill_table_school()
def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def create_table():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = ("""CREATE TABLE Students
(
Student_id INTEGER NOT NULL PRIMARY KEY,
Student_name varchar(100) NOT NULL,
School_id INTEGER NOT NULL
);""")
    
    cursor.execute(query)
    connection.commit()
    close_connection(connection)

  except (Exception, sqlite3.Error) as error:
    print('Ошибка при создании таблицы:', error)

def fill_table():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = ("""INSERT INTO Students(student_id, student_name, school_id)
                VALUES
                	  (201, "Иван", 1),
                    (202, "Петр", 2),
                    (203, "Анастасия", 3),
                    (204, "Игорь", 4);""")
    
    cursor.execute(query)
    
    connection.commit()
    close_connection(connection)

  except (Exception, sqlite3.Error) as error:
    print('Ошибка при заполнении таблицы:', error)

def get_student(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    query = ("""SELECT st.student_id, st.student_name, sc.school_id, sc.school_name
                FROM Students AS st
                JOIN School AS sc
                ON st.School_id = sc.School_Id
                WHERE st.student_id = ?""")
    cursor.execute(query, (student_id, ))
    records = cursor.fetchall()
    print(f'Студент №{student_id}:\n')
    
    for row in records:
      print('ID студента:', row[0])
      print('Имя:', row[1])
      print('ID школы:', row[2])
      print('Название школы:', row[3],'\n')
    
    close_connection(connection)
  
  except (Exception, sqlite3.Error) as error:
    print('Ошибка в получении данных по студенту: ', error)

print('SQL: Самостоятельная работа')
create_table()
fill_table()
get_student(202)