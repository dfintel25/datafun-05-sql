-- query_sorting.sql

-- Get all books ordered by publication year (ascending)
SELECT title, publication_year
FROM books
ORDER BY publication_year ASC;

-- Get authors ordered by their birth year (descending)
SELECT name, birth_year
FROM authors
ORDER BY birth_year DESC;
