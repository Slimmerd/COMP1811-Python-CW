import tkinter as tk


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.init_menu_gui()

    # Function which initialise the GUI
    def init_menu_gui(self):
        self.controller.title('Administrator panel menu')

        self.label = tk.Label(self, text="Administrator menu", font=self.controller.title_font)
        self.label.pack(side="top", pady=20)

        # Category List Button
        self.category_list_button = tk.Button(self, text='Category List', height=2, width=20,
                                              command=lambda: self.controller.show_frame(3))
        self.category_list_button.pack(pady=(0, 20))

        # Product list button
        self.product_list_button = tk.Button(self, text='Product List', height=2, width=20,
                                             command=lambda: self.controller.show_frame(2))
        self.product_list_button.pack(pady=(0, 20))

        # Stock taking button
        self.stock_taking_button = tk.Button(self, text='Stock taking', height=2, width=20,
                                             command=lambda: self.controller.show_frame(4))
        self.stock_taking_button.pack(pady=(0, 20))

        # Low stock list button
        self.low_stock_list_button = tk.Button(self, text='Low stock List', height=2, width=20,
                                               command=lambda: self.controller.show_frame(5))
        self.low_stock_list_button.pack(pady=(0, 20))

        # Exit button
        self.exit_button = tk.Button(self, text='Exit', command=lambda: self.controller.quit())
        self.exit_button.pack(pady=10, padx=10, side='right')
