import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
"""from Classes.Objects import *
from MySQLFunctions.updateSQL import *
import uuid
import re
from datetime import datetime"""

db = DatabaseConnection()
c = db.cursor()

print(db)