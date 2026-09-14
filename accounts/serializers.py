from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": False}
        }

    def validate_email(self, value):
        if not value:
            return value

        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("An account already exists with this email.")
        return value

    def validate_password(self, value):
        user = User(username=self.initial_data.get("username", ""),
                email=self.initial_data.get("email", ""))
        validate_password(value, user=user)
        return value

    def validate(self, data):
        if data.get("password") != data.get("password2"):
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop("password2", None)
        user = User.objects.create_user(**validated_data)
        Token.objects.get_or_create(user=user)
        return user
