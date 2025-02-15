DELETE FROM books
WHERE book_id IN (
    SELECT book_id FROM books
    JOIN authors ON books.author_id = authors.author_id
    WHERE authors.name = 'Rowling'
);