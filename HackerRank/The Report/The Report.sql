SELECT 
    CASE WHEN G.Grade >= 8 THEN S.Name
         ELSE 'NULL'END AS Name,
         G.Grade,
         S.Marks
FROM Students S JOIN Grades G ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
ORDER BY 
    G.Grade DESC,
    CASE WHEN g.Grade >= 8 THEN s.Name
         ELSE NULL END ASC,
    CASE WHEN g.Grade < 8 THEN s.Marks
        ELSE NULL END ASC