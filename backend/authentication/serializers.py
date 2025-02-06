from rest_framework.serializers import ModelSerializer
from .models import User


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        write_only_fields = ['password']
    
    def create(self, validation_data):
        password = validation_data.pop('password')
        user = User.objects.create(**validation_data)
        user.set_password(password)
        user.save()
        return user
    

