import sqlite3
con = sqlite3.connect("../library.db")
cursor = con.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    print("Таблица создана")

def get_books_by_author(author):
    cursor = con.execute("""
    SELECT * FROM books
    WHERE author = ?
    ORDER BY name ASC
    """, (author,))

    books = cursor.fetchall()

    if books:
        for book in books:
            print(book)
    else:
        print("Книги этого автора не найдены")

def insert_books():
    books = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 500, 10),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 7),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Novel", 430, 4),
        ("War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 3),
        ("The Alchemist", "Paulo Coelho", 1988, "Adventure", 208, 6),
        ("The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fairy tale", 96, 8),
        ("Sherlock Holmes", "Arthur Conan Doyle", 1892, "Detective", 221, 5),
        ("Brave New World", "Aldous Huxley", 1932, "Dystopia", 311, 4),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 6)
    ]

    con.executemany("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?), ("Where the crawdads sing" , "Enolla" , 2020, "Romance" , 230, 5)
    """, books)

cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

for book in books:
    print(book)

    con.commit()
    print("Книги добавлены")

if __name__ == "__main__":
    create_table()
    insert_books()
    con.close()