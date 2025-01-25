-- 1. Retrieve the top 5 most-issued books with their issue count.
-- Uses GROUP BY, COUNT, and ORDER BY with LIMIT:

SELECT 
     BookID, COUNT(*) AS IssueCount 
FROM 
     Borrowing 
GROUP BY 
     BookID 		
ORDER BY 
     IssueCount DESC 	
LIMIT 5;

-- 2. List books along with their authors that belong to the "Fantasy" genre, sorted by publication year in descending order.
-- Uses INNER JOIN and ORDER BY:
SELECT 
    Books.Title AS BookTitle, 
    Authors.Name AS AuthorName, 
    Books.PublicationYear AS PublicationYear
FROM 
    Books 
INNER JOIN 
    BookAuthors ON Books.BookID = BookAuthors.BookID
INNER JOIN 
    Authors ON BookAuthors.AuthorID = Authors.AuthorID
WHERE 
    Books.Genre = 'Fantasy' 
ORDER BY 
    Books.PublicationYear DESC;

-- 3. Identify the top 3 customers who have borrowed the most books.
-- Uses GROUP BY, COUNT, and LIMIT:

SELECT 
    CustomerID, COUNT(*) AS BorrowCount 
FROM 
    Borrowing 
GROUP BY 
    CustomerID 
ORDER BY 
    BorrowCount DESC 
LIMIT 3;

-- 4. List all customers who have overdue books.
-- Uses WHERE with a date condition and JOIN:

SELECT DISTINCT 
    Customers.CustomerID, Customers.Name 
FROM 
    Customers
INNER JOIN 
    Borrowing ON Customers.CustomerID = Borrowing.CustomerID
WHERE 
    Borrowing.ReturnDate IS NULL 
  AND 
    Borrowing.IssueDate < CURRENT_DATE - INTERVAL '30 days';


-- 5. Find authors who have written more than 3 books.
-- Uses GROUP BY and HAVING:

SELECT 
    Authors.Name AS AuthorName, COUNT(*) AS BookCount 
FROM 
    Authors 
INNER JOIN 
    BookAuthors ON Authors.AuthorID = BookAuthors.AuthorID
GROUP BY 
    Authors.AuthorID 
HAVING 
    COUNT(*) > 3;

-- 6. Retrieve a list of authors who have books issued in the last 6 months.
-- Uses DISTINCT with a JOIN and a date filter:

SELECT DISTINCT 
    Authors.Name AS AuthorName 
FROM 
    Authors 
INNER JOIN 
    BookAuthors ON Authors.AuthorID = BookAuthors.AuthorID
INNER JOIN 
    Borrowing ON BookAuthors.BookID = Borrowing.BookID
WHERE 
    Borrowing.IssueDate >= CURRENT_DATE - INTERVAL '6 months';

-- 7. Calculate the total number of books currently issued and the percentage of books issued compared to the total available.
-- Uses subqueries and COUNT:

SELECT 
    (SELECT COUNT(*) FROM Borrowing WHERE ReturnDate IS NULL) AS TotalIssuedBooks,
    ROUND((COUNT(*) / (SELECT SUM(TotalCopies) FROM Books)) * 100, 2) AS IssuedPercentage 
FROM 
    Borrowing 
WHERE 
    ReturnDate IS NULL;

-- 8. Generate a monthly report of issued books for the past year, showing month, book count, and unique customer count.
-- Uses GROUP BY, COUNT, and date formatting:

SELECT 
    TO_CHAR(IssueDate, 'YYYY-MM') AS Month, 
    COUNT(*) AS BookCount, 
    COUNT(DISTINCT CustomerID) AS UniqueCustomerCount 
FROM 
    Borrowing 
WHERE 
    IssueDate >= CURRENT_DATE - INTERVAL '1 YEAR'
GROUP BY 
    TO_CHAR(IssueDate, 'YYYY-MM') 
ORDER BY 
    Month;

-- 9. Add appropriate indexes to optimize queries.
-- Uses CREATE INDEX:

--CREATE INDEX idx_Borrowing_BookID ON Borrowing(BookID);
--CREATE INDEX idx_Books_Genre_PublicationYear ON Books(Genre, PublicationYear);
--CREATE INDEX idx_Borrowing_IssueDate ON Borrowing(IssueDate);
--CREATE INDEX idx_Borrowing_ReturnDate ON Borrowing(ReturnDate);
--CREATE INDEX idx_BookAuthors_BookID ON BookAuthors(BookID);

-- 10. Analyze query execution plans for at least two queries using EXPLAIN.
-- For Query 1:

EXPLAIN 
SELECT 
    BookID, COUNT(*) AS IssueCount 
FROM 
    Borrowing 
GROUP BY 
    BookID 
ORDER BY 
    IssueCount DESC 
LIMIT 5;

--•	For Query 2:

EXPLAIN SELECT 
    Books.Title AS BookTitle, 
    Authors.Name AS AuthorName, 
    Books.PublicationYear AS PublicationYear
FROM 
    Books 
INNER JOIN 
    BookAuthors ON Books.BookID = BookAuthors.BookID
INNER JOIN 
    Authors ON BookAuthors.AuthorID = Authors.AuthorID
WHERE 
    Books.Genre = 'Fantasy' 
ORDER BY 
    Books.PublicationYear DESC;
