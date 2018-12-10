from flask import Flask, render_template, request, json, redirect, url_for, session, send_file
from Endpoints import *
from Classes.Objects import *
from DBandTables import *
from MySQLFunctions.insertSQL import *
import uuid
from datetime import datetime
from MySQLFunctions.getSQL import *
from MySQLFunctions.updateSQL import *
from MySQLFunctions.deleteSQL import *
import random
from datetime import datetime

app = Flask(__name__)

# added for staying logged in
app.secret_key = 'secretkey'


# landing page endpoint
@app.route('/')
def main():
    return render_template('index.html')
    #return getCoursesByGrade("student_addOrDropCourse.html", 'Jamie51788')

# added for staying logged in
# @app.route('/')
# def index():
#    if 'username' in session:
#       username = session['username']
#       return render_template('student_editProfile.html')
#    return render_template('practiceSignIn.html')
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return render_template('practiceSignIn.html')
#
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('main'))

# 1st: show registration page
@app.route('/showSignUp')
def showSignUp():
    return render_template('registration.html')

# 2nd: registration endpoint
@app.route('/signUp', methods=['POST'])
def signUp():
    return json.dumps({'html': '<span>All fields good !!</span>'})

# 3rd (last Registration Endpoint): where information is received and saved to database for Registration (only if valid)
@app.route('/signUp/applied', methods=['POST'])
def afterapplied():
    # read in the values (if any) from the UI
    _fname = request.form['firstName']
    _lname = request.form['lastName']
    _initial = request.form['initial']
    _preferredName = request.form['preferredName']
    _suffix = request.form['suffix']
    _address = request.form['address']
    _city = request.form['city']
    _zip = request.form['zip']
    _state = request.form['state']
    _dob = request.form['dob']
    _gender = request.form['gender']
    _race = request.form['race']
    _email = request.form['email']
    _phoneNumber = request.form['phoneNumber']
    _siblings = request.form['siblings']
    _healthConditions = request.form['healthConditions']
    _disability = request.form['disability']
    _schoolName = request.form['schoolName']
    _schoolDistrict = request.form['schoolDistrict']
    _schoolType = request.form['schoolType']
    _gradeInFall = request.form['gradeInFall']
    _gt = request.form['gt']
    _ell = request.form['ell']
    _gradDate = request.form['gradDate']
    _expHighSchool = request.form['expHighSchool']

    # read in Parents 1, info (required)
    _p1fname = request.form['p1FirstName']
    _p1lname = request.form['p1LastName']
    _p1address = request.form['p1Address']
    _p1city = request.form['p1City']
    _p1state = request.form['p1State']
    _p1zip = request.form['p1Zip']
    _p1email = request.form['p1Email']
    _p1HomePhone = request.form['p1HomePhone']
    _p1phonenumber = request.form['p1PhoneNumber']
    _p1workphone = request.form['p1WorkPhone']

    # read in Parents 2, info (NOT required)
    _p2fname = request.form['p2FirstName']
    _p2lname = request.form['p2LastName']
    _p2address = request.form['p2Address']
    _p2city = request.form['p2City']
    _p2state = request.form['p2State']
    _p2zip = request.form['p2Zip']
    _p2email = request.form['p2Email']
    _p2HomePhone = request.form['p2HomePhone']
    _p2phonenumber = request.form['p2PhoneNumber']
    _p2workphone = request.form['p2WorkPhone']
    _dateOfRegistration = request.form['dateOfRegistration']

    # if any of the non-required fields are blank initialize with "N/A"
    if _initial == "":
        _initial = "N/A"

    if _preferredName == "":
        _preferredName = "N/A"

    if _suffix == "":
        _suffix = "N/A"

    if _address == "":
        _address = "N/A"

    if _city == "":
        _city = "N/A"

    if _zip == "":
        _zip = "N/A"

    if _state == "Choose...":
        _state = "N/A"

    if _dob == "":
        _dob = datetime.strptime("01/01/0001", '%m/%d/%Y')
    else:
        temp = _dob
        _dob = datetime.strptime(temp, '%m/%d/%Y')

    if _gender == "Choose...":
        _gender = "N/A"

    if _race == "Choose...":
        _race = "N/A"

    if _email == "":
        _email = "N/A"

    if _phoneNumber == "":
        _phoneNumber = "N/A"

    if _siblings == "":
        _siblings = "N/A"

    if _healthConditions == "":
        _healthConditions = "N/A"

    if _disability == "":
        _disability = "N/A"

    if _schoolName == "":
        _schoolName = "N/A"

    if _schoolDistrict == "":
        _schoolDistrict = "N/A"

    if _schoolType == "Choose...":
        _schoolType = "N/A"

    if _gradeInFall == "Choose...":
        _gradeInFall = "N/A"

    if _gt == "Choose...":
        _gt = "N/A"

    if _ell == "Choose...":
        _ell = "N/A"

    if _gradDate == "":
        _gradDate = "N/A"

    if _expHighSchool == "":
        _expHighSchool = "N/A"

    if _p2fname == "":
        _p2fname = "N/A"

    if _p2lname == "":
        _p2lname = "N/A"

    if _p2address == "":
        _p2address = "N/A"

    if _p2city == "":
        _p2city = "N/A"

    if _p2state == "Choose...":
        _p2state = "N/A"

    if _p2zip == "":
        _p2zip = "N/A"

    if _p2email == "":
        _p2email = "N/A"

    if _p2phonenumber == "":
        _p2phonenumber = "N/A"

    if _p2HomePhone == "":
        _p2HomePhone = "N/A"

    if _p2workphone == "":
        _p2workphone = "N/A"

    temp1 = _dateOfRegistration
    _dateOfRegistration = datetime.strptime(temp1, '%m/%d/%Y')

    sid = str(uuid.uuid4())[:12]
    p1id = str(uuid.uuid4())[:12]
    p2id = str(uuid.uuid4())[:12]

    # generating username: Contains firstname + random number (range: 10,000 to 99,999)
    num = random.randint(10000, 99999)

    # used in generating password
    ran = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!$?."
    plen = 8

    s = Student(str(sid), _dateOfRegistration, "N/A", _fname, _lname, _initial, _suffix, _preferredName, _dob, _gender, _race,
                _address, _city, _state, _zip, _email, _phoneNumber, _disability, _healthConditions, _siblings,
                _schoolName, _schoolDistrict, _schoolType, _gradeInFall, _expHighSchool, _gradDate, _gt, _ell,
                "N/A", _fname + str(num), ("".join(random.sample(ran, plen))), "0")
    parent1 = Parent(str(p1id), str(sid), _p1fname, _p1lname, _p1address, _p1city, _p1state, _p1zip, _p1email, _p1phonenumber,
                     _p1workphone, _p1HomePhone, "0")
    parent2 = Parent(str(p2id), str(sid), _p2fname, _p2lname, _p2address, _p2city, _p2state, _p2zip, _p2email, _p2phonenumber,
                     _p2workphone, _p2HomePhone, "0")

    insertStudent(s)
    insertParent(parent1)
    insertParent(parent2)

    return render_template('afterApplying.html')

