from django.core.exceptions import ValidationError
import re

class UppercaseValidator:
    def validate(self, password, user=None):
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                "La contraseña debe contener al menos una letra mayúscula.",
                code='password_no_upper',
            )
    def get_help_text(self):
        return "Tu contraseña debe contener al menos una letra mayúscula."
