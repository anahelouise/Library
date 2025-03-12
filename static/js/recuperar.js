document.addEventListener("DOMContentLoaded", function() {
  const form = document.querySelector("form");
  const errorMessage = document.getElementById("error-message");

  form.addEventListener("submit", function(event) {
      const username = document.getElementById("username").value;
      const email = document.getElementById("email").value;

      if (username.trim() === "" || email.trim() === "") {
          event.preventDefault();
          errorMessage.textContent = "Por favor, preencha todos os campos.";
      } else {
          errorMessage.textContent = "";
      }
  });
});
