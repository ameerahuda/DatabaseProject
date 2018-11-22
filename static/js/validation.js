// this line executes when a page finishes loading
$(document).ready(function () {
console.log("here"); // for testing purposes

// this validates the form (registration form where student, parent info is)
// the form is: <form id="regist"> in the signup.html
// so have to use regist so the function can know what to validate
// the rules section:
//  - the name (firstName, dob, address, etc) is found in signup.html
//      - usually in the <input name="NAME">
//  - so you get that name and add whatever requirments or validations you want to it
//      - can search up "jquery validation rules" on google to see which rules are out there

$('#regist').validate({
    rules: {
        firstName: {
            minlength: 2,
            required: true,
            lettersonly: true
        },
        lastName: {
            required: true,
            minlength: 2
        },
        initial: {
            maxlength: 1
        },
        suffix: {
            lettersonly: true
        },
        dob: {
            dateISO: true,
            required: true
        },
        address: {
            minlength: 2,
        },
        city: {
            minlength: 2,
            lettersonly: true
        },
        zip: {
            digits: true
        },
        siblings: {
            lettersonly: true
        },
        phoneNumber: {
            phoneUS: true
        },
        healthConditions: {
            lettersonly: true
        },
        schoolName: {
            minlength: 2,
            lettersonly: true
        },
        schoolDistrict: {
            minlength: 2,
            lettersonly: true
        },
        gradDate: {
            maxlength: 4,
            minlength: 4,
            digits: true
        },
        expHighSchool: {
            lettersonly: true
        },
        p1FirstName: {
            lettersonly: true,
            required: true
        },
        p1LastName: {
            required: true,
            lettersonly: true
        },
        p1Address: {
            minlength: 2,
            required: true,
        },
        p1City: {
            required: true,
            lettersonly: true
        },
        p1State: {
            required: true
        },
        p1Zip: {
            digits: true,
            required: true
        },
        p1Email: {
            email: true,
            required: true
        },
        p1PhoneNumber: {
            phoneUS: true,
            required: true
        },
        p1WorkPhone: {
            phoneUS: true,
            required: true
        },
        p2FirstName: {
            lettersonly: true
        },
        p2LastName: {
            lettersonly: true
        },
        p2Address: {
            minlength: 2
        },
        p2City: {
            lettersonly: true
        },
        p2Zip: {
            digits: true
        },
        p2Email: {
            email: true
        },
        p2PhoneNumber: {
            phoneUS: true
        },
        p2WorkPhone: {
            phoneUS: true
        }
    }
});
console.log("This is working so far~");
});