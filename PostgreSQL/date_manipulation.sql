-- Suppose you have values ranging from 1-365 as indicates date of year. You wish to have a calendar date with format as YYYY-MM-DD

-- to_date()
-- ||

/*
https://www.postgresql.org/docs/10/functions-formatting.html
https://www.postgresql.org/docs/9.1/functions-string.html
https://www.postgresql.org/docs/9.4/functions-datetime.html

*/

SELECT to_date('2016-' || julian_day::text, 'IYYY-IDDD')
FROM glad_asia_2016 as g;


ALTER TABLE glad_asia_2016 ADD COLUMN date date;

UPDATE glad_asia_2016 f
SET date = g.date
FROM (
	SELECT id, to_date('2016-' || julian_day::text, 'IYYY-IDDD') as date
		FROM glad_asia_2016
) AS g
WHERE f.id = g.id;