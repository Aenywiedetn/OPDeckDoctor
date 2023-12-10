const handleToggleInput = () => {
    const passwordField = document.getElementById('passwordField');
    const confirmPasswordField = document.getElementById('confirmPasswordField');
    const showPasswordToggle = document.querySelector('.showPasswordToggle');

    if (showPasswordToggle.textContent === 'show') {
        showPasswordToggle.textContent = 'hide';
        passwordField.setAttribute('type', 'text');
        confirmPasswordField.setAttribute('type', 'text');

    } else {
        showPasswordToggle.textContent = 'show';
        passwordField.setAttribute('type', 'password');
        confirmPasswordField.setAttribute('type', 'password');
    }
};

const showPasswordToggle = document.querySelector('.showPasswordToggle');
showPasswordToggle.addEventListener('click', handleToggleInput);