//Change Surname
function changeSurName() {
    var changeSur = document.getElementById('changeSurname').value;
    document.getElementById('surName').innerHTML = changeSur;

    window.open('Surname Changed!!')
}

//Change First
function changeFirstName() {
    var changeFirst = document.getElementById('changeFirstname').value;
    document.getElementById('firstName').innerHTML = changeFirst;
}

//Change Other Name
function changeOtherName() {
    var changeOther = document.getElementById('changeOthername').value;
    document.getElementById('otherName').innerHTML = changeOther;
}

//Change Date of Birth
function changeDob() {
    var changeDOB = document.getElementById('changeDob').value;
    document.getElementById('dob').innerHTML = changeDOB;
}

//Change Gender
function changeGender() {
    var changeGen = document.getElementById('changeGender').value;
    document.getElementById('gender').innerHTML = changeGen;
}
