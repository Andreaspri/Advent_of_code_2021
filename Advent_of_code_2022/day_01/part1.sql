
-- Making temp tables to store the values extracted later
DROP TABLE IF EXISTS #vals
CREATE TABLE #vals (val INT)
DROP TABLE IF EXISTS #sums
CREATE TABLE #sums (sum INT)

DECLARE @pos INT = 1
DECLARE @len BIGINT = (SELECT LEN(inputData) FROM Advent_Of_Code_2022 WHERE day = 1)
DECLARE @inputData VARCHAR(MAX) = (SELECT inputData FROM Advent_Of_Code_2022 WHERE day = 1)

WHILE @pos < @len
BEGIN

    DECLARE @nextPos INT = (SELECT CHARINDEX(CHAR(10), @inputData, @pos))

    IF (@nextPos - @pos = 0)
    BEGIN
    -- This means that a new group is starting
        INSERT INTO #sums 
            SELECT SUM(val) FROM #vals
        DELETE FROM #vals WHERE 1 = 1
        -- Continue to next iteration
        SET @pos = @nextPos + 1
        CONTINUE
    END

    DECLARE @val INT = (SELECT SUBSTRING(@inputData, @pos, @nextPos - @pos))
    INSERT INTO #vals VALUES (@val)
    SET @pos = @nextPos + 1

END

SELECT MAX(sum) AS Solution
FROM #sums