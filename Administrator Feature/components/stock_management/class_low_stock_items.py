import tkinter as tk

from api.database_management import DatabaseAPI
from components.stock_management.sub_components.class_show_info_window import ShowInfoWindow
from tools.saving_tool import SaveFile


class LowStockPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.init_low_stock_list_gui()

    # Function which initialise the GUI
    def init_low_stock_list_gui(self):
        self.controller.title('Stock management')

        #   Title
        self.label = tk.Label(self, text='Low stock list', font=self.controller.title_font).pack(pady=20)

        #   Categories list
        self.low_stock_product_list = tk.Listbox(self, height=10, width=50, selectmode='SINGLE',
                                                 name='low_stock_product_list')

        # Items
        DatabaseAPI().get_list("ProductName", "Products", 'ProductStock <20', self.low_stock_product_list, 1, 2)

        self.low_stock_product_list.select_set(0)  # First item selected by default
        self.low_stock_product_list.pack(pady=(0, 20))

        #   Back button
        self.back_button = tk.Button(self, text='Back', command=lambda: self.back_button_function())
        self.back_button.pack(pady=10, padx=10, side='left')

        #   Info button
        self.info_button = tk.Button(self, text='Info',
                                     command=lambda: self.get_info(self.controller, self.low_stock_product_list))
        self.info_button.pack(pady=10, padx=10, side='right')

        #   Save button
        save_button = tk.Button(self, text='Save',
                                command=lambda: SaveFile(self).save_low_stock_file())

        save_button.pack(pady=10, padx=10, side='right')

    def back_button_function(self):
        self.controller.show_frame(1)

    def get_info(self, controller, list_name):
        ShowInfoWindow(self, controller, list_name)
