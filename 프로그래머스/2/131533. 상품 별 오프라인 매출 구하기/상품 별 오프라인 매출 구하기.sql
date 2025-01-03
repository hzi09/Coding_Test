SELECT P.PRODUCT_CODE, (SUM(O.SALES_AMOUNT) * PRICE) AS SALES
FROM PRODUCT P INNER JOIN OFFLINE_SALE O ON P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY P.PRODUCT_ID
ORDER BY SALES DESC, P.PRODUCT_CODE