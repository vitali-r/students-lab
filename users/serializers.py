from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from django.utils.translation import ugettext as _


UserModel = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CustomJSONWebTokenSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }
        if all(credentials.values()):
            user = authenticate(**credentials)
            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
                if not user.email_confirmed:
                    msg = _('Email is not verified.')
                    raise serializers.ValidationError(msg)
                payload = jwt_payload_handler(user)
                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


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
        fields = ('email', 'password', 'password2', 'username')

    def create(self, validated_data):
        user_object = UserModel(
            username=validated_data['username'],
            email=validated_data['email'])
        user_object.set_password(validated_data['password'])
        user_object.save()
        return user_object


class ChangeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = (
            'email',
            'email_confirmed',
            'groups',
            'user_permissions',
            'is_staff',
            'is_active',
            'is_superuser',
            'password')
