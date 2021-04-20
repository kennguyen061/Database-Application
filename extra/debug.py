import csv
import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

#for resetting database
class debug:
    def __init__(self):
        try: self.dbConnection = mysql.connector.connect(host="db1.cwkukgaf0ib6.us-east-1.rds.amazonaws.com",
                                               user="jbinz",
                                               passwd="password")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        self.cursor = self.dbConnection.cursor()
    
    def resetDB( self, dbName ):
        cmd = "DROP SCHEMA " + dbName
        self.cursor.execute(cmd)
        cmd = "create database " + dbName
        self.cursor.execute(cmd)

    
    def createDB( self, dbName ):
        cmd = "create database " + dbName
        self.cursor.execute(cmd)

debug = debug()
debug.resetDB("p4ex")
