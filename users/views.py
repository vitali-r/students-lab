from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ChangeProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from rest_framework_jwt.views import JSONWebTokenAPIView
from .serializers import CustomJSONWebTokenSerializer
from django.http import HttpResponse
from django.shortcuts import render


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


def users_detail(request, user_id):
    user = get_user_model().objects.get(pk=user_id)
    change_permission = False
    if request.user.email == user.email or request.user.is_staff:
        change_permission = True
    return render(request, 'user_page.html', {
        'user': user,
        'address': user.get_address(),
        'name': user.get_full_name(),
        'change_permission': change_permission})


class UpdateProfileView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangeProfileSerializer

    def get_queryset(self):
        user = get_user_model()
        user_id = self.kwargs.get('user_id')
        requested_user = user.objects.get(pk=user_id)
        if self.request.user.email == requested_user.email or self.request.user.is_staff:
            queryset = user.objects.filter(id=user_id)
            return queryset
        return HttpResponse(render_to_string(
            'info_message.html',
            {'message': 'Changes are successfully saved.'}))


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
