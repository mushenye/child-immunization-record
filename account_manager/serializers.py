
from rest_framework import serializers

from .models import User







class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =[ 'id','username', 'email','password', ]
        extra_kwargs = {'password': {'write_only': True}}

    
    # def validate(self, attrs):
    #     password=attrs.get['password']
    #     if len(password) < 8:
    #         return serializers.ValidationError(" Password too short")
    #     return super().validate(attrs)
    
