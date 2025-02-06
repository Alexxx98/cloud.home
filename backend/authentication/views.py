from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializer

# Create your views here.

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User successfully registered!"})
        return Response(serializer.errors)
