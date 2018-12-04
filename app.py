from flask import Flask, render_template, request, json, redirect, url_for, session
from Endpoints import *
from Classes.Objects import *
from DBandTables import *
from MySQLFunctions.insertSQL import *
import uuid
from datetime import datetime
from MySQLFunctions.getSQL import *
import random

app = Flask(__name__)

# landing page endpoint
@app.route('/', methods = ['GET'])
def main():
    return getStudentByUsername("personnel_editStudent.html", "'ameera0115'")
    #return render_template('index.html')

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
        _dob = datetime.strptime("00/00/0000", '%m/%d/%Y')
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
@app.route('/showSignIn')
def showSignIn():
    return render_template("signIn.html")

@app.route('/signIn', methods=['POST'])
def signIn():
    return json.dumps({'html': '<span>All fields good !!</span>'})

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
    insertInstructor(admin)

    # CHANGE TO WHATEVEVER WE DECIDE
    return render_template('afterApplying.html')

if __name__ == "__main__":
    app.run()