import tkinter as tk
from tkinter import messagebox

from api.database_management import DatabaseAPI
from tools.window_size import center_window_on_screen


class AddProductWindow(tk.Frame):

    def __init__(self, parent, controller, list_name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.list_name = list_name

        self.init_add_product_gui()

    # Function which initialise the GUI
    def init_add_product_gui(self):
        self.win = tk.Toplevel()
        self.win.title("Add Product")
        center_window_on_screen(350, 350, self.winfo_screenwidth(), self.winfo_screenheight(), self.win)

        # Title
        self.label = tk.Label(self.win, text='Create product', font=self.controller.title_font).pack(pady=20)

        # Product name
        self.product_name_label = tk.Label(self.win, text="Product name:")
        self.product_name_label.pack()

        self.product_name_entry = tk.Entry(self.win, name='product_name_entry')
        self.product_name_entry.pack(pady=(0, 0))

        self.selected = tk.StringVar()
        self.selected.set('Category ID')
        self.opt = []

        DatabaseAPI().get_list('CategoryName', 'Categories', 0, self.opt, 2)

        # Product Category ID
        self.product_category_label = tk.Label(self.win, text="Category:")
        self.product_category_label.pack()

        self.product_category_menu = tk.OptionMenu(self.win, self.selected, *self.opt)
        self.product_category_menu.pack(pady=(0, 0))

        # Product Price
        self.product_price_label = tk.Label(self.win, text="Product price:")
        self.product_price_label.pack()

        self.product_price_entry = tk.Entry(self.win, name='product_price_entry')
        self.product_price_entry.pack(pady=(0, 0))

        # Product Stock
        self.product_stock_label = tk.Label(self.win, text="Product stock:")
        self.product_stock_label.pack()

        self.product_stock_entry = tk.Entry(self.win, name='product_stock_entry')
        self.product_stock_entry.pack(pady=(0, 0))

        # Exit button
        self.exit_button = tk.Button(self.win, text="Exit", command=self.win.destroy)
        self.exit_button.pack(side='right', padx=(0, 140))

        # Add button
        self.add_button = tk.Button(self.win, text="Add", command=lambda: self.add_product_button(), name='add_button')
        self.add_button.pack(side='left', padx=(140, 0))

    # Get category id
    @staticmethod
    def __get_category_id(menu):
        chosen_value = menu.get()
        try:
            result = DatabaseAPI().get_item_id('Categories', 'CategoryID', 'CategoryName', chosen_value)
            return result
        except TypeError:
            return ''

    # Adds product to the database
    def add_product_button(self):
        product_name = self.product_name_entry.get()
        category_name = self.__get_category_id(self.selected)
        price_value = self.product_price_entry.get()
        stock_value = self.product_stock_entry.get()

        # Checks if entry is already exist in database
        if DatabaseAPI().repeat_checker("ProductName", "Products", product_name) == 1:
            messagebox.showerror('Error', f'Product {product_name} already exist')
        else:
            try:
                # Checks empty fields
                for value in (product_name, category_name, price_value, stock_value):
                    if value == '':
                        raise ValueError('Empty Fields')

                # Creates product in database
                DatabaseAPI().create_product(product_name, category_name, price_value, stock_value)
                self.win.destroy()
                self.__product_success(product_name)
                DatabaseAPI().update_list("ProductName", "Products", self.list_name)
                self.list_name.select_set(0)  # First item selected by default

            except:
                tk.messagebox.showerror('Error', 'You can\'t left empty fields')

    # Message box when product were added successfully
    @staticmethod
    def __product_success(product_name):
        messagebox.showinfo('Success', f'Product {product_name} created')
