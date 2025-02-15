-- query_group_by.sql

-- Get the number of books per author
SELECT authors.name, COUNT(books.book_id) AS book_count
FROM authors
LEFT JOIN books ON authors.author_id = books.author_id
GROUP BY authors.name;

-- Get the average publication year of books per author
SELECT authors.name, AVG(books.year_published) AS avg_year
FROM authors
LEFT JOIN books ON authors.author_id = books.author_id
GROUP BY authors.name;
