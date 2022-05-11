from django.contrib.auth.models import User
from .models import CrudData
from rest_framework import serializers


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudData
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password2')
        if pass1 != pass2:
            raise serializers.ValidationError('Passoword Not match')
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
