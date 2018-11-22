from flask import Flask, render_template, request, json

app = Flask(__name__)

# landing page endpoint
@app.route('/')
def main():
    return render_template('index.html')

# show registration page endpoint
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

# registration endpoint
@app.route('/signUp', methods=['POST'])
def signUp():
    # read in the values (if any) from the UI
    _fname = request.form['firstName']
    _lname = request.form['lastName']
    _initial = request.form['initial']
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
    _schoolName = request.form['schoolName']
    _schoolDistrict = request.form['schoolDistrict']
    _schoolType = request.form['schoolType']
    _gradeInFall = request.form['gradeInFall']
    _gt = request.form['gt']
    _ell = request.form['ell']
    _gradDate = request.form['gradDate']
    _expHighSchool = request.form['expHighSchool']

    #read in Parents 1, info (required)
    _p1fname = request.form['p1FirstName']
    _p1lname = request.form['p1LastName']
    _p1address = request.form['p1Address']
    _p1city = request.form['p1City']
    _p1state = request.form['p1State']
    _p1zip = request.form['p1Zip']
    _p1email = request.form['p1Email']
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
    _p2phonenumber = request.form['p2PhoneNumber']
    _p2workphone = request.form['p2WorkPhone']

    # makes sure the REQUIRED values are entered
    if _fname and _lname and _dob and _p1fname and _p1lname and _p1address and _p1city and _p1state and _p1zip\
            and _p1email and _p1phonenumber and _p1workphone:
        return json.dumps({'html': '<span>All fields good !!</span>'})
    else:
        # if in here means values that are required were not entered
        return json.dumps({'html': '<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()