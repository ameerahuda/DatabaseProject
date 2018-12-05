class Student:
  def __init__(self, id, DateOfRegistration, AcceptedStatus, FirstName, LastName, MiddleInitial, Suffix, PreferredName,
               DateOfBirth, Gender, Race, Address, City, State, Zip, Email, PhoneNumber, DisabilityInfo,
               HealthConditions, Siblings, SchoolName, SchoolDistrict, SchoolType, GradeInFall, ExpectedHighSchool,
               ExpectedGradYear, GT, ELL, ApprovedBy, UserName, Password, IsDeleted):
    self.id = id
    self.DateOfRegisteration = DateOfRegistration
    self.AceeptedStatus = AcceptedStatus
    self.FirstName = FirstName
    self.LasName = LastName
    self.MiddleInitial = MiddleInitial
    self.Suffix = Suffix
    self.PreferredName = PreferredName
    self.DateOfBirth = DateOfBirth
    self.Gender = Gender
    self.Race = Race
    self.Address = Address
    self.City = City
    self.State = State
    self.Zip = Zip
    self.Email = Email
    self.PhoneNumber = PhoneNumber
    self.DisabilityInfo = DisabilityInfo
    self.HealthConditions = HealthConditions
    self.Siblings = Siblings
    self.SchoolName = SchoolName
    self.SchoolDistrict = SchoolDistrict
    self.SchoolType = SchoolType
    self.GradeInFall = GradeInFall
    self.ExpectedHighSchool = ExpectedHighSchool
    self.ExpectedGradYear = ExpectedGradYear
    self.GT = GT
    self.ELL = ELL
    self.ApprovedBy = ApprovedBy
    self.UserName = UserName
    self.Password = Password
    self.IsDeleted = IsDeleted


class Parent:
  def __init__(self, ParentID, StudentID, FirstName, LastName, Address, City, State, Zip, Email, CellPhoneNumber,
               WorkPhoneNumber, HomePhoneNumber, IsDeleted):
    self.ParentID = ParentID
    self.StudentID = StudentID
    self.FirstName = FirstName
    self.LastName = LastName
    self.Address = Address
    self.City = City
    self.State = State
    self.Zip = Zip
    self.Email = Email
    self.CellPhoneNumber = CellPhoneNumber
    self.WorkPhoneNumber = WorkPhoneNumber
    self.HomePhoneNumber = HomePhoneNumber
    self.IsDeleted = IsDeleted

class AdditionalInformation:
  def __init__(self, StudentID, YearAccepted, GradeWhenAccepted, Status, FundingStatus, GrantName, NationalClearingHouse, IsDeleted):
    self.StudentID = StudentID
    self.YearAccepted = YearAccepted
    self.GradeWhenAccepted = GradeWhenAccepted
    self.Status = Status
    self.FundingStatus = FundingStatus
    self.GrantName = GrantName
    self.NationalClearingHouse = NationalClearingHouse
    self.IsDeleted = IsDeleted

class Instructor:
  def __init__(self, InstructorID, FirstName, LastName, Username, Password, IsDeleted):
    self.InstructorID = InstructorID
    self.FirstName = FirstName
    self.LastName = LastName
    self.Username = Username
    self.Password = Password
    self.IsDeleted = IsDeleted

class Class:
  def __init__(self, ClassID, ClassName, InstructorID, Session, Level, TimeSlot, Building, RoomNumber, Capacity,
               NumOfStudentsRegistered, NumOfStudentsWaitlisted, IsDeleted):
    self.ClassID = ClassID
    self.ClassName = ClassName
    self.InstructorID = InstructorID
    self.Session = Session
    self.Level = Level
    self.TimeSlot = TimeSlot
    self.Building = Building
    self.RoomNumber = RoomNumber
    self.Capacity = Capacity
    self.NumOfStudentsRegistered = NumOfStudentsRegistered
    self.NumOfStudentsWaitlisted = NumOfStudentsWaitlisted
    self.IsDeleted = IsDeleted

class Mentor:
  def __init__(self, InstructorID, StudentID, IsDeleted):
    self.InstructorID = InstructorID
    self.StudentID = StudentID
    self.IsDeleted = IsDeleted

class Take:
  def __init__(self, StudentID, ClassID, IsDeleted):
    self.StudentID = StudentID
    self.ClassID = ClassID
    self.IsDeleted = IsDeleted

class Applicant:
  def __init__(self, StudentID, AcceptedStatus):
    self.StudentID = StudentID
    self.AcceptedStatus = AcceptedStatus