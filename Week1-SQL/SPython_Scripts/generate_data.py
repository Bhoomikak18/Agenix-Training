import psycopg2
from faker import Faker
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database credentials from environment variables
dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

# Connect to PostgreSQL using the credentials from .env
conn = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host, port=port
)
cur = conn.cursor()

# Initialize Faker instance
fake = Faker()

# Generate and insert books
def insert_books():
    books = []
    genres = ["Fiction", "Comedy", "Thriller", "Romance", "Non-fiction", "Science Fiction", "Drama", "Fantasy"]

    for _ in range(20):  # Generate 20 books
        title = fake.catch_phrase()  # Generate a more realistic title using Faker
        genre = random.choice(genres)  # Select a random genre from the list
        pub_year = random.randint(1900, 2025)  # Random publication year
        available_copies = random.randint(1, 10)  # Random number of available copies
        total_copies = available_copies + random.randint(0, 5)  # Ensure total >= available

        # Insert into Books and fetch the generated BookID
        cur.execute(
            "INSERT INTO Books (Title, Genre, PublicationYear, AvailableCopies, TotalCopies) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING BookID",
            (title, genre, pub_year, available_copies, total_copies),
        )
        book_id = cur.fetchone()[0]  # Fetch the generated BookID (integer)
        print(f"Inserted Book with ID: {book_id}")  # Debugging print
        books.append(book_id)  # Append the integer BookID to the list

    return books

# Generate and insert authors
def insert_authors():
    authors = []
    for _ in range(10):  # Generate 10 authors
        name = fake.name()

        # Insert into Authors and fetch the generated AuthorID
        cur.execute("INSERT INTO Authors (Name) VALUES (%s) RETURNING AuthorID", (name,))
        author_id = cur.fetchone()[0]  # Fetch the generated AuthorID (integer)
        print(f"Inserted Author with ID: {author_id}")  # Debugging print
        authors.append(author_id)  # Append the integer AuthorID to the list
    return authors

# Generate and insert book-author relationships
def insert_book_authors(books, authors):
    for book_id in books:
        author_id = random.choice(authors)  # Randomly assign a valid AuthorID to a BookID
        print(f"Preparing to insert into BookAuthors: BookID = {book_id}, AuthorID = {author_id}")  # Debugging print
        
        # Ensure both values are integers before proceeding with the insert
        if isinstance(book_id, int) and isinstance(author_id, int):
            cur.execute(
                "INSERT INTO BookAuthors (BookID, AuthorID) VALUES (%s, %s)",
                (book_id, author_id),
            )
            print(f"Inserted into BookAuthors: BookID = {book_id}, AuthorID = {author_id}")  # Debugging print
        else:
            print(f"Skipping invalid data: BookID = {book_id}, AuthorID = {author_id}")  # Debugging print

# Generate and insert customers
def insert_customers():
    customers = []
    for _ in range(30):  # Generate 30 customers
        name = fake.name()[:15]  # Truncate name to 15 characters
        email = fake.email()[:15]  # Truncate email to 15 characters
        phone = fake.phone_number()[:15]  # Truncate phone number to 15 characters
        cur.execute(
            "INSERT INTO Customers (Name, Email, PhoneNumber) VALUES (%s, %s, %s) RETURNING CustomerID",
            (name, email, phone),
        )
        customer_id = cur.fetchone()[0]  # Fetch the generated ID
        customers.append(customer_id)
    return customers


# Generate and insert borrowings
def insert_borrowings(books, customers):
    for _ in range(50):  # Generate 50 borrowings
        book_id = random.choice(books)
        customer_id = random.choice(customers)
        issue_date = fake.date_this_decade()
        return_date = fake.date_this_decade() if random.choice([True, False]) else None
        
        # Make sure return_date is later than issue_date
        if return_date and return_date < issue_date:
            return_date = None
        
        cur.execute(
            "INSERT INTO Borrowing (BookID, CustomerID, IssueDate, ReturnDate) VALUES (%s, %s, %s, %s)",
            (book_id, customer_id, issue_date, return_date),
        )

# Main function to insert all data
def insert_data():
    try:
        # Insert authors and get their IDs
        authors = insert_authors()

        # Insert books and get their IDs
        books = insert_books()

        # Insert book-author relationships
        insert_book_authors(books, authors)

        # Insert customers and get their IDs
        customers = insert_customers()

        # Insert borrowings
        insert_borrowings(books, customers)

        # Commit all changes to the database
        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {e}")

# Run the data insertion process
insert_data()

# Close the connection
cur.close()
conn.close()
