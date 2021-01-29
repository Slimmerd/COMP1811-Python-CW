import sqlite3
import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.title('All about Toys')
root.config(bg='#ccffff')

width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width, height))

# different fonts and size available to use
font1 = font.Font(family='arial', size='30', weight='bold')
font2 = font.Font(family='arial', size='24', weight='bold')
font3 = font.Font(family='arial', size='20')
font4 = font.Font(family='arial', size='18', weight='bold')

product_frame = tk.Frame(root, bg='white')
product_display = tk.Frame(root, bg='white')


# product class - allows me to create different product instances
class Product:
    def __init__(self, product_name, price, brand, stock):
        self.product_name = product_name
        self.price = price
        self.brand = brand
        self.stock = stock

    # checks stock level and outputs low stock or no stock
    def stock_level(self):
        if self.stock == '0':
            return "OUT OF STOCK"
        elif self.stock == '20' or self.stock < '20':
            return "LOW STOCK"

        else:
            return "Plenty in stock. Order now!"

    # using str creates an output suited for the end users
    # displays the name of product, price, brand and stock level
    def __str__(self):
        return "Name of Product: {}        price: {}         brand: {}          stock: {}".format(self.product_name,
                                                                                                  self.price,
                                                                                                  self.brand,
                                                                                                  self.stock_level())


