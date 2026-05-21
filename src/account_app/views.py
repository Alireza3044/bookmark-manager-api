from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from account_app import serializers


class RegisterView(CreateAPIView):
    serializer_class = serializers.RegisterSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = Token.objects.get(user=user)
        data = {
            "response": "Registration was successful!",
            "name": user.name,
            "email": user.email,
            "token": token.key
        }
        headers = self.get_success_headers(data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class LogoutView(CreateAPIView):
    def create(self, request):
        self.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
