import unittest
from App import App
from api.database_management import DatabaseAPI
from components.stock_management.sub_components.class_show_info_window import ShowInfoWindow
from components.toy_categories.sub_components.class_add_category import AddCategoryWindow
from components.toy_categories.sub_components.class_delete_category import DeleteCategoryWindow
from components.toy_categories.sub_components.class_edit_category import EditCategoryWindow
from components.toy_products.sub_components.class_add_product import AddProductWindow
from components.toy_products.sub_components.class_delete_product import DeleteProductWindow
from components.toy_products.sub_components.class_edit_product import EditProductWindow
from tools.saving_tool import SaveFile


class ProductFrameTests(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.MainApp = App()

    # Open Product List Test
    def test_open_product_list_frame(self):
        self.Frame = self.MainApp.show_frame(2)

        self.assertEqual('.!frame.!productlistpage', str(self.MainApp._frame), 'Opened frame should be Product List')

    # Create Product
    def test_create_product(self):
        self.Frame = self.MainApp.show_frame(2)
        # Initialise ProductAdd window with passing required props (attribute) for the class
        self.ProductAdd = AddProductWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                           self.MainApp._frame.children['product_list'])

        # Input values
        input_values = [1, 'Roller Coaster', 64, 120, 'Mechanical']
        _database = ['product_name_entry', 'product_price_entry', 'product_stock_entry']

        # Puts values in Tkinter entries and then uploads it to database
        for row, value in zip(_database, input_values[1:4]):
            self.ProductAdd.win.children[row].insert(0, value)

        self.ProductAdd.selected.set(input_values[4])
        self.ProductAdd.win.children['add_button'].invoke()

        # Gets data from database
        database_check = DatabaseAPI().tester_get_item_id('Products', 'ProductName', str(input_values[1]))

        # Checks is there a row and have it same attributes as we wrote or not
        for actual_data, expected_data in zip(database_check[1:], input_values[:4]):
            self.assertEqual(expected_data, actual_data, 'Data appeared in database correctly')

    # Edit Product
    def test_edit_product(self):
        self.Frame = self.MainApp.show_frame(2)

        # Finds old name index in the list (used for set selection)
        old_value_name = 'Roller Coaster'
        product_list = self.MainApp._frame.children['product_list'].get(0, 'end')
        for value in product_list:
            if value == old_value_name:
                selection = product_list.index(value)

                # Clear selection
                self.MainApp._frame.children['product_list'].selection_clear(0, 'end')
                # Set selection
                self.MainApp._frame.children['product_list'].selection_set(selection)

                self.start_function = True

        if self.start_function:
            # Initialise ProductEdit window with passing required props (attribute) for the class
            self.ProductEdit = EditProductWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                                 self.MainApp._frame.children['product_list'])

            # Input values
            edited_input_values = [1, 'German Roller Coaster', 49, 19, 'Mechanical']

            # Clears input rows
            entries = ['product_name_entry', 'product_price_entry', 'product_stock_entry']
            for row in entries:
                self.ProductEdit.win.children[row].delete(0, 'end')

            for row, new_values in zip(entries, edited_input_values[1:4]):
                self.ProductEdit.win.children[row].insert(0, new_values)

            self.ProductEdit.win.children['save_button'].invoke()

            # Gets data from database
            database_check = DatabaseAPI().tester_get_item_id('Products', 'ProductName', edited_input_values[1])

            # Checks is there a row and have it same attributes as we wrote or not
            for actual_data, expected_data in zip(database_check[1:], edited_input_values[:4]):
                self.assertEqual(expected_data, actual_data, 'Data changed in database correctly')

        else:
            raise ValueError('There is no old_value_name in the list')

    # Delete Product
    def test_delete_product(self):
        self.Frame = self.MainApp.show_frame(2)

        # Finds old name index in the list (used for set selection)
        old_value_name = 'German Roller Coaster'
        product_list = self.MainApp._frame.children['product_list'].get(0, 'end')
        for value in product_list:
            if value == old_value_name:
                selection = product_list.index(value)

                # Clear selection
                self.MainApp._frame.children['product_list'].selection_clear(0, 'end')
                # Set selection
                self.MainApp._frame.children['product_list'].selection_set(selection)

                self.start_function = True

        if self.start_function:
            # Initialise ProductEdit window with passing required props (attribute) for the class
            self.ProductDelete = DeleteProductWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                                     self.MainApp._frame.children['product_list'])

            # Gets data from database
            try:
                database_check = DatabaseAPI().tester_get_item_id('Products', 'ProductName', old_value_name)

            except IndexError:
                pass

            else:
                raise ValueError('Error')


        else:
            raise ValueError('There is no old_value_name in the list')

    # Edit Product with empty fields
    def test_empty_edit_product(self):
        self.test_create_product()
        self.Frame = self.MainApp.show_frame(2)

        # Finds old name index in the list (used for set selection)
        old_value_name = 'Roller Coaster'

        product_list = self.MainApp._frame.children['product_list'].get(0, 'end')
        for value in product_list:
            if value == old_value_name:
                selection = product_list.index(value)

                # Clear selection
                self.MainApp._frame.children['product_list'].selection_clear(0, 'end')
                # Set selection
                self.MainApp._frame.children['product_list'].selection_set(selection)

                self.start_function = True

        if self.start_function:
            # Initialise ProductEdit window with passing required props (attribute) for the class
            self.ProductEdit = EditProductWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                                 self.MainApp._frame.children['product_list'])

            # Input values
            edited_input_values = [1, '', '', '', '']

            # Clears input rows
            entries = ['product_name_entry', 'product_price_entry', 'product_stock_entry']
            for row in entries:
                self.ProductEdit.win.children[row].delete(0, 'end')

            self.ProductEdit.win.children['save_button'].invoke()

            # Gets data from database
            try:
                DatabaseAPI().tester_get_item_id('Products', 'ProductName', edited_input_values[1])
            except IndexError:
                pass
            else:
                raise ValueError('Empty fields can be passed into database')

        else:
            raise ValueError('There is no old_value_name in the list')

    # Create Product with empty fields
    def test_empty_create_product(self):
        self.Frame = self.MainApp.show_frame(2)
        # Initialise ProductAdd window with passing required props (attribute) for the class
        self.ProductAdd = AddProductWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                           self.MainApp._frame.children['product_list'])

        # Input values
        input_values = [1, '', '', '', 'Mechanical']
        _database = ['product_name_entry', 'product_price_entry', 'product_stock_entry']

        # Puts values in Tkinter entries and then uploads it to database
        for row, value in zip(_database, input_values[1:4]):
            self.ProductAdd.win.children[row].insert(0, value)

        self.ProductAdd.selected.set(input_values[4])
        self.ProductAdd.win.children['add_button'].invoke()

        # Gets data from database
        self.assertRaises(IndexError, DatabaseAPI().tester_get_item_id, 'Products', 'ProductName', input_values[1])

    # Create Product with text in fields for digits
    def test_digits_create_product(self):
        self.test_create_product()
        self.test_edit_product()
        self.test_delete_product()

        self.Frame = self.MainApp.show_frame(2)
        # Initialise ProductAdd window with passing required props (attribute) for the class
        self.ProductAdd = AddProductWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                           self.MainApp._frame.children['product_list'])

        # Input values
        input_values = [1, 'Roller Coaster', 'Home', 'Hello', 'Mechanical']
        _database = ['product_name_entry', 'product_price_entry', 'product_stock_entry']

        # Puts values in Tkinter entries and then uploads it to database
        for row, value in zip(_database, input_values[1:4]):
            self.ProductAdd.win.children[row].insert(0, value)

        self.ProductAdd.selected.set(input_values[4])
        self.ProductAdd.win.children['add_button'].invoke()

        # Check data from database
        self.assertRaises(IndexError, DatabaseAPI().tester_get_item_id, 'Products', 'ProductName', input_values[1])

    # Create Edit with text in fields for digits
    def test_digits_edit_product(self):
        self.test_create_product()
        self.Frame = self.MainApp.show_frame(2)

        # Finds old name index in the list (used for set selection)
        old_value_name = 'Roller Coaster'
        product_list = self.MainApp._frame.children['product_list'].get(0, 'end')
        for value in product_list:
            if value == old_value_name:
                selection = product_list.index(value)

                # Clear selection
                self.MainApp._frame.children['product_list'].selection_clear(0, 'end')
                # Set selection
                self.MainApp._frame.children['product_list'].selection_set(selection)

                self.start_function = True

        if self.start_function:
            # Initialise ProductEdit window with passing required props (attribute) for the class
            self.ProductEdit = EditProductWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                                 self.MainApp._frame.children['product_list'])

            # Input values
            edited_input_values = [1, 'German Roller Coaster', 'hello', 'faf', 'Mechanical']

            # Clears input rows
            entries = ['product_name_entry', 'product_price_entry', 'product_stock_entry']
            for row in entries:
                self.ProductEdit.win.children[row].delete(0, 'end')

            for row, new_values in zip(entries, edited_input_values[1:4]):
                self.ProductEdit.win.children[row].insert(0, new_values)

            self.ProductEdit.win.children['save_button'].invoke()

            # Gets data from database
            self.assertRaises(IndexError, DatabaseAPI().tester_get_item_id, 'Products', 'ProductName',
                              edited_input_values[1])

        else:
            raise ValueError('There is no old_value_name in the list')


