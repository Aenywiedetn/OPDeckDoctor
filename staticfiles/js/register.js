const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback");
const emailField = document.querySelector("#emailField");
const passwordField = document.querySelector("#passwordField");
const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const passwordFeedBackArea = document.querySelector(".passwordFeedBackArea");
const submitBtn = document.querySelector(".gasnie");
corrusername = false;
corremail = false;
corrpassword = false;

submitBtn.disabled = true;
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

emailField.addEventListener('keyup', (e) => {
  const emailVal = e.target.value;

  emailField.classList.remove("is-invalid");
  emailFeedBackArea.style.display='none';

  if(emailVal.length > 0) {
  fetch("/authentication/validate-email", {
    body: JSON.stringify({ email: emailVal }),
    method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        if(data.email_error){
          corremail = false;
          emailField.classList.add("is-invalid");
          emailFeedBackArea.style.display='block';
          emailFeedBackArea.innerHTML=`<p>${data.email_error})</p>`;

        } else {
          corremail = true;
          if(corremail == true && corrusername == true && corrpassword == true){
            submitBtn.disabled = false;
          }
        }
      });

    }
})
usernameField.addEventListener("keyup", (e) => { 
  const usernameVal = e.target.value;

  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display='none';
  
  if(usernameVal.length > 0) {
  fetch("/authentication/validate-username", {
    body: JSON.stringify({ username: usernameVal }),
    method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        if(data.username_error){
          corrusername = false;
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display='block';
          feedBackArea.innerHTML=`<p>${data.username_error})</p>`;

        } else {
          corrusername = true;
          if(corremail == true && corrusername == true && corrpassword == true){
            submitBtn.disabled = false;
          }
        }
        
      });

    }
  })
passwordField.addEventListener("keyup", (e) => { 
      const passwordVal = e.target.value;
    
      passwordField.classList.remove("is-invalid");
      passwordFeedBackArea.style.display='none';
      
      if(passwordVal.length > 0) {
      fetch("/authentication/validate-password", {
        body: JSON.stringify({ password: passwordVal }),
        method: "POST",
        })
          .then((res) => res.json())
          .then((data) => {
            if(data.password_error){
              corrpassword = false;
              passwordField.classList.add("is-invalid");
              passwordFeedBackArea.style.display='block';
              passwordFeedBackArea.innerHTML=`<p>${data.password_error})</p>`;
    
            } else {
              corrpassword = true;
              if(corremail == true && corrusername == true && corrpassword == true){
                submitBtn.disabled = false;
              }
            }
            
          });
    
        }
  
  
  
  
  
  })
