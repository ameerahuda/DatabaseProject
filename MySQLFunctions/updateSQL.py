import mysql.connector as sql
from DBandTables.ConnectionToDB import DatabaseConnection
from Classes.Objects import *

def updateStudent(Student):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Students SET FirstName = %s, LastName = %s, " \
			   "MiddleInitial = %s, Suffix = %s, PreferredName = %s, " \
			   "DateOfBirth = %s, Gender = %s, Race = %s, Address = %s, " \
			   "City = %s, State = %s, Zip = %s, Email = %s, " \
			   "PhoneNumber = %s, DisabilityInfo = %s, HealthConditions = " \
			   "%s, Siblings %s, SchoolName = %s, SchoolDistrict = %s, " \
			   "SchoolType = %s, GradeInFall = %s, ExpectedHighSchool = %s, " \
			   "ExpectedGradYear = %s, GT = %s, ELL = %s, UserName = %s, " \
			   "Password = %s WHERE StudentID = %s"
		vals = (Student.FirstName, Student.LastName, Student.MiddleInitial, Student.Suffix, Student.PreferredName, Student.DateOfBirth, Student.Gender, Student.Race, Student.Address, Student.City, Student.State, Student.Zip, Student.Email, Student.PhoneNumber, Student.DisabilityInfo, Student.HealthConditions, Student.Siblings, Student.SchoolName, Student.SchoolDistrict, Student.SchoolType, Student.GradeInFall, Student.ExpectedHighSchool, Student.ExpectedGradYear, Student.GT, Student.ELL, Student.UserName, Student.Password, Student.id)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateApplicant(Student):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Students SET DateOfRegistration = %s, AcceptedStatus = %s WHERE StudentID = %s"
		vals = (Student.DateOfRegistration, Student.AcceptedStatus, Student.id)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateParent(Parent):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Parents SET FirstName = %s, LastName = %s, Address = %s, " \
			   "City = %s, State = %s, Zip = %s, Email = %s, " \
			   "CellPhoneNumber = %s, WorkPhoneNumber = %s, HomePhoneNumber = " \
			   "%s WHERE ParentID = %s AND StudentID = %s"
		vals = (Parent.StudentID, Parent.FirstName, Parent.LastName, Parent.Address, Parent.City, Parent.State, Parent.Zip, Parent.Email, Parent.CellPhoneNumber, Parent.WorkPhoneNumber, Parent.HomePhoneNumber, Parent.ParentID, Parent.StudentID)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateMentor(oldMentor, newMentor):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Mentor SET InstructorID = %s, StudentID = %s WHERE InstructorID = %s AND StudentID = %s"
		vals = (newMentor.InstructorID, newMentor.StudentID, oldMentor.InstructorID, oldMentor.InstructorID)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateInstructor(Instructor):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Instructors SET FirstName = %s, LastName = %s, " \
			   "UserName = %s, Password = %s WHERE StudentID = %s"
		vals = (Instructor.FirstName, Instructor.LastName, Instructor.UserName, Instructor.Password, Instructor.InstructorID)
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateClass(Class):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Classes SET ClassName = %s, InstructorID = %s, " \
			   "Session = %s, Level = %s, " \
			   "TimeSlot = %s, Building = %s, RoomNumber = %s, Capacity = %s, " \
			   "NumberOfStudentsRegistered = %s, NumberOfStudentsWaitListed = %s WHERE ClassID = %s"
		vals = (Class.InstructorID, Class.Session, Class.Level, Class.TimeSlot, Class.Building, Class.RoomNumber, Class.Capacity, Class.NumberOfStudentsRegistered, Class.NumberOfStudentsWaitListed, Class.ClassID)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateTake(oldTake, Take):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE Takes SET ClassID = %s WHERE StudentID = %s AND ClassID = %s"
		vals = (Take.ClassID, Take.StudentID, oldTake.ClassID)
		
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)

def updateAdditionalInfo(AdditionalInfo):
	try:
		db = DatabaseConnection()
		c = db.cursor()
		
		stmt = "UPDATE AdditionalInfo SET Status = %s, FundingStatus = %s, " \
			   "GrantName = %s, NationalClearingHouse = %s WHERE StudentID = %s"
		vals = (AdditionalInfo.Status, AdditionalInfo.FundingStatus, AdditionalInfo.GrantName, AdditionalInfo.NationalClearingHouse, AdditionalInfo.StudentID)
		c.execute(stmt, vals)
		
		db.commit()
	except (sql.Error, sql.Warning) as e:
		print(e)
		exit(0)