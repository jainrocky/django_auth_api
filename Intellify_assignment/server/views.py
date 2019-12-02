from rest_framework.views import APIView
from rest_framework.response import Response
from server.models import User
from .serializers import UserSerializer
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

class Login(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, format=None):
        # print('Console.Log', request.GET)
        username = request.GET.get('user_name', "")
        password = request.GET.get('password', "")
        response = {}
        if username and password:
            try:
                user = authenticate(username=username, password=password)
                if user:
                    response['success'] = 'login successfully'
                    response['user_display_name']=user.user_display_name
                    response['user_email']=user.user_email
                    response['user_phone']=user.user_phone
                    response['token']=Token.objects.get(user=user).key
                    return Response(response, HTTP_200_OK)
                else:
                    response['error'] = 'authentication failed'
                    return Response(response, HTTP_400_BAD_REQUEST)
            except:
                response['error'] = 'authentication failed'
                return Response(response, HTTP_400_BAD_REQUEST)
        else:
            response['error'] = []
            if not username:
                response['error'].append('user_name is required')
            if not password:
                response['error'].append('password is required')
            return Response(response, status=HTTP_400_BAD_REQUEST)


class Register(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        response = {}
        if serializer.is_valid():
            user = serializer.save()
            response['success'] = 'successfully registered new user'
            return Response(response, status=HTTP_200_OK)
        else:
            response = serializer.errors
            return Response(response, status=HTTP_400_BAD_REQUEST)

