// Assignment 3 - Structured Thinking \\
use role accountadmin;


-- Find a dataset with daily metrics over one month (e.g., date, response time, avg runtime, number of queries executed). 
-- hint: SNOWFLAKE.ACCOUNT_USAGE

-- START_TIME
-- END_TIME
--  *TOTAL_ELAPSED_TIME*
-- ROWS_PRODUCED
-- COMPILATION_TIME
-- EXECUTION_TIME
-- TRANSACTION_BLOCKED_TIME;

SELECT AVG(TOTAL_ELAPSED_TIME) 
-- AS AveragePrice 
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY;

-- AVG(TOTAL_ELAPSED_TIME)
-- 65.199894


SELECT AVG(TOTAL_ELAPSED_TIME) 
-- AS AveragePrice 
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
where START_TIME between '2024-01-16' and '2024-01-17';

-- 16th 
-- AVG(TOTAL_ELAPSED_TIME)
-- 57.719481

SELECT AVG(TOTAL_ELAPSED_TIME) 
-- AS AveragePrice 
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
where START_TIME between '2024-01-18' and '2024-01-19';

-- AVG(TOTAL_ELAPSED_TIME)
-- 44.351217

SELECT
  DATE_TRUNC('DAY', START_TIME) AS query_day,
  AVG(EXECUTION_TIME) AS avg_query_runtime
FROM
  SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
GROUP BY
  query_day
ORDER BY
  AVG_QUERY_RUNTIME desc;


-- 2024-01-22 00:00:00.000 -0800	110.706587
-- 2024-01-11 00:00:00.000 -0800	94.783784
    
-- 2024-01-22
-- 2024-01-11

-- large table scans 
-- complex aggregations
-- shitty sql 

SELECT * 
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
where START_TIME between '2024-01-20' and '2024-01-23'
order by TOTAL_ELAPSED_TIME desc;

-- select * was returning all rows from a table... 
-- BYTES_SCANNED is high on top ten queries 
-- PARTITIONS_SCANNED is higher on queries with high runtime
-- COMPILATION_TIME was higher on the queries with high runtime


-- 2024-01-22
