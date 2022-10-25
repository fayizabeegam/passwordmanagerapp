from rest_framework import serializers
from django.contrib.auth.models import User
from passwordapi.models import Quicker


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=[
            "username",
            "email",
            "password",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class QuickerSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)


    class Meta:
        model=Quicker
        fields=[
            "user",
            "org_name",
            "org_password",

        ]

    def create(self, validated_data):
        user=self.context.get("user")
        return Quicker.objects.create(user=user,**validated_data)