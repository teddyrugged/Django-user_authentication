from rest_framework import serializers
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': {
                            'first_name': self.user.first_name, 
                            'last_name': self.user.last_name,
                            'id': self.user.id,
                        }
                    })
        return data


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required =True)
    password = serializers.CharField(min_length=6, required=True,write_only=True)
    
    class Meta:  
    
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
        'password':{"write_only":True},
        }
        
    def create(self, validated_data):
        password = self.validated_data.pop('password',None)
        account = self.Meta.model(**validated_data)
        print(password)
        if password is None:
            raise  serializers.ValidationError({'password': 'Enter password.'})
        account.set_password(password)
        print(account.password)
        account.save()
        return account
    
