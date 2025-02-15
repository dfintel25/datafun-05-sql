-- query_filter.sql

-- Get books published after 2010
SELECT title, publication_year
FROM books
WHERE publication_year > 2010;

-- Get authors born before 1950
SELECT name, birth_year
FROM authors
WHERE birth_year < 1950;
