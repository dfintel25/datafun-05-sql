-- query_aggregation.sql

-- Count the number of books
SELECT COUNT(*) AS total_books
FROM books;

-- Calculate the average publication year of books
SELECT AVG(publication_year) AS average_year
FROM books;

-- Calculate the total number of books per author (using SUM)
SELECT authors.name, COUNT(books.book_id) AS total_books
FROM authors
LEFT JOIN books ON authors.author_id = books.author_id
GROUP BY authors.name;
