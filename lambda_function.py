import datetime
import json
import pymysql
import sys

def lambda_handler(event, context):
    rds_host  = $RDS
    name = $USERNAME
    password = $PASSWORD
    db_name = $DATABASE
    # get table name form API url example  https://execute-api.amazonaws.com/prod/?get-table=student    
    try:
        db_table = event['get-table']
    except NameError:
        print('table not defined')

    print("Trying to connect to DB...")
    # connect to database
    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(e)
        sys.exit()
        
    print("inside function")
    with conn.cursor() as cur:
        # SQL query
        cur.execute("SELECT * FROM {}".format(db_table))
        rows = cur.fetchall()
        # time stamps need to converted to string for json
        json_rows = json.dumps(rows, indent=4, sort_keys=True, default=str)
        print(json_rows)
        return {
            "statusCode": 200,
            "body": json_rows,
            "table": db_table
        }