# SIGN IN
@app.route('/showSignIn', methods=['POST', 'GET'])
def showSignIn():
    if 'username' in session:
        username = session['username']
        ## check if student or personnel
        if studentOrPersonnel(username) == "student entry":
            return redirect(url_for('showStudentProfile'))
        else:
            return redirect(url_for('personnelHome'))
    return render_template("signIn.html")

@app.route('/signIn', methods=['GET', 'POST'])
def signIn():
    # check if username even exists
    # if yes then do this
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('showSignIn'))
    # else redirect ot home page to register
    return render_template('index.html')


# @app.route('/signIn', methods=['POST'])
# def signIn():
#     return json.dumps({'html': '<span>All fields good !!</span>'})

@app.route('/signIn/student', methods=['POST', 'GET'])
def afterStudentSignIn():
    return render_template('signIn.html')

# PERSONNEL REGISTRATION
@app.route('/showAdminSignUp')
def showAdminSignUp():
    return render_template("personnelRegistration.html")

@app.route('/adminSignUp', methods=['POST'])
def adminSignUp():
    return json.dumps({'html': '<span>All fields good !!</span>'})

@app.route('/adminSignUp/applied', methods=['POST'])
def afteradminapplied():
    _adminFirstName = request.form['firstName']
    _adminLastName = request.form['lastName']
    _adminActivationCode = request.form['activationCode']
    _adminUserName = request.form['userName']
    _adminPassword = request.form['passWord']

    #admin == instructor
    adminID = str(uuid.uuid4())[:12]
    admin = Instructor(str(adminID), _adminFirstName, _adminLastName, _adminUserName, _adminPassword, "0")
    if getInstructorByUsernameOnly(admin.Username) == 0:
        insertInstructor(admin)
        return redirect(url_for('showSignIn'))
    else:
        return render_template('personnelRegistration.html')


