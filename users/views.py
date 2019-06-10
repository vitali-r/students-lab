from django.shortcuts import render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text


def activate(request, uidb64, token):
    user_model = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = user_model.objects.get(pk=uid)
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse(render_to_string('after_confirmation.html'))
        else:
            return HttpResponse(render_to_string('failed_activation.html'))
    except(TypeError, ValueError, OverflowError, user_model.DoesNotExist):
        return HttpResponse(render_to_string('failed_activation.html'))
    

class RegistrationView(APIView):
    user_model = get_user_model()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        data = UserSerializer(data=request.data)
        if data.is_valid():
            user = data.save()
            current_site = get_current_site(request)
            mail_subject = 'Account activation'
            message = render_to_string('activation_message.html', {
                'username': user.username,
                'domaim': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),               
            })
            sending_address = user.email
            email = EmailMessage(mail_subject, message, to=[sending_address])
            email.send()
            return HttpResponse(render_to_string('after_registration.html'))
        return Response(status=status.HTTP_400_BAD_REQUEST)