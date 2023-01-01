DELIMITER //

CREATE PROCEDURE print (IN n INTEGER)
BEGIN
    WHILE n > 0 DO
        SELECT REPEAT('* ', n);
        SET n = n - 1;
    END WHILE;
END //

CALL print(20)