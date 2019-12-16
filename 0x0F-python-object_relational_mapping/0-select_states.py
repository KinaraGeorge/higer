#!/usr/bin/python3
""" Python scripte to list items from MySQL"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()
    sql = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)
    cursor.close()
    conn.close()
