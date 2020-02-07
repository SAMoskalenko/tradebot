from rest_framework import serializers

from .models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserAccount
        fields = '__all__'
