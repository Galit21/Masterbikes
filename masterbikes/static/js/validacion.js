document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('registrationForm');
  if (!form) return;

  form.addEventListener('submit', function(e) {
    const pwd = this.password1.value;
    const regex = /^(?=.*[A-Z])(?=.*\d).{8,}$/;
    if (!regex.test(pwd)) {
      e.preventDefault();
      alert(
        'La contraseña debe tener al menos 8 caracteres, ' +
        'una mayúscula y un número.'
      );
    }
  });
});