class CategoryFrameTests(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.MainApp = App()

    # Open Category List Test
    def test_open_category_list_frame(self):
        self.Frame = self.MainApp.show_frame(3)

        self.assertEqual('.!frame.!categorylistpage', str(self.MainApp._frame), 'Opened frame should be Category List')

    # Create Category
    def test_create_category(self):
        self.Frame = self.MainApp.show_frame(3)
        # Initialise ProductAdd window with passing required props (attribute) for the class
        self.CategoryAdd = AddCategoryWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                             self.MainApp._frame.children['category_list'])

        # Puts values in Tkinter entries and then uploads it to database
        category_name = 'Dolls'

        self.CategoryAdd.win.children['category_name_entry'].insert(0, category_name)

        self.CategoryAdd.win.children['add_button'].invoke()

        # Gets data from database
        database_check = DatabaseAPI().tester_get_item_id('Categories', 'CategoryName', category_name)

        # Checks is there a row and have it same attributes as we wrote or not
        self.assertEqual(category_name, database_check[1], 'Data appeared in database correctly')

    # Edit Category
    def test_edit_category(self):
        self.Frame = self.MainApp.show_frame(3)

        # Finds old name index in the list (used for set selection)
        old_value_name = 'Dolls'
        product_list = self.MainApp._frame.children['category_list'].get(0, 'end')
        for value in product_list:
            if value == old_value_name:
                selection = product_list.index(value)

                # Clear selection
                self.MainApp._frame.children['category_list'].selection_clear(0, 'end')
                # Set selection
                self.MainApp._frame.children['category_list'].selection_set(selection)

                self.start_function = True

        if self.start_function:
            # Initialise CategoryEdit window with passing required props (attribute) for the class
            self.CategoryEdit = EditCategoryWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                                   self.MainApp._frame.children['category_list'])

            # Input values
            edited_input_values = 'Educational'

            # Clears input rows
            self.CategoryEdit.win.children['category_name_entry'].delete(0, 'end')
            self.CategoryEdit.win.children['category_name_entry'].insert(0, edited_input_values)

            self.CategoryEdit.win.children['save_button'].invoke()

            # Gets data from database
            database_check = DatabaseAPI().tester_get_item_id('Categories', 'CategoryName', edited_input_values)

            # Checks is there a row and have it same attributes as we wrote or not
            self.assertEqual(edited_input_values, database_check[1], 'Data changed in database correctly')

        else:
            raise ValueError('There is no old_value_name in the list')

    # Delete Category
    def test_delete_category(self):
        self.Frame = self.MainApp.show_frame(3)

        # Finds old name index in the list (used for set selection)
        old_value_name = 'Educational'
        product_list = self.MainApp._frame.children['category_list'].get(0, 'end')
        for value in product_list:
            if value == old_value_name:
                selection = product_list.index(value)

                # Clear selection
                self.MainApp._frame.children['category_list'].selection_clear(0, 'end')
                # Set selection
                self.MainApp._frame.children['category_list'].selection_set(selection)

                self.start_function = True

        if self.start_function:
            # Initialise ProductEdit window with passing required props (attribute) for the class
            self.ProductDelete = DeleteCategoryWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                                      self.MainApp._frame.children['category_list'])

            # Gets data from database
            try:
                database_check = DatabaseAPI().tester_get_item_id('Categories', 'CategoryName', old_value_name)

            except IndexError:
                pass

            else:
                raise ValueError('Error')

        else:
            raise ValueError('There is no old_value_name in the list')

    # Edit Category with empty values
    def test_empty_edit_category(self):
        self.test_create_category()
        self.Frame = self.MainApp.show_frame(3)

        # Finds old name index in the list (used for set selection)
        old_value_name = 'Dolls'

        product_list = self.MainApp._frame.children['category_list'].get(0, 'end')
        for value in product_list:
            if value == old_value_name:
                selection = product_list.index(value)

                # Clear selection
                self.MainApp._frame.children['category_list'].selection_clear(0, 'end')
                # Set selection
                self.MainApp._frame.children['category_list'].selection_set(selection)

                self.start_function = True

        if self.start_function:
            # Initialise ProductEdit window with passing required props (attribute) for the class
            self.CategoryEdit = EditCategoryWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                                   self.MainApp._frame.children['category_list'])

            # Clears input rows
            self.CategoryEdit.win.children['category_name_entry'].delete(0, 'end')

            self.CategoryEdit.win.children['save_button'].invoke()

            # Gets data from database
            try:
                DatabaseAPI().tester_get_item_id('Categories', 'CategoryName', '')
            except IndexError:
                pass
            else:
                raise ValueError('Empty fields can be passed into database')

        else:
            raise ValueError('There is no old_value_name in the list')

    # Create Category with empty values
    def test_empty_create_category(self):
        self.Frame = self.MainApp.show_frame(3)
        # Initialise ProductAdd window with passing required props (attribute) for the class
        self.CategoryAdd = AddCategoryWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                             self.MainApp._frame.children['category_list'])

        # Input values
        input_values = ''

        # Puts values in Tkinter entries and then uploads it to database
        self.CategoryAdd.win.children['category_name_entry'].insert(0, input_values)

        self.CategoryAdd.win.children['add_button'].invoke()

        # Gets data from database
        self.assertRaises(IndexError, DatabaseAPI().tester_get_item_id, 'Products', 'ProductName', input_values)


