SELECT CONCAT(Name, "(", LEFT(occupation, 1), ")")
FROM OCCUPATIONS
ORDER BY Name;

SELECT CONCAT("There are a total of ", COUNT(Occupation), " ", LOWER(Occupation), "s.")
FROM OCCUPATIONS
GROUP BY occupation
ORDER BY COUNT(Occupation), Occupation ASC;