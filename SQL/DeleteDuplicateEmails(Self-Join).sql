DELETE p2
FROM Person p1
JOIN Person p2
ON p1.Email = p2.Email
WHERE p1.id< p2.id;