DELIMITER //

CREATE PROCEDURE print (IN n INTEGER)
BEGIN
    DECLARE x INTEGER;
    SET x = n;
    
    WHILE n > 0 DO
        SELECT REPEAT('* ', x - n + 1);
        SET n = n - 1 ;
    END WHILE;
END //

CALL print(20);