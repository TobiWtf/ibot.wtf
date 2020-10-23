CREATE TABLE
IF NOT EXISTS
test_table
(column_1 TEXT,
  column_2 INT);

/* Creates a table test_table if it doesnt exist already*/


INSERT INTO
test_table
VALUES ("TEST", 1002);

/*inserts some dummy data into test_table*/

SELECT *
FROM test_table
WHERE column_1 = "TEST";

/*Selects the dummy data from the table and returns it to client*/

/*OUTPUT: "[(1002,),]"*/
