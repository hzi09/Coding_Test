SELECT id, age, coins_needed, power
FROM Wands W JOIN Wands_Property WP ON W.code = WP.code
WHERE WP.is_evil != 1
    AND coins_needed = (
        SELECT MIN(coins_needed)
        FROM Wands W2
        JOIN Wands_Property WP2 ON W2.code = WP2.code
        WHERE WP2.is_evil != 1 AND W2.power = W.power AND WP2.age = WP.age
    )
ORDER BY 4 DESC, 2 DESC