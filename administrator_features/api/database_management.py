import csv
import os
import sqlite3
import tkinter as tk


class DatabaseAPI:
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(__file__))
        self.database_path = self.path + '/database/all_about_toys.db'

        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()

    # Makes list from database for specific column
    def get_list(self, column, table, condition, list_name, list_type=1, database_type=1):

        if database_type == 1:
            database = self.cursor.execute(f"SELECT {column} FROM {table}")

        elif database_type == 2:
            database = self.cursor.execute(f"SELECT {column} FROM {table} WHERE {condition}")

        num_rows = database.fetchall()

        for item in num_rows:
            if list_type == 1:
                list_name.insert(tk.END, item[0])
            elif list_type == 2:
                list_name.insert(0, item[0])

        self.connection.commit()
        self.connection.close()

    # Updates list
    def update_list(self, column, table, list_name):

        list_name.delete(0, tk.END)
        self.get_list(column, table, 0, list_name)

    # Checks if entry is already exist in the list
    def repeat_checker(self, column_name, table_table, entry_data):

        self.cursor.execute(f"select {column_name} from {table_table} where {column_name}=?", (entry_data,))
        data = self.cursor.fetchall()

        self.connection.commit()
        self.connection.close()

        if not data:
            # Data not found returns 0
            return 0
        else:
            # Data found returns 1
            return 1

    # Create category
    def create_category(self, category_name):

        self.cursor.execute(f"INSERT INTO Categories (CategoryName) VALUES ('{category_name}')")

        self.connection.commit()
        self.connection.close()

    # Create product
    def create_product(self, product_name, category_id, product_price, product_stock):

        self.cursor.execute(
            f"INSERT INTO Products (ProductName,CategoryID,ProductPrice,ProductStock) VALUES ('{product_name}',{category_id},{product_price},{product_stock})")

        self.connection.commit()
        self.connection.close()

    # Get's id's from the table
    def get_item_id(self, table_name, column_name, user_entry, user_choice):

        self.cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE {user_entry}=?", (user_choice,))

        rows = self.cursor.fetchone()

        self.connection.commit()
        self.connection.close()

        id_check = rows[0]
        return id_check

    # Delete item from database
    def delete_item(self, table_name, column_name, chosen_item):

        self.cursor.execute(f"DELETE FROM {table_name} WHERE {column_name}=?", (chosen_item,))

        self.connection.commit()
        self.connection.close()

    #  Edit item in database
    def edit_item(self, table_name, column_name, old_value, new_value, product_name=0, new_product_name=0, type_id=1):

        if type_id == 1:
            self.cursor.execute(f"UPDATE {table_name} SET {column_name} = ? WHERE {column_name} = ?",
                                (new_value, old_value))
        elif type_id == 2:
            self.cursor.execute(f"UPDATE {table_name} SET {column_name} = ? WHERE {product_name} = ?",
                                (new_value, new_product_name))

        self.connection.commit()
        self.connection.close()

    # Saves csv file in chosen filepath
    def save_database_file(self, table_name, file_name, file_path, saving_type=1):

        if saving_type == 1:
            self.cursor.execute(f"select * from {table_name}")
        elif saving_type == 2:
            self.cursor.execute(f"SELECT ProductName FROM Products WHERE ProductStock <20")

        if os.path.exists(file_path):
            with open(file_path + "/" + file_name + '.csv', "w") as csv_file:
                csv_writer = csv.writer(csv_file, delimiter="\t")

                # Writes headers
                csv_writer.writerow([i[0] for i in self.cursor.description])
                # Writes other data
                csv_writer.writerows(self.cursor)
        else:
            print('Error')

        self.connection.close()

    # Gets chosen item stock
    def get_item_stock(self):

        low_stock = self.cursor.execute(f"SELECT ProductName FROM Products WHERE ProductStock <20")

        low_stock_list = []
        for item in low_stock:
            low_stock_list.append(item[0])

        self.connection.close()
        return low_stock_list

    # Get item id (used for unit tests)
    def tester_get_item_id(self,table_name, user_entry, user_choice):

        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {user_entry}=?", (user_choice,))

        # rows = cursor.fetchone()
        rows = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()

        id_check = rows[0]

        return id_check
