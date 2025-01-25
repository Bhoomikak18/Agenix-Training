
CREATE TABLE Books (
    BookID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Genre VARCHAR(100) NOT NULL,
    PublicationYear INT NOT NULL,
    AvailableCopies INT NOT NULL CHECK (AvailableCopies >= 0),
    TotalCopies INT NOT NULL CHECK (TotalCopies >= 0)
);


CREATE TABLE Authors (
    AuthorID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);


CREATE TABLE BookAuthors (
    BookAuthorID SERIAL PRIMARY KEY,
    BookID INT NOT NULL REFERENCES Books(BookID) ON DELETE CASCADE,
    AuthorID INT NOT NULL REFERENCES Authors(AuthorID) ON DELETE CASCADE,
    UNIQUE (BookID, AuthorID)
);


CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(15) UNIQUE,
    );


CREATE TABLE Borrowing (
    BorrowingID SERIAL PRIMARY KEY,
    BookID INT NOT NULL REFERENCES Books(BookID) ON DELETE CASCADE,
    CustomerID INT NOT NULL REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    IssueDate DATE NOT NULL,
    ReturnDate DATE
);
