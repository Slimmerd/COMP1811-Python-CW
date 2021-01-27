import tkinter as tk
from tkinter import messagebox

from api.database_management import DatabaseAPI
from tools.window_size import center_window_on_screen


class EditCategoryWindow(tk.Frame):

    def __init__(self, parent, controller, list_name):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.list_name = list_name

        self.init_edit_category_gui()

    # Function which initialise the GUI
    def init_edit_category_gui(self):
        self.category_list_value = self.list_name.get(self.list_name.curselection())
        self.win = tk.Toplevel()
        self.win.title("Edit Category")
        center_window_on_screen(250, 250, self.winfo_screenwidth(), self.winfo_screenheight(), self.win)

        #   Title
        self.label = tk.Label(self.win, text='Edit category', font=self.controller.title_font).pack(pady=20)

        # Category code
        self.category_code_label = tk.Label(self.win,
                                            text=f"Category code: {self.__get_category_id(self.category_list_value)}")
        self.category_code_label.pack()

        # Category name
        self.category_name_label = tk.Label(self.win, font=self.controller.label_font, text="Category name:")
        self.category_name_label.pack(pady=(20, 5))

        self.category_name_entry = tk.Entry(self.win, name='category_name_entry')

        # Make default entry
        self.category_name_entry.insert(0, self.category_list_value)

        self.category_name_entry.pack()

        # Cancel button
        self.cancel_button = tk.Button(self.win, text="Cancel", command=self.win.destroy)
        self.cancel_button.pack(side='right', padx=(0, 60))

        # Save button
        self.save_button = tk.Button(self.win, text="Save", name='save_button',
                                     command=lambda: self.save_edited_category_button(self.category_list_value,
                                                                                      self.category_name_entry,
                                                                                      self.win,
                                                                                      self.list_name))
        self.save_button.pack(side='left', padx=(60, 0))

    # Gets category id value
    @staticmethod
    def __get_category_id(chosen_value):
        result = DatabaseAPI().get_item_id('Categories', 'CategoryID', 'CategoryName', chosen_value)

        return result

    # Saves user entries and checks if the user wrote the name that already exist
    def save_edited_category_button(self, old_value, user_entry, window, list_name):
        new_value = user_entry.get()

        try:
            if new_value == '':
                raise ValueError('Empty Fields')
            # Checks if new name is exist in database
            if DatabaseAPI().repeat_checker("CategoryName", "Categories", new_value) == 1:
                messagebox.showerror('Error', f'Category {new_value} already exist')
                # Edits category
            else:
                DatabaseAPI().edit_item('Categories', 'CategoryName', old_value, new_value)
                window.destroy()
                self.__edit_category_success(new_value)
                DatabaseAPI().update_list("CategoryName", "Categories", list_name)
                list_name.select_set(0)  # First item selected by default
        except ValueError:
            tk.messagebox.showerror('Error', 'You can\'t left empty fields')

    # Message box about successful changing of category
    @staticmethod
    def __edit_category_success(category_name):
        messagebox.showinfo('Success', f'Category {category_name} was successfully edited')
