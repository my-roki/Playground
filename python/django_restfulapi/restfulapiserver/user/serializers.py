from rest_framework import serializers
from .models import User

# Keep our code a bit more concise.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "password",
            "email",
            "phone_number",
            "group",
            "is_active",
            "created_at",
            "updated_at",
        ]
