from rest_framework import serializers

from .models import UserData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = [
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "date_joined",
        ]

    def create(self, validated_data):
        user = UserData.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
