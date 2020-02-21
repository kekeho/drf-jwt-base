from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from .models import User, UserManager


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'display_name', 'email', 'profile', 'password')
    
    def create(self, validation_data):
        return User.objects.create_user(**validation_data)
