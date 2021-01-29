import tkinter as tk

from api.database_management import DatabaseAPI
from components.toy_categories.sub_components.class_add_category import AddCategoryWindow
from components.toy_categories.sub_components.class_delete_category import DeleteCategoryWindow
from components.toy_categories.sub_components.class_edit_category import EditCategoryWindow


class CategoryListPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.init_category_list_gui()

    # Function which initialise the GUI
    def init_category_list_gui(self):
        self.controller.title('Categories list')

        #   Title
        self.label = tk.Label(self, text='Categories list', font=self.controller.title_font).pack(pady=20)

        #   Categories list
        self.category_list = tk.Listbox(self, height=10, width=50, selectmode='SINGLE', name='category_list')

        # Items
        DatabaseAPI().get_list("CategoryName", "Categories", 0, self.category_list, 1)

        self.category_list.select_set(0)  # First item selected by default
        self.category_list.pack(pady=(0, 20))

        #   Back button
        back_button = tk.Button(self, text='Back', command=lambda: self.back_button_function())
        back_button.pack(pady=10, padx=10, side='left')

        #   Delete button
        delete_button = tk.Button(self, text='Delete', command=lambda: self.delete_category_button())
        delete_button.pack(pady=10, padx=10, side='right')

        #   Edit button
        edit_button = tk.Button(self, text='Edit', command=lambda: self.edit_category_button())
        edit_button.pack(pady=10, padx=10, side='right')

        #   Add button
        add_button = tk.Button(self, text='Add', command=lambda: self.add_category_button())
        add_button.pack(pady=10, padx=10, side='right')

    # Create category button function
    def add_category_button(self):
        self.add_window = AddCategoryWindow(self, self.controller, self.category_list)

    # Edit category function
    def edit_category_button(self):
        self.edit_window = EditCategoryWindow(self, self.controller, self.category_list)

    # Delete category button function
    def delete_category_button(self):
        self.delete_window = DeleteCategoryWindow(self, self.controller, self.category_list)

    # Back button function
    def back_button_function(self):
        self.controller.show_frame(1)
