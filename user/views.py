import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            return  JsonResponse({
                'status': 'error',
                'message': "Invalid credentials"
            })
        
        refresh = RefreshToken.for_user(user)

        return JsonResponse({
            'status': 'Success',
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'user': {
                'id': user.id,
                'username': user.username
            }
        })