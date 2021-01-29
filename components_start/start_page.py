import os
import tkinter as tk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.init_menu_gui()

    # Function which initialise the GUI
    def init_menu_gui(self):
        self.controller.title('Start Menu')

        # Administrator panel
        self.admin_label = tk.Label(self, text="Administrator panel", font=self.controller.title_font)
        self.admin_label.pack(side="top", pady=20)

        self.admin_button = tk.Button(self,
                                      text='Open',
                                      command=lambda: os.system('python3 ./administrator_features/App.py'))
        self.admin_button.pack(pady=10)

        # Customer Panel
        self.customer_label = tk.Label(self, text="Customer panel", font=self.controller.title_font)
        self.customer_label.pack(side="top", pady=20)

        self.customer_button = tk.Button(self,
                                         text='Open',
                                         command=lambda: os.system('python3 ./customer_features/customer_main.py'))
        self.customer_button.pack(pady=10)

        # Sales staff Panel
        self.customer_label = tk.Label(self, text="Customer panel", font=self.controller.title_font)
        self.customer_label.pack(side="top", pady=20)

        self.customer_button = tk.Button(self,
                                         text='Open',
                                         command='')
        # os.system('python3 ./customer_features/customer_main.py'))
        self.customer_button.pack(pady=10)

        # Exit button
        self.customer_button = tk.Button(self,
                                         text='Exit', fg='red',
                                         command=exit)
        self.customer_button.pack(pady=40)
