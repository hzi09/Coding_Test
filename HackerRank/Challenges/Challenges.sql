WITH challenge_counts AS (
  SELECT
    hacker_id,
    COUNT(*) AS total
  FROM challenges
  GROUP BY hacker_id
),
max_total AS (
  SELECT MAX(total) AS max_total FROM challenge_counts
),
duplicates AS (
  SELECT total
  FROM challenge_counts
  GROUP BY total
  HAVING COUNT(*) > 1
),
filtered AS (
  SELECT cc.hacker_id, h.name, cc.total
  FROM challenge_counts cc
  JOIN hackers h ON cc.hacker_id = h.hacker_id
  WHERE cc.total = (SELECT max_total FROM max_total)
     OR (cc.total NOT IN (SELECT total FROM duplicates))
)
SELECT *
FROM filtered
ORDER BY total DESC, hacker_id;
