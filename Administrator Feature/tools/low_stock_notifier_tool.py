import tkinter as tk
from tkinter import messagebox

from api.database_management import DatabaseAPI


class LowStockNotifier:
    def __init__(self):
        self.low_stock_items = DatabaseAPI().get_item_stock()

        # If there items that low in stock it will popup the messagebox with notification
        if len(self.low_stock_items) > 0:
            tk.messagebox.showwarning('Low stock items',
                                      f'The following items are on low stock: {", ".join(self.low_stock_items)}. Please check detail information in Low Stock section')
