SELECT  d.name , a.name , c.name , b.name FROM
(SELECT  ROW_NUMBER() over(order by Name) as r , name FROM OCCUPATIONS WHERE Occupation = 'Professor') a

LEFT JOIN (SELECT  ROW_NUMBER() over(order by Name) as r , name FROM OCCUPATIONS WHERE Occupation = 'Actor') b ON a.r = b.r

LEFT JOIN (SELECT  ROW_NUMBER() over(order by Name) as r , name FROM OCCUPATIONS WHERE Occupation = 'Singer') c ON a.r = c.r

LEFT JOIN (SELECT  ROW_NUMBER() over(order by Name) as r , name FROM OCCUPATIONS WHERE Occupation = 'Doctor') d ON a.r = d.r