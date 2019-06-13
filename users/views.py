from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from rest_framework_jwt.views import JSONWebTokenAPIView
from .serializers import CustomJSONWebTokenSerializer
from django.http import HttpResponse


def activate(request, uidb64, token):
    user_model = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = user_model.objects.get(pk=uid)
        if account_activation_token.check_token(user, token):
            user.email_confirmed = True
            user.save()
            return HttpResponse(render_to_string(
                'info_message.html', 
                {'message': 'You have successfully activated your account. Now you can sign in.'}))
        else:
            return HttpResponse(render_to_string(
                'info_message.html', 
                {'message': 'Your link is invalid!'}))
    except(TypeError, ValueError, OverflowError, user_model.DoesNotExist):
        return HttpResponse(render_to_string(
            'info_message.html', 
            {'message': 'Your link is invalid!'}))


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            current_site = get_current_site(request)
            mail_subject = 'Account activation'
            message = render_to_string('activation_message.html', {
                'username': user.username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            sending_address = user.email
            email = EmailMessage(mail_subject, message, to=[sending_address])
            email.send()
            return HttpResponse(render_to_string(
                'info_message.html',
                {'message': 'Thank you for choosing our company. \
                     Please confirm your email address to complete the registration.'}))
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ObtainCustomJSONWebToken(JSONWebTokenAPIView):
    serializer_class = CustomJSONWebTokenSerializer