# this function give functionality to the items in the listbox
def go(event):
    cs = listbox.curselection()
    product_display.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.75, anchor='n')
    # this button will take the user back to the products page
    back_btn = tk.Button(header, text='back', bg='white', fg='darkgreen', relief='flat', command=show_products)
    back_btn.place(relx=0.1, rely=0.35)

    for list in cs:
        if list == 0:
            listbox.pack_forget()
            product_name = tk.Label(product_display, text='TEDDY BEAR. SOFT & CUDDLY TOY', bg='white', font=font1)
            product_name.place(rely=0.03, relx=0.13)
            brand = tk.Label(product_display, text='Build-a-Bear', bg='white', font=font2)
            brand.place(rely=0.13, relx=0.37)
            Description = tk.Label(product_display,
                                   text='This plush, cuddly bear is great for you to hug and snuggle them \n all you want!',
                                   bg='white', font=font3)
            Description.place(rely=0.23, relx=0.13)
            price = tk.Label(product_display, text='£3.50', bg='white', font=font2)
            price.place(rely=0.14, relx=0.67)
            buy_btn = tk.Button(product_display, text='BUY NOW', bg='pink')
            buy_btn.place(rely=0.43, relx=0.2, relheight=0.2, relwidth=0.2)
            review_btn = tk.Button(product_display, text='REVIEWS', bg='pink', command=ted_rev)
            review_btn.place(rely=0.43, relx=0.45, relheight=0.2, relwidth=0.2)

        if list == 1:
            listbox.pack_forget()
            product_name = tk.Label(product_display, text='GUESS WHO BOARD GAME', bg='white', font=font1)
            product_name.place(rely=0.03, relx=0.13)
            brand = tk.Label(product_display, text='Hasbro', bg='white', font=font2)
            brand.place(rely=0.13, relx=0.37)
            Description = tk.Label(product_display,
                                   text='The game where you guess the other persons\ncharacter with yes/no questions',
                                   bg='white', font=font3)
            Description.place(rely=0.23, relx=0.13)
            price = tk.Label(product_display, text='£4.50', bg='white', font=font2)
            price.place(rely=0.14, relx=0.67)
            buy_btn = tk.Button(product_display, text='BUY NOW', bg='pink')
            buy_btn.place(rely=0.43, relx=0.2, relheight=0.2, relwidth=0.2)
            review_btn = tk.Button(product_display, text='REVIEWS', bg='pink', command=GW_rev)
            review_btn.place(rely=0.43, relx=0.45, relheight=0.2, relwidth=0.2)

        if list == 2:
            listbox.pack_forget()
            product_name = tk.Label(product_display, text='MONOPOLY BOARD GAME', bg='white', font=font1)
            product_name.place(rely=0.03, relx=0.13)
            brand = tk.Label(product_display, text='Hasbro', bg='white', font=font2)
            brand.place(rely=0.13, relx=0.37)
            Description = tk.Label(product_display,
                                   text='Monopoly is the fast-dealing property trading game.\nYou will buy, sell and have a blast with your friends/family.',
                                   bg='white', font=font3)
            Description.place(rely=0.23, relx=0.13)
            price = tk.Label(product_display, text='£12.99', bg='white', font=font2)
            price.place(rely=0.14, relx=0.67)
            buy_btn = tk.Button(product_display, text='BUY NOW', bg='pink')
            buy_btn.place(rely=0.43, relx=0.2, relheight=0.2, relwidth=0.2)
            review_btn = tk.Button(product_display, text='REVIEWS', bg='pink')
            review_btn.place(rely=0.43, relx=0.45, relheight=0.2, relwidth=0.2)

        if list == 3:
            listbox.pack_forget()
            product_name = tk.Label(product_display, text='IRON MAN FIGURE', bg='white', font=font1)
            product_name.place(rely=0.03, relx=0.13)
            brand = tk.Label(product_display, text='Hasbro', bg='white', font=font2)
            brand.place(rely=0.13, relx=0.37)
            Description = tk.Label(product_display,
                                   text='With this cool action figure, kids can create their own\nadventures with Tony Stark',
                                   bg='white', font=font3)
            Description.place(rely=0.23, relx=0.13)
            price = tk.Label(product_display, text='£15.00', bg='white', font=font2)
            price.place(rely=0.14, relx=0.67)
            buy_btn = tk.Button(product_display, text='BUY NOW', bg='pink')
            buy_btn.place(rely=0.43, relx=0.2, relheight=0.2, relwidth=0.2)
            review_btn = tk.Button(product_display, text='REVIEWS', bg='pink')
            review_btn.place(rely=0.43, relx=0.45, relheight=0.2, relwidth=0.2)

        if list == 4:
            listbox.pack_forget()
            product_name = tk.Label(product_display, text='UNO CARD GAME', bg='white', font=font1)
            product_name.place(rely=0.03, relx=0.13)
            brand = tk.Label(product_display, text='Mattel', bg='white', font=font2)
            brand.place(rely=0.13, relx=0.37)
            Description = tk.Label(product_display,
                                   text='A FUN GAME TO PLAY WITH ALL',
                                   bg='white', font=font3)
            Description.place(rely=0.23, relx=0.13)
            price = tk.Label(product_display, text='£1.99', bg='white', font=font2)
            price.place(rely=0.14, relx=0.67)
            buy_btn = tk.Button(product_display, text='BUY NOW', bg='pink')
            buy_btn.place(rely=0.43, relx=0.2, relheight=0.2, relwidth=0.2)
            review_btn = tk.Button(product_display, text='REVIEWS', bg='pink')
            review_btn.place(rely=0.43, relx=0.45, relheight=0.2, relwidth=0.2)

        if list == 5:
            listbox.pack_forget()
            product_name = tk.Label(product_display, text='BATMAN FIGURE', bg='white', font=font1)
            product_name.place(rely=0.03, relx=0.13)
            brand = tk.Label(product_display, text='Hasbro', bg='white', font=font2)
            brand.place(rely=0.13, relx=0.37)
            Description = tk.Label(product_display,
                                   text='With this cool action figure, kids can create their own\nadventures with Batman',
                                   bg='white', font=font3)
            Description.place(rely=0.23, relx=0.13)
            price = tk.Label(product_display, text='£13.99', bg='white', font=font2)
            price.place(rely=0.14, relx=0.67)
            buy_btn = tk.Button(product_display, text='BUY NOW', bg='pink')
            buy_btn.place(rely=0.43, relx=0.2, relheight=0.2, relwidth=0.2)
            review_btn = tk.Button(product_display, text='REVIEWS', bg='pink')
            review_btn.place(rely=0.43, relx=0.45, relheight=0.2, relwidth=0.2)


# displays it on to the product frame
listbox = tk.Listbox(product_frame)

# the different products
Teddy = Product('Teddy Bear', '£3.50', 'Build-a-Bear', '10')
Guesswho = Product('Guess Who', '£4.50', 'Hasbro', '50')
Monopoly = Product('Monopoly', '£12.99', 'Hasbro', '20')
Ironman = Product('Iron Man', '£15', 'Marvel', '0')
Uno = Product('Uno cards', '£1.99', 'Mattel', '87')
Batman = Product('Batman', '£13.99', 'Marvel', '3')

# puts all the products into the listbox
main_list = [Batman, Uno, Ironman, Monopoly, Guesswho, Teddy]
for item in main_list:
    listbox.insert(0, item)

listbox.config(font=35)

# Binding double click with left mouse
# button with go function
listbox.bind('<Double-1>', go)
listbox.pack(fill='both', expand=True)

review_pg = tk.Frame(root, bg='white')
add_review = tk.Frame(root, bg='lightblue')


# creating submit function - will store user's review into database
# def submit():
def submit_review():
    # connecting to database
    conn = sqlite3.connect('database/review.db')
    # creating a cursor
    c = conn.cursor()

    c.execute("INSERT INTO Rating VALUES(:prod_name, :rating, :comment)",
              {
                  'prod_name': prod_name.get(),
                  'rating': rating.get(),
                  'comment': comment.get()
              })
    print('functioning')
    # commit our command
    conn.commit()
    # close our connection
    conn.close()