# PERSONNEL APPROVAL
@app.route('/showPersonnelApproval')
def showPersonnelApproval():
    return getAllStudents('personnel_approval.html')

@app.route('/personnelApproval', methods=['POST'])
def personnelApproval():
    return json.dumps({'html': '<span>All fields good !!</span>'})

@app.route('/personnelApproval/status', methods=['POST'])
def afterPersonnelApproval():
    _aFStudent = request.form['aStudentFirstName']
    _aLStudent = request.form['aStudentLastName']
    _aUStudent = request.form['aStudentUname']
    _rFStudent = request.form['rStudentFirstName']
    _rLStudent = request.form['rStudentLastName']
    _rUStudent = request.form['rStudentUname']

    username = session['username']

    varr = getPersonnelInfoOnly(username)

    _authF = varr[0][0]
    _authL = varr[0][1]
    _authU = username

    var = "'"
    var += _aUStudent
    var += "'"

    var1 = "'"
    var1 += _rUStudent
    var1 += "'"

    var2 = "'"
    var2 += _authU
    var2 += "'"

    # if there is a student in both approve and deny
    if _aFStudent != "" and _aLStudent != "" and _aUStudent != "" and _rFStudent != "" and _rLStudent != "" and\
            _rUStudent != "":
        print("here")
        if _authF != "" and _authL != "" and _authU != "":
            if getStudentByUsernameOnly(var) == 0 or getStudentByUsernameOnly(var1) == 0:
                return render_template('approval_StudentDNE.html')
            else:
                asID = getStudentID(var)
                rsID = getStudentID(var1)
                # d = datetime.datetime.today().strftime('%m/%d/%Y')
                s = Applicant(asID, "Accepted", _authF, _authL)
                s1 = Applicant(rsID, "Denied", _authF, _authL)
                updateApplicant(s)
                updateApplicant(s1)
                return redirect(url_for('showPersonnelApproval'))
        else:
            return render_template('approval_StudentDNE.html')
            # only approved student
    elif _aFStudent != "" and _aLStudent != "" and _aUStudent != "" and _rFStudent == "" and _rLStudent == "" and\
            _rUStudent == "":
        print("over here")
        if _authF != "" and _authL != "" and _authU != "":
            if getStudentByUsernameOnly(var) == 0:
                return render_template('approval_StudentDNE.html')
            else:
                asID = getStudentID(var)
                #d = datetime.datetime.today().strftime('%m/%d/%Y')
                s = Applicant(asID, "Accepted", _authF, _authL)
                updateApplicant(s)
                return redirect(url_for('showPersonnelApproval'))
        else:
            return render_template('approval_StudentDNE.html')
    elif _aFStudent == "" and _aLStudent == "" and _aUStudent == "" and _rFStudent != "" and _rLStudent != "" and\
            _rUStudent != "":
        print("over over here")
        if _authF != "" and _authL != "" and _authU != "":
            if getStudentByUsernameOnly(var1) == 0:
                return render_template('approval_StudentDNE.html')
            else:
                rsID = getStudentID(var1)
                # d = datetime.datetime.today().strftime('%m/%d/%Y')
                s = Applicant(rsID, "Denied", _authF, _authL)
                updateApplicant(s)
                return redirect(url_for('showPersonnelApproval'))
        else:
            return render_template('approval_StudentDNE.html')
    else:
        print("over over over here")
        return redirect(url_for('showPersonnelApproval'))

# ----- Student Search (Personnel) ------
@app.route('/showStudentSearch', methods=['GET'])
def showStudentSearch():
    return getAllStudents("personnel_searchStudent.html")

