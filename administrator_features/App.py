import tkinter as tk
import tkinter.font as font

from components.login.class_login_frame import AuthPage
from components.menu.class_menu_frame import MenuPage
from components.stock_management.class_low_stock_items import LowStockPage
from components.stock_management.class_stock_taking import StockTakingPage
from components.toy_categories.class_category_list import CategoryListPage
from components.toy_products.class_product_list import ProductListPage
from tools.low_stock_notifier_tool import LowStockNotifier


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Fonts
        self.title_font = font.Font(family='Arial', size='18', weight='bold')
        self.label_font = font.Font(family='Arial', size='15', weight='bold')

        # Frame frame_container
        self.frame_container = tk.Frame(self)
        self.frame_container.pack(side="top", fill="both")

        # List of pages and their numbers in the self.frames list
        '''LoginPage = 0
            MenuPage = 1
            ProductListPage = 2
            CategoryListPage = 3
            StockTakingPage = 4
            LowStockPage = 5 '''
        self.frames = [AuthPage, MenuPage, ProductListPage, CategoryListPage, StockTakingPage, LowStockPage]

        # Initial frame
        self._frame = None

        # Set initial frame to LoginPage
        self.show_frame(0)

        # Center window and make proper size of it
        self.center_window_on_screen()

        # Used for notification about low stock
        self.first_start = True

    # Show a frame for the given page name
    def show_frame(self, page_number):

        frame_object = self.frames[page_number]
        new_frame = frame_object(parent=self.frame_container, controller=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

        # Low stock notification, notifies user about low stock items on first launch menu frame
        if frame_object == MenuPage and self.first_start:
            LowStockNotifier()
            self.first_start = False

    # Function which defines size of window and centres it on the screen
    def center_window_on_screen(self):
        width, height = 500, 350
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Centres windows and makes appropriate windows size
        x_cord = int((screen_width / 2) - (width / 2))
        y_cord = int((screen_height / 2) - (height / 2))
        self.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


if __name__ == "__main__":
    app = App()

    app.mainloop()
