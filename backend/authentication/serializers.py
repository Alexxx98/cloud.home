from rest_framework.serializers import ModelSerializer, ValidationError
from .models import User


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        write_only_fields = ['password']
    
    def create(self, validation_data):
        password = validation_data.pop('password')

        # Check if password is safe
        contains_digit = False
        contains_special_character = False

        special_characters = [
            "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
            "[", "]", "{", "}", "\\", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"
        ]
        digits = [str(digit) for digit in range(10)]

        for character in password:
            if character in special_characters:
                contains_special_character = True
            elif character in digits:
                contains_digit = True

        if len(password) < 12:
            raise ValidationError("Password must be at least 12 characters long.")
        if not contains_digit:
            raise ValidationError("Password must contain at least one digit.")
        if not contains_special_character:
            raise ValidationError("Password must contain at least one special character.")
        
        user = User.objects.create(**validation_data)
        user.set_password(password)
        user.save()
        return user
