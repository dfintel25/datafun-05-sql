-- query_sorting.sql

-- Get all books ordered by publication year (ascending)
SELECT title, year_published
FROM books
ORDER BY year_published ASC;

-- Get authors ordered by their birth year (descending)
--SELECT author.id, birth_year
--FROM authors
--ORDER BY birth_year DESC;