@app.route('/studentSearch', methods=['POST', 'GET'])
def studentSearch():
    return json.dumps({'html': '<span>All fields good !!</span>'})

@app.route('/studentSearch/student', methods=['POST', 'GET'])
def afterStudentSearch():
    _studentUsername = request.form['studentUname']

    if _studentUsername == "":
        return getAllStudents("personnel_searchStudent.html")
    else:
        var = "'"
        var += _studentUsername
        var += "'"
        if getStudentByUsernameOnly(var) == 0:
            return render_template('approval_StudentDNE.html')
        else:
            return getEditStudentFromPersonnel('personnel_editStudent.html', _studentUsername)

@app.route('/showSuccessfulEdit', methods=['POST', 'GET'])
def showSuccessfulEdit():
    _fname = request.form['firstName']
    _lname = request.form['lastName']
    _initial = request.form['initial']
    _preferredName = request.form['preferredName']
    _suffix = request.form['suffix']
    _address = request.form['address']
    _city = request.form['city']
    _zip = request.form['zip']
    _state = request.form['state']
    _dob = request.form['dob']
    _gender = request.form['gender']
    _race = request.form['race']
    _email = request.form['email']
    _phoneNumber = request.form['phoneNumber']
    _siblings = request.form['siblings']
    _healthConditions = request.form['healthConditions']
    _disability = request.form['disability']
    _schoolName = request.form['schoolName']
    _schoolDistrict = request.form['schoolDistrict']
    _schoolType = request.form['schoolType']
    _gradeInFall = request.form['gradeInFall']
    _gt = request.form['gt']
    _ell = request.form['ell']
    _gradDate = request.form['gradDate']
    _expHighSchool = request.form['expHighSchool']
    _uname = request.form['uname']
    _mentorID = request.form['mentorID']

    val = "'" + _uname + "'"
    data = getStudentByUsernameOnly(val)
    if len(data[0][3]) > 0 and len(_fname) == 0 :
        _fname = data[0][0]
    if len(data[0][4]) > 0 and len(_lname) == 0:
        _lname = data[0][4]
    if len(data[0][5]) > 0 and len(_initial) == 0:
        _initial = data[0][5]
    if len(data[0][7]) > 0 and len(_preferredName) == 0:
        _preferredName = data[0][7]
    if len(data[0][6]) > 0 and len(_suffix) == 0:
        _suffix = data[0][6]
    if len(data[0][11]) > 0 and len(_address) == 0:
        _address = data[0][11]
    if len(data[0][12]) > 0 and len(_city) == 0:
        _city = data[0][12]
    if len(data[0][14]) > 0 and len(_zip) == 0:
        _zip = data[0][14]
    if len(data[0][13]) > 0 and len(_state) == 0:
        _state = data[0][13]
    if len(data[0][9]) > 0 and len(_gender) == 0:
        _gender = data[0][9]
    if len(data[0][10]) > 0 and len(_race) == 0:
        _race = data[0][10]
    if len(data[0][15]) > 0 and len(_email) == 0:
        _email = data[0][15]
    if len(data[0][16]) > 0 and len(_phoneNumber) == 0:
        _phoneNumber = data[0][16]
    if len(data[0][19]) > 0 and len(_siblings) == 0:
        _siblings = data[0][19]
    if len(data[0][18]) > 0 and len(_healthConditions) == 0:
        _healthConditions = data[0][18]
    if len(data[0][17]) > 0 and len(_disability) == 0:
        _disability = data[0][17]
    if len(data[0][20]) > 0 and len(_schoolName) == 0:
        _schoolName = data[0][20]
    if len(data[0][21]) > 0 and len(_schoolDistrict) == 0:
        _schoolDistrict = data[0][21]
    if len(data[0][22]) > 0 and len(_schoolType) == 0:
        _schoolType = data[0][22]
    if len(data[0][23]) > 0 and len(_gradeInFall) == 0:
        _gradeInFall = data[0][23]
    if len(data[0][26]) > 0 and len(_gt) == 0:
        _gt = data[0][26]
    if len(data[0][27]) > 0 and len(_ell) == 0:
        _ell = data[0][27]
    if len(data[0][25]) > 0 and len(_gradDate) == 0:
        _gradDate = data[0][25]
    if len(data[0][24]) > 0 and len(_expHighSchool) == 0:
        _expHighSchool = data[0][24]

    s = Student1(_fname, _lname, _initial, _suffix, _preferredName, _dob, _gender, _race,
                 _address, _city, _state, _zip, _email, _phoneNumber, _disability, _healthConditions, _siblings,
                 _schoolName, _schoolDistrict, _schoolType, _gradeInFall, _expHighSchool, _gradDate, _gt, _ell, _uname)

    updateEditedStudent(s)

    if _mentorID != "Choose...":
        var = "'" + _uname + "'"
        data = getStudentByUsernameOnly(var)
        print(data[0][0])
        m = Mentor(_mentorID,data[0][0],0)
        insertMentor(m)

    return redirect(url_for('showStudentSearch'))

