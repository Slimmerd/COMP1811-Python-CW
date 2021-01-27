import tkinter as tk

from api.database_management import DatabaseAPI
from tools.window_size import center_window_on_screen


class ShowInfoWindow(tk.Frame):

    def __init__(self, parent, controller, list_name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.list_name = list_name

        self.init_show_info_gui()

    # Function which initialise the GUI
    def init_show_info_gui(self):
        self.product_list_value = self.list_name.get(self.list_name.curselection())

        self.win = tk.Toplevel()
        self.win.title("Product information")
        center_window_on_screen(250, 500, self.winfo_screenwidth(), self.winfo_screenheight(), self.win)

        self.title = self.controller.title("Product information")

        #   Title frame
        self.label = tk.Label(self.win, text='Product information', font=self.controller.title_font).pack(pady=20)

        #   Product ID
        self.category_code_label = tk.Label(self.win, text="Product code:", font=self.controller.label_font)
        self.category_code_label.pack(pady=(10, 5))
        self.category_code_entry = tk.Label(self.win, text=self.__get_id(self.product_list_value, 2),
                                            name='category_code_entry')
        self.category_code_entry.pack()

        #   Product name
        self.product_name_label = tk.Label(self.win, font=self.controller.label_font, text="Product name:")
        self.product_name_label.pack(pady=(20, 5))

        self.product_name_entry = tk.Label(self.win, text=self.product_list_value, name='product_name_entry')
        self.product_name_entry.pack()

        # Product Category ID
        self.product_id = self.__get_id(self.product_list_value, 1)

        self.product_category_label = tk.Label(self.win, text="Category:", font=self.controller.label_font)
        self.product_category_label.pack(pady=(20, 5))

        self.product_category_entry = tk.Label(self.win, text=self.product_id, name='product_category_entry')
        self.product_category_entry.pack(pady=(0, 0))

        #   Product price
        self.product_price_label = tk.Label(self.win, font=self.controller.label_font, text="Product price:")
        self.product_price_label.pack(pady=(20, 5))

        self.product_price = self.__get_id(self.product_list_value, 4)

        self.product_price_entry = tk.Label(self.win, text=self.product_price, name='product_price_entry')
        self.product_price_entry.pack()

        #   Product stock
        self.product_stock_label = tk.Label(self.win, font=self.controller.label_font, text="Product stock:")
        self.product_stock_label.pack(pady=(20, 5))

        self.product_stock = self.__get_id(self.product_list_value, 5)

        self.product_stock_entry = tk.Label(self.win, text=self.product_stock, name='product_stock_entry')
        self.product_stock_entry.pack()

        #   Close button
        close_button = tk.Button(self.win, text="Close", command=self.win.destroy)
        close_button.pack(pady=(30, 0))

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
        # Get product price
        elif id_type == 4:
            result = DatabaseAPI().get_item_id('Products', 'ProductPrice', 'ProductName', chosen_value)

            return result
        #     Get product stock
        elif id_type == 5:
            result = DatabaseAPI().get_item_id('Products', 'ProductStock', 'ProductName', chosen_value)

            return result
