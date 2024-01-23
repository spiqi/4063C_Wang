#!/usr/bin/env python
import snowflake.connector

query = "SELECT 1"

# Gets the version
ctx = snowflake.connector.connect(
    user='<your_user_name>',
    password='<your_password>',
    account='<your_account_name>'
    )
cs = ctx.cursor()
try:
    cs.execute(query)
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()