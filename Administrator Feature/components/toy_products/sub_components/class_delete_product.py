import tkinter as tk
from tkinter import messagebox

from api.database_management import DatabaseAPI


class DeleteProductWindow(tk.Frame):

    def __init__(self, parent, controller, list_name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.list_name = list_name

        self.init_delete_product_gui()

    # Function which initialise the GUI
    def init_delete_product_gui(self):
        product_list_value = self.list_name.get(self.list_name.curselection())
        self.__delete_product(product_list_value, self.list_name)
        messagebox.showinfo('Success', f'Product {product_list_value} deleted')

    @staticmethod
    def __delete_product(value, list_name):
        DatabaseAPI().delete_item('Products', 'ProductName', value)
        DatabaseAPI().update_list("ProductName", "Products", list_name)
        list_name.select_set(0)  # First item selected by default
