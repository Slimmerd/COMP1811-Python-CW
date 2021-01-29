import sqlite3
from contextlib import closing

connection = sqlite3.connect('all_about_toys.db')
cursor = connection.cursor()

"""USED ONLY FOR CREATING DATABASE AND TESTING IF IT WAS CREATED SUCCESSFULLY"""


# Function creates two tables
def create_tables():
    cursor.execute("CREATE TABLE Categories (CategoryID INTEGER PRIMARY KEY, CategoryName TEXT)")
    cursor.execute(
        "CREATE TABLE Products (ProductID INTEGER PRIMARY KEY, CategoryID INTEGER REFERENCES Categories(CategoryID), ProductName TEXT, ProductPrice INTEGER, ProductStock INTEGER )")
    connection.commit()
    close_table()
    main()


# Function inserts test values to the table
def test_insert_values():
    # cursor.execute("INSERT INTO Categories (CategoryName) VALUES ('Mechanical')")
    cursor.execute(
        "INSERT INTO Products (CategoryID, ProductName, ProductPrice, ProductStock) VALUES (1,'Big Dragon',39,259)")
    connection.commit()
    close_table()
    main()


# Check data in the table
def check_table_values():
    rows1 = cursor.execute(
        "SELECT CategoryID, CategoryName FROM Categories").fetchall()
    rows2 = cursor.execute(
        "SELECT ProductID, CategoryID, ProductName, ProductPrice, ProductStock FROM Products").fetchall()

    print(rows1)
    print('')
    print(rows2)

    main()


# Closes table
def close_table():
    with closing(sqlite3.connect("all_about_toys.db")) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute('SELECT 1').fetchall()


def main():
    print('Choose option')
    print('1 - Create Table \n 2 - Insert test values \n 3 - Show table \n 4 - Exit')
    user_input = int(input('Write your choice:'))

    if user_input == 1:
        create_tables()
    elif user_input == 2:
        test_insert_values()
    elif user_input == 3:
        check_table_values()
    elif user_input == 4:
        exit()
    else:
        print('Error')


main()
