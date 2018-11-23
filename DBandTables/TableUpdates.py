# Run after creating tables
# insert your password wherever it says "your_password"

import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection


mydb = DatabaseConnection()
mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE Students ADD ApprovedBy VARCHAR(255)")
#
# mycursor.execute("ALTER TABLE Students ADD UserName VARCHAR(255)")
#
# mycursor.execute("ALTER TABLE Students ADD Password VARCHAR(255)")
#
# mycursor.execute("ALTER TABLE Instructors ADD UserName VARCHAR(255)")
#
# mycursor.execute("ALTER TABLE Instructors ADD Password VARCHAR(255)")

mycursor.execute("ALTER TABLE Students ADD IsDeleted INT")

mycursor.execute("ALTER TABLE Parents ADD IsDeleted INT")

mycursor.execute("ALTER TABLE AdditionalInfo ADD IsDeleted INT")

mycursor.execute("ALTER TABLE Instructors ADD IsDeleted INT")

mycursor.execute("ALTER TABLE Classes ADD IsDeleted INT")

mycursor.execute("ALTER TABLE Mentors ADD IsDeleted INT")

mycursor.execute("ALTER TABLE Takes ADD IsDeleted INT")



