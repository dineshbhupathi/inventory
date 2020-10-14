from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','email','password']

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """

        validated_data['password'] = make_password(validated_data['password'])
        print(validated_data,'kldsjflk')
        return super(UserSerializer, self).create(validated_data)

class BorrowBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowBook
        fields = serializers.ALL_FIELDS

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = serializers.ALL_FIELDS