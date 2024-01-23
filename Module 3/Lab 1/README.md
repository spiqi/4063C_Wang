# Module 3 Lab: Snowflake + Python
You will learn how to connect to Snowflake and execute a query using python.

## Getting Started

### Dependencies

* Python installed
    * See [Downloading Python](https://wiki.python.org/moin/BeginnersGuide/Download)
* Access to Snowflake sandbox
    * See [Downloading Python](https://uc.instructure.com/courses/1666166/pages/module-2-snowflake-info?module_item_id=71810477)
*  Snowflake Connector for Python
     * You'll do this via the Python package installer 'pip' by running the following command

        ```
        pip install --upgrade snowflake-connector-python
    * See [Installing the Python Connector](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-install)
* [4063C_24](https://github.com/IT4063/4063C_24) repo forked and cloned to your machine
    * See [Forking a Repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
    * See [Cloning a Repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
* Environment variables set
    * Run the following command to add your Snowflake User and Pass to your environment variables
        * MAC/LINUX
            ```
            export SNOWFLAKE_PASS='password'
            export SNOWFLAKE_USER='username'
            export SNOWFLAKE_ACCT='isa12503.east-us-2.azure'
        * PC
            ```
            set SNOWFLAKE_PASS=password
            set SNOWFLAKE_USER=username 
            set SNOWFLAKE_ACCT=isa12503.east-us-2.azure
    * See [Connecting to Snowflake with the Python Connector](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-connect)


### 1. Test the connection
Use test_connection.py to test the connection to snowflake
* Open up a terminal, change directories to your repo, and run the following command:

    ```
    python test_connection.py
### 2. Executing queries
Use the run_query.py script to query Snowflake
* Open run_query.py in the IDE of your choice
* Replace query variable value with the query you'd like to run
* Open up a terminal change directories to your repo, and run the following command:

    ```
    python run_query.py
    
## Guides, useful resources, references etc.
* [Ask your classmates](https://uc.instructure.com/courses/1666166/discussion_topics/8564268)
* [Ask Stack Overflow](https://stackoverflow.com/)
* [Ask the Snowflake Community](https://community.snowflake.com/s/)
* [Ask the Python Community](https://www.python.org/community/)
* [Ask the VS Code Community](https://code.visualstudio.com/community)
* [Ask ChatGPT](https://chat.openai.com/)
* [Snowflake: Getting Started with Python ](https://quickstarts.snowflake.com/guide/getting_started_with_python/index.html?index=..%2F..index#5)
* [Microsoft: Introduction to Python ](https://vscodeedu.com/courses/intro-to-python)



## Help
### Schedule Office Hours 

* [link](https://uc.instructure.com/courses/1666166#:~:text=Request%20Office%20Hours,an%20external%20site.) 
### Contact me via email
* burrelbn@mail.uc.edu

## Author

[@bjornburrell](https://github.com/bjornburrell)
