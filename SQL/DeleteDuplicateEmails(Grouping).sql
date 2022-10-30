DELETE FROM Person 
WHERE id NOT IN (
SELECT MIN(id) id 
    FROM Person
    GROUP BY email
)