prod_name = tk.Entry(add_review)
rating = tk.Entry(add_review)
comment = tk.Entry(add_review)
submit = tk.Button(add_review, text='SUBMIT', fg='black', bg='white', command=submit_review)


# this will take the user to a separate 'page' to write their own reviews
def add_more_reviews():
    add_review.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.75, anchor='n')
    prod_lbl = tk.Label(add_review, text='PRODUCT NAME', fg='black', bg='lightblue')
    prod_lbl.place(relx=0.05, rely=0.11)
    prod_name.place(relx=0.17, rely=0.1, relheight=0.05, relwidth=0.6)
    rating_lbl = tk.Label(add_review, text='RATING', fg='black', bg='lightblue')
    rating_lbl.place(relx=0.05, rely=0.21)
    rating.place(relx=0.17, rely=0.2, relheight=0.05, relwidth=0.6)
    comment_lbl = tk.Label(add_review, text='COMMENT', fg='black', bg='lightblue')
    comment_lbl.place(relx=0.05, rely=0.46)
    comment.place(relx=0.17, rely=0.3, relheight=0.4, relwidth=0.6)
    submit.place(relx=0.84, rely=0.45, relheight=0.2, relwidth=0.1)


# allows user to read reviews on teddy bear
# this connects to the database I made and displays the data according to the query
def ted_rev():
    # connecting to database
    conn = sqlite3.connect('database/review.db')
    # creating a cursor
    c = conn.cursor()

    review_pg.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.75, anchor='n')
    add_btn = tk.Button(review_pg, text='ADD REVIEW', bg='lightpink', command=add_more_reviews)
    add_btn.place(relx=0.25, rely=0.02, relheight=0.1, relwidth=0.4)

    c.execute("SELECT * FROM Rating WHERE Product = 'Teddy'")
    record = c.fetchall()
    print(record)
    # loop through results
    print_record = ''
    for rec in record:
        print_record += str(rec[0]) + " " + str(rec[1]) + " " + str(rec[2]) + "\n"

    review_lbl = tk.Label(review_pg, text=print_record, bg='white', font=font4)
    review_lbl.place(relx=0.01, rely=0.13, relheight=0.3, relwidth=0.8)

    print('completed')
    # commit our command
    conn.commit()
    # close our connection
    conn.close()


# allows user to read reviews on guess who product
def GW_rev():
    # connecting to database
    conn = sqlite3.connect('database/review.db')
    # creating a cursor
    c = conn.cursor()

    review_pg.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.75, anchor='n')
    add_btn = tk.Button(review_pg, text='ADD REVIEW', bg='lightpink', command=add_more_reviews)
    add_btn.place(relx=0.25, rely=0.02, relheight=0.1, relwidth=0.4)

    c.execute("SELECT * FROM Rating WHERE Product = 'Guess who'")
    record = c.fetchall()

    # loop through results
    print_record = ''
    for rec in record:
        print_record += str(rec[0]) + " " + str(rec[1]) + " " + str(rec[2]) + "\n"

    review_lbl = tk.Label(review_pg, text=print_record, bg='white', font=font4)
    review_lbl.place(relx=0.01, rely=0.13, relheight=0.3, relwidth=0.8)

    print('completed')

    # commit our command
    conn.commit()
    # close our connection
    conn.close()


# this function will take the user to the main page
def main_page():
    product_frame.place_forget()
    cat_frame.place_forget()
    frame_3.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.55, anchor='n')


# this function takes the user to the products page.
# this is a page that shows the different products available
def show_products():
    frame_3.place_forget()
    product_display.place_forget()
    listbox.pack(fill='both', expand=True)
    product_frame.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.75, anchor='n')
    btn_2 = tk.Button(header, text='back', bg='white', fg='darkgreen', relief='flat', command=main_page)
    btn_2.place(relx=0.1, rely=0.35)


display_frame = tk.Frame(root, bg='white')


# gives the search box functionality
def search(search_box):
    print('this is the entry: ', search_box)
    if search_box == 'Action figures' or 'action figures':
        action_figures()

    elif search_box == 'Board games' or 'board games' or 'Monopoly' or 'Guess who':
        board_games()

    elif search_box == 'Card games' or 'card games' or 'uno' or 'Uno':
        card_games()


# this will only display the action figures when searched or the category is chosen
listbox1 = tk.Listbox(display_frame)


