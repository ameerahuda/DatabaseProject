import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
from Classes.Objects import *
from MySQLFunctions.insertSQL import *
import uuid
from datetime import datetime

mydb = DatabaseConnection()
mycursor = mydb.cursor()


# testing insert into Students table
id = str(uuid.uuid4())[:12]
registrationDate = datetime.strptime("01/20/2013", '%m/%d/%Y')
birthDate = datetime.strptime("01/15/2018", '%m/%d/%Y')
stu1  = Student(str(id), registrationDate, "Accepted", "Ameera", "Huda", "A", "N/A", "Ameera",
               birthDate, "Female", "American", "123 Bagby Avenue", "Waco", "TX", "76706", "ameera_huda@aylor.edu", "832-492-7881", "None",
               "None", "N/A", "Baylor University", "Waco ISD", "Provate", "Senior", "2020",
               "2020", "No", "No", "Jane Doe", "ameera15", "pwd15", "0")
insertStudent(stu1)

# testing insert into Parents table
pid = str(uuid.uuid4())[:12]
parent1 = Parent(pid, id, "John", "Doe", "123 Bagby Avenue", "Waco", "TX", "76706", "perentemail@google.com", "832-492-7881",
               "123-456-7890", "N/A", "0")
insertParent(parent1)

# testing insert into AdditionalInfo table
addInfo = AdditionalInformation(id, "2018", "11", "Accepted", "N/A", "N/A", "N/A", "0")
insertAdditionalInfo(addInfo)

# testing insert into Instructors table
iid = str(uuid.uuid4())[:12]
instructor1 = Instructor(iid, "Janice", "Doen", "jdoen", "jdoen123", "0")
insertInstructor(instructor1)

# testing insert into Classes table
cid = str(uuid.uuid4())[:12]
class1 = Class(cid, "Database 1", iid, "1", "3", "9:45 - 10:45", "Cashion", "334", "30",
               "25", "0", "0")
insertClass(class1)

# testing insert into Mentors table
mentor1 = Mentor(iid, id, "0")
insertMentor(mentor1)

# testing insert into Takes table
take1 = Take(id, cid, "0")
insertTake(take1)

