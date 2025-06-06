SELECT MEMBER_NAME, REVIEW_TEXT, 
       DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE M JOIN REST_REVIEW R ON M.MEMBER_ID = R.MEMBER_ID
WHERE M.MEMBER_ID = (SELECT MEMBER_ID
                   FROM REST_REVIEW
                   GROUP BY MEMBER_ID
                   ORDER BY COUNT(*) DESC
                   LIMIT 1)
ORDER BY 3, 2