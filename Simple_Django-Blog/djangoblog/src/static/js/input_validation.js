var email1 = document.getElementById("mailbox1"),
    email2 = document.getElementById("mailbox2"),
    password1 = document.getElementById("password1"),
    password2 = document.getElementById("password2");

function validatePassword(){
  if(password1.value != password2.value) {
    password2.setCustomValidity("Passwords Don't Match");
  } else {
    password2.setCustomValidity('');
  }
}

function validateEmail(){
  if(email1.value != email2.value) {
    email2.setCustomValidity("Email Don't Match");
  } else {
    email2.setCustomValidity('');
  }
}
password1.onchange = validatePassword;
password2.onkeyup = validatePassword;

email1.onchange = validateEmail;
email2.onkeyup = validateEmail;