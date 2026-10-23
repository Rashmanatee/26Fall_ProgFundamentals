import sqlite3
# Open a connection and create a cursor 
conn = sqlite3.connect('library.db')                                                                                                                    
cur = conn.cursor()                                                                                                                                     
cur.execute("DROP TABLE IF EXISTS books")

cur.execute("""CREATE TABLE books
(   id INT NOT NULL,
TITLE VARCHAR(60) NOT NULL,
AUTHOR VARCHAR(40) NOT NULL,
YEAR INT NOT NULL,
GENRE VARCHAR(20),
COPIES INT,
RATING INT,
PRIMARY KEY (id));
""")

# adding the books

# Add the books
cur.execute("""
INSERT INTO books 
VALUES (1, 'Pride and Prejudice', 'Jane Austen', 1813, 'Fiction', 2, 3)
""")

# The rest: each ? is filled in from a tuple. None is stored as NULL (no rating).
books = [
    (2, "The Origin of Species", "Charles Darwin", 1859, "Science", 2, 4),
    (3, "A Brief History of Time", "Stephen Hawking", 1988, "Science", 3, 4),
    (4, "Gone Girl", "Gillian Flynn", 2012, "Mystery", 5, 4),
    (5, "The Guns of August", "Barbara Tuchman", 1962, "History", 2, 5),
    (6, "Sapiens", "Yuval Noah Harari",  2011, "History", 6, None),
    (7, "The Martian", "Andy Weir", 2011, "Fiction", 3, 4),
    (8, "Cosmos", "Carl Sagan", 1980, "Science", 1, None),
    (9, "The Hound of the Baskervilles", "Arthur Conan Doyle", 1902, "Mystery", 2, 3),
]
cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)", books)


print("Books published after 1990 (title and author):")
for row in cur.execute("SELECT title, author FROM books WHERE year > 1990"):
    print(row)

print("Fiction books with more than 2 copies:")
for row in cur.execute("SELECT title FROM books WHERE genre = 'Fiction' AND copies > 2"):
    print(row)

print("books published before 1900, or rated 5:")
for row in cur.execute("SELECT title FROM books WHERE year < 1900 OR rating = 5"):
    print(row)

print("books that are not in the Mystery genre:")
for row in cur.execute("SELECT title FROM books WHERE NOT genre = 'Mystery'"):
    print(row)

print("books in the Science or History genre:")
for row in cur.execute("SELECT title FROM books WHERE genre IN ('Science', 'History')"):
    print(row)


letter = input("\nType a letter: ").strip()
print("LIKE: authors whose names start with", letter + ":")
for row in cur.execute("SELECT author FROM books WHERE author LIKE ?", (letter + "%",)):
    print(row)

print("books with no rating:")
for row in cur.execute("SELECT title FROM books WHERE rating IS NULL"):
    print(row)

conn.commit()
conn.close()