# ADD CLASS
@app.route('/showAddClass',methods=['POST'])
def showAddClass():
    return getAllInstructors("addClass.html")
    # return render_template("addClass.html")

@app.route('/addClass', methods=['POST'])
def addClass():
    return json.dumps({'html': '<span>All fields good !!</span>'})

@app.route('/addClass/class', methods=['POST'])
def afterAddedClass():

    # CHECK THAT CLASS BEING ADDED IS ONLY OFFERED ONCE IN THAT SESSION MAYBE
    #   MAYBE SHOULD DO THAT IN ENDPOINT: /addClass

    # SHOULD CHECK IF INSTRUCTOR ID EXISTS OR ELSE FAILS OR COULD JUST USE LOGIN

    _className = request.form['className']
    _insID = request.form['instructorID']
    _building = request.form['building']
    _roomno = request.form['roomNo']
    _session = request.form['session']
    _level = request.form['level']
    _cap = request.form['capacity']
    _startTime = request.form['startTime']
    _endTime = request.form['endTime']

    startTime_string = datetime.strptime(_startTime, '%H:%M')
    endTime_string = datetime.strptime(_endTime, '%H:%M')
    if endTime_string < startTime_string:
        return render_template('error_incorrectInput.html')

    timeslot = startTime_string.strftime('%I:%M %p') + "-" + endTime_string.strftime('%I:%M %p')
    # timeslot = _startTime + _endTime

    if checkCourseInSession(_className, _session) > 0:
        return render_template("personnel_ErrorCoursesExist.html")
    elif getCourseByInstructorAndTime(_insID, timeslot, _session) == 0 \
            and getCourseByRoomAndTime(_building, _roomno, timeslot, _session) == 0:
        classid = str(uuid.uuid4())[:6]
        c = Class(str(classid), _className, _insID, _session, _level, timeslot, _building, _roomno, _cap, "0", "0", "0")
        insertClass(c)

        return redirect(url_for('showPersonnelCourses'))
    else:
        return getAllInstructors("error_incorrectInput.html")

# ---- List class (Personnel) ----
@app.route('/showPersonnelCourses', methods=['GET', 'POST'])
def showPersonnelCourses():
    return getAllCourses("listClasses.html")

@app.route('/personnelCourses', methods=['POST', 'GET'])
def personnelCourses():
    return json.dumps({'html': '<span>All fields good !!</span>'})

@app.route('/personnelCourses/courses', methods=['POST', 'GET'])
def afterpersonnelCourses():
    _className = request.form['className']
    _insID = request.form['instructorID']
    _building = request.form['building']
    _roomno = request.form['roomNo']
    _session = request.form['session']
    _level = request.form['level']
    _cap = request.form['capacity']
    _startTime = request.form['startTime']
    _endTime = request.form['endTime']

    timeslot = _startTime + _endTime

    classid = str(uuid.uuid4())[:6]
    c = Class(str(classid), _className, _insID, _session, _level, timeslot, _building, _roomno, _cap, "0", "0", "0")
    insertClass(c)

    # CHANGE TO WHATEVEVER WE DECIDE
    return render_template('afterApplying.html')

