-- query_join.sql

-- Get books with their authors (INNER JOIN)
SELECT books.title, authors.name
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;

-- Get all authors and their books (LEFT JOIN)
SELECT authors.name, books.title
FROM authors
LEFT JOIN books ON authors.author_id = books.author_id;