def action_figures():
    cat_frame.place_forget()
    frame_3.place_forget()
    listbox2.pack_forget()
    listbox3.pack_forget()
    display_frame.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.75, anchor='n')
    btn_2 = tk.Button(header, text='back', bg='white', fg='darkgreen', relief='flat', command=show_categories)
    btn_2.place(relx=0.1, rely=0.35)

    listbox1.insert(0, Ironman)
    listbox1.insert(1, Batman)

    listbox1.config(font=35)

    listbox1.pack(fill='both', expand=True)


listbox2 = tk.Listbox(display_frame)


def board_games():
    cat_frame.place_forget()
    frame_3.place_forget()
    listbox1.pack_forget()
    listbox3.pack_forget()
    display_frame.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.75, anchor='n')
    btn_2 = tk.Button(header, text='back', bg='white', fg='darkgreen', relief='flat', command=show_categories)
    btn_2.place(relx=0.1, rely=0.35)

    listbox2.insert(0, Guesswho)
    listbox2.insert(1, Monopoly)

    listbox2.config(font=35)

    listbox2.pack(fill='both', expand=True)


listbox3 = tk.Listbox(display_frame)


def card_games():
    cat_frame.place_forget()
    frame_3.place_forget()
    listbox1.pack_forget()
    listbox2.pack_forget()
    display_frame.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.75, anchor='n')
    btn_2 = tk.Button(header, text='back', bg='white', fg='darkgreen', relief='flat', command=show_categories)
    btn_2.place(relx=0.1, rely=0.35)

    listbox3.insert(0, Uno)

    listbox3.config(font=35)
    listbox3.pack(fill='both', expand=True)


# this is my category frame. when the category button is clicked, all the different categories will be displayed
cat_frame = tk.Frame(root, bg='white')


def show_categories():
    frame_3.place_forget()
    cat_frame.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.75, anchor='n')
    # category_1 - action figures
    action_btn = tk.Button(cat_frame, text='Action Figures', bg='red', fg='black', font=90, command=action_figures)
    action_btn.place(relx=0.02, rely=0.02, relheight=0.3, relwidth=0.2)
    # category_2 - board games
    board_btn = tk.Button(cat_frame, text='Board Games', bg='lightblue', fg='black', font=90, command=board_games)
    board_btn.place(relx=0.02, rely=0.36, relheight=0.3, relwidth=0.2)
    # category_3 - card games
    card_btn = tk.Button(cat_frame, text='Card Games', bg='yellow', fg='black', font=90, command=card_games)
    card_btn.place(relx=0.24, rely=0.02, relheight=0.3, relwidth=0.2)

    btn_2 = tk.Button(header, text='back', bg='white', fg='darkgreen', relief='flat', command=main_page)
    btn_2.place(relx=0.1, rely=0.35)


# This is the header where the company name and 'exit' button is displayed
header = tk.Frame(root, bg='white')
header.place(relx=0.5, rely=0.02, relwidth=0.95, relheight=0.1, anchor='n')

lbl_font = font.Font(family='arial', size='32', weight='bold')
lbl_1 = tk.Label(header, text='All about Toys', fg='lightpink', bg='white', font=lbl_font)
lbl_1.place(relx=0.5, rely=0.45, anchor='center')
btn_1 = tk.Button(header, text='exit', bg='white', fg='red', relief='flat', command=quit)
btn_1.place(relx=0.9, rely=0.35)

# This frame is where the search box is displayed
search_frame = tk.Frame(root, bg='#ccffcc')
search_frame.place(relx=0.5, rely=0.15, relwidth=0.95, relheight=0.1, anchor='n')

# search box
search_box = tk.Entry(search_frame)
search_box.place(relx=0.01, rely=0.25, relwidth=0.5, relheight=0.5)
search_btn = tk.Button(search_frame, text='SEARCH', bg='#ccfff2', fg='black', command=lambda: search(search_box.get()))
search_btn.place(relx=0.7, rely=0.25, relwidth=0.2, relheight=0.5)

# This frame is where the main 2 buttons are displayed
# This frame will be displayed as the 'main menu'
frame_3 = tk.Frame(root)
frame_3.place(relx=0.5, rely=0.3, relwidth=0.95, relheight=0.55, anchor='n')
# these 2 buttons will lead the user to different 'pages'; catalogue and categories
product_btn = tk.Button(frame_3, text='TOY CATALOGUE', bg='#ffccd9', fg='black', font=80, command=show_products)
product_btn.pack(side='left', fill='both', expand=True)
category_btn = tk.Button(frame_3, text='CATEGORIES', bg='#fff2cc', fg='black', font=80, command=show_categories)
category_btn.pack(side='right', fill='both', expand=True)

root.mainloop()
