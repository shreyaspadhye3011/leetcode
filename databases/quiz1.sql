SELECT SUM(ORDERQTY) AS TOTSALES 
FROM SALESORDERDETAIL
GROUP BY YEAR
