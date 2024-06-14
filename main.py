from pydoc import describe
import psycopg2

def connect():
    conn = psycopg2.connect(dbname ="examsql", host = 'localhost',port = 5433, password = '123')

    return conn
connection = connect()
cursor = connection.cursor()

def create_user(): 
    name = input("Enter name: ") 
    age = int(input("Enter age: ")) 
    gender = input("Enter gender: ") 
    query = f"insert into users(name, age, gender) values ('{name}', {age}, '{gender}')" 
    cursor.execute(query)  
    connection.commit() 
     
def create_magazine(): 
    name = input("Enter name: ") 
    query = f"insert into magazines(name) values ('{name}')" 
    cursor.execute(query) 
    connection.commit 
     
def create_magazine_distribution(): 
    user_id = int(input("Enter user id: ")) 
    magazine_id = int(input("Enter magazine id: ")) 
    query = f"insert into magazine_distribution(user_id, magazine_id) values ({user_id}, {magazine_id})" 
    cursor.execute(query) 
    connection.commit
def view_all_magazines():
    d = f'select * from magazines'
    cursor.execute(d)
    connection.commit()
def view_all_users():
    s = f'select * from users'
    cursor.execute(s)
    connection.commit()
def start():
    print('what u want to do?')
    print('1)create_user 2)create_magazine 3)selection view 4)')