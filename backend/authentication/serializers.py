from rest_framework.serializers import ModelSerializer
from .models import User


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validation_data):
        user = User.objects.create()
        return user
    

