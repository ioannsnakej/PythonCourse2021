SELECT name, volume, 'drinks' AS category
FROM drinks
UNION
SELECT name, weight, 'meals' AS category
FROM meals;

WITH cte_movies_genres AS (
    SELECT m.movie_title
          ,m.director
          ,m.year
          ,g.genre_title
    FROM movies m
        INNER JOIN genres g ON m.genre_id = g.genre_id
    WHERE m.year > 1990
)
SELECT movie_title, director, genre_title
FROM cte_movies_genres
ORDER BY year ASC;