with cteactivity AS 
    (SELECT DISTINCT *
    FROM activities)
SELECT sell_date,
		 count(product) AS num_sold,
		 string_agg(product, ',') within group (order by product) AS products
FROM cteactivity
GROUP BY  sell_date
ORDER BY  sell_date