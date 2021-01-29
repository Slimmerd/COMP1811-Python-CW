import tkinter as tk
from tkinter import messagebox

from api.database_management import DatabaseAPI


class DeleteCategoryWindow(tk.Frame):

    def __init__(self, parent, controller, list_name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.list_name = list_name

        self.init_delete_product_gui()

    # Function which initialise the GUI
    def init_delete_product_gui(self):
        category_list_value = self.list_name.get(self.list_name.curselection())
        self.__delete_category(category_list_value, self.list_name)
        messagebox.showinfo('Success', f'Category {category_list_value} deleted')

    # Deletes chosen category and updates the list of elements
    @staticmethod
    def __delete_category(value, list_name):
        DatabaseAPI().delete_item('Categories', 'CategoryName', value)
        DatabaseAPI().update_list("CategoryName", "Categories", list_name)
        list_name.select_set(0)  # First item selected by default