class StockTakingFrameTests(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.MainApp = App()

    # Open Stock Taking Frame
    def test_open_stock_taking_frame(self):
        self.Frame = self.MainApp.show_frame(4)

        self.assertEqual('.!frame.!stocktakingpage', str(self.MainApp._frame),
                         'Opened frame should be Stock Taking List')

    # Save Stock Taking
    def test_save_stock_taking_frame(self):
        self.Frame = self.MainApp.show_frame(4)

        try:
            SaveFile(self.Frame).save_stock_taking_file()
        except ValueError:
            self.fail()


class LowStockFrameTests(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.MainApp = App()

    # Open Stock Taking Frame
    def test_open_low_stock_frame(self):
        self.Frame = self.MainApp.show_frame(5)

        self.assertEqual('.!frame.!lowstockpage', str(self.MainApp._frame),
                         'Opened frame should be Stock Taking List')

    # Save Stock Taking
    def test_low_stock_frame(self):
        self.Frame = self.MainApp.show_frame(5)

        try:
            SaveFile(self.Frame).save_stock_taking_file()
        except ValueError:
            self.fail()

    # Show low stock info
    def test_show_low_stock_info(self):
        self.Frame = self.MainApp.show_frame(5)

        # Finds old name index in the list (used for set selection)
        old_value_name = 'Big Dragon'
        product_list = self.MainApp._frame.children['low_stock_product_list'].get(0, 'end')
        for value in product_list:
            if value == old_value_name:
                selection = product_list.index(value)

                # Clear selection
                self.MainApp._frame.children['low_stock_product_list'].selection_clear(0, 'end')
                # Set selection
                self.MainApp._frame.children['low_stock_product_list'].selection_set(selection)

                self.start_function = True

        if self.start_function:
            self.show_low_stock_info = ShowInfoWindow(self.MainApp._frame, self.MainApp._frame.controller,
                                                      self.MainApp._frame.children['low_stock_product_list'])

            expected_result = ['Big Dragon', 2, 23, 3]

            attributes_list = ['category_code_entry', 'product_name_entry', 'product_category_entry',
                               'product_price_entry', 'product_stock_entry']
            actual_attributes = []

            for attribute in attributes_list:
                actual_attributes.append(self.show_low_stock_info.win.children[attribute].cget("text"))

            self.assertEqual(expected_result, actual_attributes[1:], 'Results should be equal')

        else:
            raise ValueError('There is no old_value_name in the list')


if __name__ == '__main__':
    unittest.main()
