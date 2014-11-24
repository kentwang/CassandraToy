-- problem 1
SELECT votes FROM movies WHERE title = 'The Matrix (1999)';
-- problem 2 (Very complicated) Create multiple table and join
SELECT title FROM movies WHERE rank < 8.3 AND votes >= 400000;
-- problem 3
SELECT COUNT(*) FROM movies WHERE rank = 8.9 ALLOW FILTERING;
-- problem 4 (Very Complicated) Create Join
CREATE INDEX ON literature(bookauthor);

