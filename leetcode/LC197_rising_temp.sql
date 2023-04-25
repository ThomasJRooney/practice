SELECT x.id FROM weather x, weather y WHERE x.temperature > y.temperature AND DATEDIFF(x.recordDate, y.recordDate) = 1;
