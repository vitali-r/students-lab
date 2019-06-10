from rest_framework import serializers
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8,
        max_length=50,
        style={'input_type': 'password'},
        write_only=True)
    password2 = serializers.CharField(
        min_length=8,
        max_length=50,
        style={'input_type': 'password'},
        write_only=True)

    class Meta:
        model = UserModel
        fields = ('username', 'password', 'password2', 'email')

    def create(self, validated_data):
        user_object = UserModel(
            username=validated_data.get('username'),
            email=validated_data.get('email'))
        user_object.set_password(validated_data.get('password'))
        user_object.save()
        return user_object
