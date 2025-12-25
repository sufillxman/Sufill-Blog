from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import *

class loginview(APIView):
    def post(self, request):
        try:
            data = request.data
            username = data.get('username')
            password = data.get('password')

            if not username or not password:
                return Response({
                    'status': 400, 
                    'message': 'Username and Password are required'
                })

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return Response({
                    'status': 200,
                    'message': f'Welcome {user.username}!',
                    'data': {'username': user.username}
                })
            else:
                return Response({
                    'status': 401, 
                    'message': 'Invalid Credentials'
                })

        except Exception as e:
            print(e)
            return Response({
                'status': 500, 
                'message': 'Something went wrong'
            })

# Note: Maine wo 'loginview = loginview.as_view()' wali line hata di hai.

class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Account created successfully',
                    'data': serializer.data
                })
            
            return Response({
                'status': 400,
                'message': 'Validation Error',
                'data': serializer.errors
            })
            
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Something went wrong'
            })