import sqlite3


# connecting to database
conn = sqlite3.connect('review.db')
# creating a cursor
c = conn.cursor()

# creating table
'''
c.execute("""CREATE TABLE Rating (
                Product TEXT,
                Rating REAL, 
                Comment TEXT
                ) """)
'''
# using this query, I am able to add values into the table
# c.execute("INSERT INTO Rating VALUES('Teddy','3.5','Good toy but destroyed in the wash')")
all_reviews = [
                ('Uno','4.5','Very fun game'),
                ('Uno','5.0','Enjoyed by all. kept us entertained.'),
                ('Uno','5.0','Entertaining and very fun')
                ]
# using this query, I am able to create a list and add it into the database
# c.executemany("INSERT INTO Rating VALUES (?,?,?)", all_reviews)
