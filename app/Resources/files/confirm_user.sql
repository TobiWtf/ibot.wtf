/*
This is a SQL query
set for a confirmation
table i built :))
*/

CREATE TABLE
confirmation
(user_id TEXT,
  reset TEXT);

/*
This creates a TABLE
for confirming the user
*/

INSERT INTO
confirmation
VALUES (?, ?);

/*
This inserts
values into our
created table
*/

SELECT user_id
FROM confirmation
WHERE user_id = ?;

/*
This selects
the user id from
the table  the
user id is the same
as user_id
*/

INSERT INTO
confirmation
VALUES (?, ?);

/*
This inserts a user
id and a dummy value
"RESET"
*/

DELETE FROM
confirmation
WHERE user_id = ?;

/*
This deletes a user
from the Database
table layer
*/

DELETE FROM
confirmation
WHERE reset = ?;

/*
This deletes all records
*/

/*
This script is an example
of database query strings
i use while building backends
in Sqlite3
*/