# ---- Edit Class (Personnel) ----
@app.route('/showPersonnelEditCourse', methods=['POST', 'GET'])
def showPersonnelEditCourse():
    _courseid = request.form['EditedCourseID']
    print(_courseid)
    val = "'" + _courseid + "'"
    print(val)

    if _courseid == "":
        return redirect(url_for('/personnelEditCourse'))
    else:
        if checkIfCourseExists(_courseid) == 0:
            return render_template("error_courseDNE_PERSONNEL.html") # check this
        else:
            return getEditCourseInfo('editClass.html', _courseid)

@app.route('/personnelEditCourse', methods=['POST', 'GET'])
def personnelEditCourse():

    _className = request.form['className']
    _building = request.form['building']
    _roomno = request.form['roomNo']
    _session = request.form['session']
    _level = request.form['level']
    _cap = request.form['capacity']
    _startTime = request.form['timeSlot']

    cid = getCourseID(_className, _session)

    c = EditCourse(_className, _building, _roomno, _session, _level, _cap, _startTime)

    updateEditClass(c, cid)

    return redirect(url_for('showPersonnelCourses'))

# ---- Personnel Home Page (Edit their profile) ----
@app.route('/personnelHome', methods=['POST', 'GET'])
def personnelHome():
    username = session['username']
    return getPersonnelInfo('personnel_editProfile.html', username)

@app.route('/personnelEditProfile', methods=['POST', 'GET'])
def personnelEditProfile():
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    username = session['username']
    updatePersonnelProfile(firstName, lastName, username)
    return redirect(url_for('personnelHome'))

# ---- Student MyCourses (AKA their home) ----
@app.route('/studentHome', methods=['POST', 'GET'])
def showStudentHome():
    username = session['username']
    return getStudentByUsername("student_editProfile.html", username)
    # return render_template("student_myCourses.html")
    # return getStudentCoursesByUsername("student_myCourses.html")

# ---- Student MyProfile ----
@app.route('/studentProfile', methods=['POST', 'GET'])
def showStudentProfile():
    username = session['username']
    return getStudentByUsername("student_editProfile.html", username)

# ---- Student Edit Profile ----
@app.route('/studentProfile/edit', methods=['POST', 'GET'])
def editStudentProfile():
    username = session['username']

    _fname = request.form['firstName']
    _lname = request.form['lastName']
    _initial = request.form['initial']
    _preferredName = request.form['preferredName']
    _suffix = request.form['suffix']
    _address = request.form['address']
    _city = request.form['city']
    _zip = request.form['zip']
    _state = request.form['state']
    _dob = request.form['dob']
    _gender = request.form['gender']
    _race = request.form['race']
    _email = request.form['email']
    _phoneNumber = request.form['phoneNumber']
    _siblings = request.form['siblings']
    _healthConditions = request.form['healthConditions']
    _disability = request.form['disability']
    _schoolName = request.form['schoolName']
    _schoolDistrict = request.form['schoolDistrict']
    _schoolType = request.form['schoolType']
    _gradeInFall = request.form['gradeInFall']
    _gt = request.form['gt']
    _ell = request.form['ell']
    _gradDate = request.form['gradDate']
    _expHighSchool = request.form['expHighSchool']

    val = "'" + username + "'"
    data = getStudentByUsernameOnly(val)
    if len(data[0][3]) > 0 and len(_fname) == 0:
        _fname = data[0][0]
    if len(data[0][4]) > 0 and len(_lname) == 0:
        _lname = data[0][4]
    if len(data[0][5]) > 0 and len(_initial) == 0:
        _initial = data[0][5]
    if len(data[0][7]) > 0 and len(_preferredName) == 0:
        _preferredName = data[0][7]
    if len(data[0][6]) > 0 and len(_suffix) == 0:
        _suffix = data[0][6]
    if len(data[0][11]) > 0 and len(_address) == 0:
        _address = data[0][11]
    if len(data[0][12]) > 0 and len(_city) == 0:
        _city = data[0][12]
    if len(data[0][14]) > 0 and len(_zip) == 0:
        _zip = data[0][14]
    if len(data[0][13]) > 0 and len(_state) == 0:
        _state = data[0][13]
    if len(data[0][9]) > 0 and len(_gender) == 0:
        _gender = data[0][9]
    if len(data[0][10]) > 0 and len(_race) == 0:
        _race = data[0][10]
    if len(data[0][15]) > 0 and len(_email) == 0:
        _email = data[0][15]
    if len(data[0][16]) > 0 and len(_phoneNumber) == 0:
        _phoneNumber = data[0][16]
    if len(data[0][19]) > 0 and len(_siblings) == 0:
        _siblings = data[0][19]
    if len(data[0][18]) > 0 and len(_healthConditions) == 0:
        _healthConditions = data[0][18]
    if len(data[0][17]) > 0 and len(_disability) == 0:
        _disability = data[0][17]
    if len(data[0][20]) > 0 and len(_schoolName) == 0:
        _schoolName = data[0][20]
    if len(data[0][21]) > 0 and len(_schoolDistrict) == 0:
        _schoolDistrict = data[0][21]
    if len(data[0][22]) > 0 and len(_schoolType) == 0:
        _schoolType = data[0][22]
    if len(data[0][23]) > 0 and len(_gradeInFall) == 0:
        _gradeInFall = data[0][23]
    if len(data[0][26]) > 0 and len(_gt) == 0:
        _gt = data[0][26]
    if len(data[0][27]) > 0 and len(_ell) == 0:
        _ell = data[0][27]
    if len(data[0][25]) > 0 and len(_gradDate) == 0:
        _gradDate = data[0][25]
    if len(data[0][24]) > 0 and len(_expHighSchool) == 0:
        _expHighSchool = data[0][24]

    print("HERE!")
    s = Student2(_fname, _lname, _initial, _suffix, _preferredName, _dob, _gender, _race,
                 _address, _city, _state, _zip, _email, _phoneNumber, _disability, _healthConditions, _siblings,
                 _schoolName, _schoolDistrict, _schoolType, _gradeInFall, _expHighSchool, _gradDate, _gt, _ell)

    studentUpdateProfile(s, username)

    return redirect(url_for('showStudentProfile'))

