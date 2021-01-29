import os
import tkinter as tk


class AuthPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.init_login_gui()

    # Function which initialise the GUI
    def init_login_gui(self):
        self.controller.title('Administrator login')

        self.label = tk.Label(self, text="Administrator panel", font=self.controller.title_font)
        self.label.pack(side="top", pady=20)

        # Error message area
        self.status_label = tk.Label(self, text='', font=self.controller.label_font)
        self.status_label.pack(pady=(0, 10))

        # User login
        self.login_label = tk.Label(self,
                                    text="Username:",
                                    font=self.controller.label_font).pack()

        self.login_entry = tk.Entry(self)
        self.login_entry.pack(pady=(0, 20))

        # Password
        self.password_label = tk.Label(self,
                                       text="Password:",
                                       font=self.controller.label_font).pack()

        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(pady=(0, 20))

        # Login button
        self.login_button = tk.Button(self,
                                      text='Login',
                                      command=lambda: self.login_in_process())
        self.login_button.pack(pady=10)

    # login in function
    def login_in_process(self):
        user_name = self.login_entry.get()
        user_password = self.password_entry.get()

        user_base = os.listdir('./users/')

        # Check if User registered
        if user_name in user_base:
            open_file = open('./users/' + user_name, 'r')
            check_password = open_file.read().splitlines()
            # Checks user's password
            if user_password in check_password:
                self.login_status(1)
            else:
                self.login_status(2)
        else:
            self.login_status(3)

    # Login status function
    def login_status(self, status):
        if status == 1:
            self.status_label.config(text="Login success", fg='green')

            self.controller.show_frame(1)
        elif status == 2:
            self.status_label.config(text="Wrong Password", fg='red')
        elif status == 3:
            self.status_label.config(text="User not found", fg='red')
