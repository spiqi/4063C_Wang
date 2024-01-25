import snowflake.connector
import os

# Gets the version
ctx = snowflake.connector.connect(
    user= os.getenv('SNOWFLAKE_USER'),
    password= os.getenv('SNOWFLAKE_PASS'),
    account=os.getenv('SNOWFLAKE_ACCT'),
    role='ACCOUNTADMIN'
    )
cs = ctx.cursor()
try:
 cs.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")
 cs.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb_mg")
 cs.cursor().execute("USE DATABASE testdb_mg")
 cs.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema_mg")
finally:
    cs.close()
ctx.close()
