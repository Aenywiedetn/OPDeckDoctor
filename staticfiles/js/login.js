const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback");
const emailField = document.querySelector("#emailField");
const passwordField = document.querySelector("#passwordField");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const passwordFeedBackArea = document.querySelector(".passwordFeedBackArea");


const handleToggleInput=(e)=>{

if(showPasswordToggle.textContent==="show"){
  showPasswordToggle.textContent = "hide"

  passwordField.setAttribute("type", "text");

} else {
  showPasswordToggle.textContent = "show";
  passwordField.setAttribute("type", "password");
}
}

showPasswordToggle.addEventListener('click', handleToggleInput);
