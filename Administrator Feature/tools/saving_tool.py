import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime

from api.database_management import DatabaseAPI


class SaveFile:
    def __init__(self, window):
        self.window = window

        # Gets current date
        self.current_date = str(datetime.today().strftime('%Y-%m-%d'))

        # Gets chosen filepath by user
        self.chosen_filepath = tk.filedialog.askdirectory(parent=self.window,
                                                          initialdir='C:\\',
                                                          title="Please select a directory:")

    def save_stock_taking_file(self):

        # Sets the file name
        self.file_name = f'Stock taking from {self.current_date}'
        self.__save_file(1)  # Saves file

    def save_low_stock_file(self):

        # Sets the file name
        self.file_name = f'Low stock items on {self.current_date}'
        self.__save_file(2)  # Saves file

    def __save_file(self, saving_type):

        # If directory were chosen it will save the file
        if len(self.chosen_filepath) > 0:

            if saving_type == 1:
                DatabaseAPI().save_database_file('Products', self.file_name, self.chosen_filepath)
            elif saving_type == 2:
                DatabaseAPI().save_database_file('Products', self.file_name, self.chosen_filepath, 2)

            tk.messagebox.showinfo('Saved', f'File "{self.file_name}" is saved in {self.chosen_filepath} directory')
        else:
            tk.messagebox.showerror('Error', 'You have to choose directory')
            raise ValueError('You have to choose directory')
