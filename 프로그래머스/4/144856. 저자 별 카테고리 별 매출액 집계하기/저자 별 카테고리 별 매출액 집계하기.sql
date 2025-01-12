SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY,
       SUM(BS.SALES * B.PRICE) AS TOTAL_SALES
FROM AUTHOR A JOIN BOOK B ON A.AUTHOR_ID = B.AUTHOR_ID
              JOIN BOOK_SALES BS ON B.BOOK_ID = BS.BOOK_ID
WHERE BS.SALES_DATE LIKE '2022-01-%'
GROUP BY A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
ORDER BY A.AUTHOR_ID ASC, B.CATEGORY DESC