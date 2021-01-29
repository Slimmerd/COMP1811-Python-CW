import tkinter as tk
from tkinter import messagebox

from api.database_management import DatabaseAPI
from tools.window_size import center_window_on_screen


class AddCategoryWindow(tk.Frame):

    def __init__(self, parent, controller, list_name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.list_name = list_name

        self.init_add_category_gui()

    # Function which initialise the GUI
    def init_add_category_gui(self):
        self.win = tk.Toplevel()
        self.win.title("Add Category")
        center_window_on_screen(350, 200, self.winfo_screenwidth(), self.winfo_screenheight(), self.win)

        # Title
        self.label = tk.Label(self.win, text='Create category', font=self.controller.title_font).pack(pady=20)

        # Product name
        self.category_name_label = tk.Label(self.win, text="Category name:")
        self.category_name_label.pack()
        self.category_name_entry = tk.Entry(self.win, name='category_name_entry')
        self.category_name_entry.pack(pady=(0, 0))

        # Exit button
        self.exit_button = tk.Button(self.win, text="Exit", command=self.win.destroy)
        self.exit_button.pack(side='right', padx=(0, 140))

        # Add button
        self.add_button = tk.Button(self.win, text="Add",name='add_button',
                                    command=lambda: self.add_category_button(self.category_name_entry, self.win,
                                                                             self.list_name))
        self.add_button.pack(side='left', padx=(140, 0))

    def add_category_button(self, user_entry, window, list_name):
        category_name = user_entry.get()

        try:
            # Check if category name is empty and string
            if category_name == '':
                raise ValueError(1, 'Empty Fields')

            # Checks if entry is already exist in database
            if DatabaseAPI().repeat_checker("CategoryName", "Categories", category_name) == 1:
                messagebox.showerror('Error', f'Category {category_name} already exist')

            # Creates new category
            else:
                DatabaseAPI().create_category(category_name)
                window.destroy()
                self.__category_success(category_name)
                DatabaseAPI().update_list("CategoryName", "Categories", list_name)
                list_name.select_set(0)  # First item selected by default

        except ValueError:
            tk.messagebox.showerror('Error', 'You can\'t left empty fields')

    @staticmethod
    def __category_success(category_name):
        messagebox.showinfo('Success', f'Category {category_name} created')
