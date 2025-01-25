-- Insert Books
INSERT INTO Books (Title, Genre, PublicationYear, AvailableCopies, TotalCopies)
VALUES ('The Catcher in the Rye', 'Fiction', 1951, 5, 10);

-- Insert Authors
INSERT INTO Authors (Name) VALUES ('J.D. Salinger');

-- Insert BookAuthors (many-to-many)
INSERT INTO BookAuthors (BookID, AuthorID) VALUES (1, 1);

-- Insert Customers
INSERT INTO Customers (Name, Email, PhoneNumber) VALUES ('John Doe', 'john@example.com', '1234567890');

-- Insert Borrowing Records
INSERT INTO Borrowing (BookID, CustomerID, IssueDate, ReturnDate) 
VALUES (1, 1, '2025-01-10', '2025-01-20');
