import tkinter as tk

from api.database_management import DatabaseAPI
from components.toy_products.sub_components.class_add_product import AddProductWindow
from components.toy_products.sub_components.class_delete_product import DeleteProductWindow
from components.toy_products.sub_components.class_edit_product import EditProductWindow
from tools.saving_tool import SaveFile


class StockTakingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.init_stock_taking_list_gui()

    # Function which initialise the GUI
    def init_stock_taking_list_gui(self):
        self.controller.title('Stock management')

        #   Label
        self.label = tk.Label(self, text='Product list', font=self.controller.title_font).pack(pady=20)

        #   Categories list
        self.product_list = tk.Listbox(self, height=10, width=50, selectmode='SINGLE')

        # Items
        DatabaseAPI().get_list("ProductName", "Products", 0, self.product_list)

        self.product_list.select_set(0)  # First item selected by default
        self.product_list.pack(pady=(0, 20))

        #   Back button
        self.back_button = tk.Button(self, text='Back', command=lambda: self.back_button_function())
        self.back_button.pack(pady=10, padx=10, side='left')

        #   Delete button
        self.delete_button = tk.Button(self, text='Delete',
                                       command=lambda: self.delete_product_button())
        self.delete_button.pack(pady=10, padx=10, side='right')

        #   Edit button
        self.edit_button = tk.Button(self, text='Edit', command=lambda: self.edit_product_button())
        self.edit_button.pack(pady=10, padx=10, side='right')

        #   Add button
        self.add_button = tk.Button(self, text='Add', command=lambda: self.add_product_button())
        self.add_button.pack(pady=10, padx=10, side='right')

        #  Save button
        self.save_button = tk.Button(self, text='Save', name='save_button',
                                     command=lambda: self.save_stock_taking_button())
        self.save_button.pack(pady=10, padx=10, side='right')

    # Create product, button function
    def add_product_button(self):
        AddProductWindow(self, self.controller, self.product_list)

    #  Edit product function
    def edit_product_button(self):
        EditProductWindow(self, self.controller, self.product_list)

    # Delete product, button function
    def delete_product_button(self):
        DeleteProductWindow(self, self.controller, self.product_list)

    # Saves file
    def save_stock_taking_button(self):
        SaveFile(self).save_stock_taking_file()

    # Back button function
    def back_button_function(self):
        self.controller.show_frame(1)
