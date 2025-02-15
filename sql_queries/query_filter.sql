-- query_filter.sql

-- Get books published after 2010
SELECT title, year_published
FROM books
WHERE year_published > 2010;

-- Get authors born before 1950
SELECT name, birth_year
FROM authors
WHERE birth_year < 1950;
