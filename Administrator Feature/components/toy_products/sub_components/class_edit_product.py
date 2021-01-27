import tkinter as tk
from tkinter import messagebox

from api.database_management import DatabaseAPI
from tools.window_size import center_window_on_screen


class EditProductWindow(tk.Frame):

    def __init__(self, parent, controller, list_name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.list_name = list_name

        self.init_edit_product_gui()

    # Function which initialise the GUI
    def init_edit_product_gui(self):
        self.product_list_value = self.list_name.get(self.list_name.curselection())
        self.win = tk.Toplevel()
        self.win.title("Edit product")
        center_window_on_screen(250, 500, self.winfo_screenwidth(), self.winfo_screenheight(), self.win)

        #   Title
        self.label = tk.Label(self.win, text='Edit product', font=self.controller.title_font).pack(pady=20)

        #   Product ID
        self.category_code_label = tk.Label(self.win, text=f"Product code: {self.__get_id(self.product_list_value, 2)}")
        self.category_code_label.pack()

        #   Product name
        self.product_name_label = tk.Label(self.win, font=self.controller.label_font, text="Product name:")
        self.product_name_label.pack(pady=(20, 5))

        self.product_name_entry = tk.Entry(self.win, name='product_name_entry')

        # Make default entry
        self.product_name_entry.insert(0, self.product_list_value)

        self.product_name_entry.pack()

        # Product Category ID
        self.product_categories = []
        DatabaseAPI().get_list('CategoryName', 'Categories', 0, self.product_categories, 2)
        old_product_id = self.__get_id(self.product_list_value, 1)
        self.product_categories.reverse()

        self.new_product_id = tk.StringVar()
        self.new_product_id.set(self.product_categories[old_product_id - 1])

        self.product_category_label = tk.Label(self.win, text="Category:")
        self.product_category_label.pack()
        self.product_category_menu = tk.OptionMenu(self.win, self.new_product_id, *self.product_categories)
        self.product_category_menu.pack(pady=(0, 0))

        #   Product price
        self.product_price_label = tk.Label(self.win, font=self.controller.label_font, text="Product price:")
        self.product_price_label.pack(pady=(20, 5))

        self.product_price_entry = tk.Entry(self.win, name='product_price_entry')

        # Make default entry
        self.old_product_price = self.__get_id(self.product_list_value, 4)
        self.product_price_entry.insert(0, self.old_product_price)

        self.product_price_entry.pack()

        #   Product stock
        self.product_stock_label = tk.Label(self.win, font=self.controller.label_font, text="Product stock:")
        self.product_stock_label.pack(pady=(20, 5))

        self.product_stock_entry = tk.Entry(self.win, name='product_stock_entry')

        # Make default entry
        self.old_product_stock = self.__get_id(self.product_list_value, 5)
        self.product_stock_entry.insert(0, self.old_product_stock)

        self.product_stock_entry.pack()

        #   Cancel button
        self.cancel_button = tk.Button(self.win, text="Cancel", command=self.win.destroy)
        self.cancel_button.pack(side='right', padx=(0, 60))

        #   Save button
        self.save_button = tk.Button(self.win, text="Save", name='save_button',
                                     command=lambda: self.save_edited_product_button(self.product_list_value,
                                                                                     self.product_name_entry,
                                                                                     self.new_product_id,
                                                                                     self.product_price_entry,
                                                                                     self.product_stock_entry,
                                                                                     self.win,
                                                                                     self.list_name))
        self.save_button.pack(side='left', padx=(60, 0))

    # Gets category id value
    @staticmethod
    def __get_id(chosen_value, id_type):
        # Get Category ID
        if id_type == 1:
            result = DatabaseAPI().get_item_id('Products', 'CategoryID', 'ProductName', chosen_value)
            return result
        # Get product ID
        elif id_type == 2:
            result = DatabaseAPI().get_item_id('Products', 'ProductID', 'ProductName', chosen_value)
            return result
        # Get categories names for drop down menu
        elif id_type == 3:
            result = DatabaseAPI().get_item_id('Categories', 'CategoryID', 'CategoryName', chosen_value)

            return result
        # Get product price
        elif id_type == 4:
            result = DatabaseAPI().get_item_id('Products', 'ProductPrice', 'ProductName', chosen_value)

            return result
        #     Get product stock
        elif id_type == 5:
            result = DatabaseAPI().get_item_id('Products', 'ProductStock', 'ProductName', chosen_value)

            return result

    # Saves user entries and checks if the user wrote the name that already exist
    def save_edited_product_button(self, old_name, new_name, new_category, new_price,
                                   new_stock, window, list_name):
        new_category_value = self.__get_id(new_category.get(), 3)
        new_price_value = new_price.get()
        new_name_value = new_name.get()
        new_stock_value = new_stock.get()

        # Checks if new name is exist in database
        if DatabaseAPI().repeat_checker("CategoryName", "Categories", new_category_value) == 1:
            messagebox.showerror('Error', f'Category {new_category_value} already exist')
            # Edits category
        else:
            try:
                for value in (new_category_value, new_price_value, new_name_value, new_stock_value):
                    if value == '':
                        raise ValueError('1')

                for value in (new_price_value, new_stock_value):
                    if not str.isdecimal(value):
                        raise ValueError('2')

                # Set product price
                DatabaseAPI().edit_item('Products', 'ProductPrice', 0, new_price_value, 'ProductName', old_name, 2)
                # Set product name
                DatabaseAPI().edit_item('Products', 'ProductName', old_name, new_name_value)
                # Set product category
                DatabaseAPI().edit_item('Products', 'CategoryID', 0, new_category_value, 'ProductName', old_name, 2)
                # Set product stock
                DatabaseAPI().edit_item('Products', 'ProductStock', 0, new_stock_value, 'ProductName', new_name_value, 2)
                window.destroy()
                self.__edit_product_success(new_name_value)
                DatabaseAPI().update_list("ProductName", "Products", list_name)
                list_name.select_set(0)  # First item selected by default

            # Calls Error
            except ValueError as ve:

                error = int(ve.args[0])

                if error == 1:
                    tk.messagebox.showerror('Error', 'You can\'t left empty fields')
                elif error == 2:
                    tk.messagebox.showerror('Error', 'The stock and price fields should be numeral')

    # Message box about successful changing of category
    @staticmethod
    def __edit_product_success(product_name):
        messagebox.showinfo('Success', f'Product {product_name} was successfully edited')
