document.addEventListener("DOMContentLoaded", function() {
  const form = document.querySelector("form");
  const errorMessage = document.getElementById("error-message");

  form.addEventListener("submit", function(event) {
      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;

      if (username.trim() === "" || password.trim() === "") {
          event.preventDefault();
          errorMessage.textContent = "Por favor, preencha todos os campos.";
      }
  });
});
