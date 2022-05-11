from rest_framework.pagination import PageNumberPagination
from .models import CrudData
from rest_framework import generics
from .serializers import DataSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import logout,authenticate,login
import json
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class Logout(generics.GenericAPIView):
    def post(self,request):
        print(request.data)
        refresh_token = request.data
        token = RefreshToken(refresh_token)
        token.blacklist()
        logout(request)
        return Response({"message":"Logout"})

class LoginData(generics.GenericAPIView):
    def post(self,request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if username is None or password is None:
            return Response({"error":"invalid"})
        user = authenticate(username=username,password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            login(request,user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error":"invalid"})



class UserData(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        password = serializer.validated_data['password']
        serializer.save()
    

class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
class CreateListData(generics.CreateAPIView):
    queryset = CrudData.objects.all()
    serializer_class = DataSerializer
    pagination_class = MyPageNumberPagination
    def perform_create(self, serializer):
        name = serializer.validated_data['name']
        age = serializer.validated_data['age']
        print(age)
        serializer.save()
class UpdateData(generics.UpdateAPIView):
    queryset = CrudData.objects.all()
    serializer_class = DataSerializer
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        result ={"detail":'save'}
        return Response(result)

    def perform_update(self, serializer):
        serializer.save()

class DestroyData(generics.DestroyAPIView):
    queryset = CrudData.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class UserList(generics.ListAPIView):
    queryset = CrudData.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



