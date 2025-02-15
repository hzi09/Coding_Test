SELECT name AS results 
FROM Users
WHERE user_id = (
                SELECT user_id
                FROM MovieRating
                GROUP BY user_id
                ORDER BY COUNT(*) DESC,
                        (SELECT name 
                         FROM Users u 
                         WHERE u.user_id = MovieRating.user_id)
                LIMIT 1)

UNION ALL

SELECT m.title AS results
FROM Movies m 
WHERE m.movie_id = (SELECT movie_id
                    FROM MovieRating
                    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
                    GROUP BY movie_id
                    ORDER BY AVG(rating) DESC, movie_id ASC
                    LIMIT 1)