#!/usr/bin/env python
import snowflake.connector
import os

# Query we will execute
query = "select user_name, event_timestamp from snowflake.account_usage.login_history order by event_timestamp desc"

# Define connection
ctx = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password= os.getenv('SNOWFLAKE_PASS'),
    account=os.getenv('SNOWFLAKE_ACCT'),
    role='ACCOUNTADMIN'
    )
try:
    # Create connection
    cs = ctx.cursor()

    # Get the results from a query.
    query = cs.execute(query)
    query_id = cs.sfqid
    print(query_id)
    for (user_name, event_timestamp) in query:
        print('{0}, {1}'.format(user_name, event_timestamp))
finally:
    cs.close()
ctx.close()