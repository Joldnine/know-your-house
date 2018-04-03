import sys
import logging
import pymysql
import rds_config
import json

# rds settings
rds_host = "cs5224.ck6brzp5fs3z.ap-southeast-1.rds.amazonaws.com"
db_username = rds_config.db_username
db_password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

print(db_username)


conn = pymysql.connect(rds_host, user=db_username, passwd=db_password, db=db_name, connect_timeout=5)


logger.info("SUCCESS: Connection to RDS mysql instance succeeded")


def post(event, context):
    event = json.loads(event['body'])  # comment this line if it is in aws
    """
    This function fetches content from mysql RDS instance
    """
    street = event['street'].upper()
    rows = []
    town = ''
    with conn.cursor() as cur:
        cur.execute('SELECT DISTINCT town, street_name FROM cs5224.ResalePrices;')
        if cur.rowcount > 0:
            for row in cur:
                if row[0] in street or street in row[1] or row[1] in street:
                    town = row[0]
                    break

    return {"body": json.dumps({'town': town}), "statusCode": 200}