# ---- Student MyCourses ----
@app.route('/studentMyCourses', methods=['POST', 'GET'])
def studentMyCourses():
    username = session['username']
    print username
    var = "'" + username + "'"
    return getStudentCoursesByUsername("student_myCourses.html", var)

# ---- Student SHOW Add/Drop Course ----
@app.route('/studentAddDropCourse', methods=['POST', 'GET'])
def addDropCourseStudent():
    username = session['username']
    var = "'" + username + "'"
    return getCoursesByGrade("student_addOrDropCourse.html", username)

# ---- Student Add Course ----
@app.route('/studentAddCourse', methods=['POST', 'GET'])
def studentAddCourse():

    _courseid = request.form['classID']

    if checkIfCourseExists(_courseid) == 0:
        return render_template("error_StudentCourseDNE.html")
    else:
        username = session['username']
        var = "'" + username + "'"
        _sid = getStudentID(var)
        print ("here")
        print (_sid)
        val = "'" + _sid[0] + "'"
        print val
        t = Take(_sid[0], _courseid, "0")
        insertTake(t)
        return redirect(url_for('showStudentHome'))

# ---- Student SHOW Add/Drop Course ----
@app.route('/studentDropCourse', methods=['POST', 'GET'])
def studentDropCourse():
    _courseid = request.form['classID']

    if checkIfCourseExists(_courseid) == 0:
        return render_template("error_StudentCourseDNE.html")
    else:
        username = session['username']
        var = "'" + username + "'"
        _sid = getStudentID(var)
        deleteTake(_sid, _courseid)
        return redirect(url_for('showStudentHome'))

# ---- Export Classes ----
@app.route('/exportClasses', methods=['GET', 'POST'])
def exportClasses():
    file = ""
    file += "Course ID,Course Name,Instructor ID,Session,Level,Time Slot,Building,Room Number,Capacity,Course Size, Waitlist Size,Deleted?\n"
    for course in getAllCoursesNoFile():
        c = (str(course[0]), str(course[1]), str(course[2]), str(course[3]), str(course[4]), str(course[5]), str(course[6]), str(course[7]), str(course[8]), str(course[9]), str(course[10]), str(course[11]))
        file += ",".join(c)
        file += "\n"
    return file

if __name__ == "__main__":
    app.run()