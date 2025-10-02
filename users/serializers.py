from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "email", "favorite_team", "favorite_city"]
        extra_kwargs = {
            "password": {"write_only": True},
            "favorite_team": {"required": False, "allow_null": True, "allow_blank": True},
            "favorite_city": {"required": False, "allow_null": True, "allow_blank": True},
        }

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)