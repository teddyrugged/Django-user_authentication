from rest_framework import serializers
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    #: customizes the TokenObtainPairSerializer to return additional
    #: info (first_name, last_name, id) of the user when logged in
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
    
    confirm_password = serializers.CharField(style = {"input_type": "password"},write_only=True)
    
    class Meta:
        
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
        # 'password':{read_only:True}
        }
        
        def save(self):
            account = Account(
                email=self.validate_email['email'],
            )
            password = self.validate_password['password']
            confirm_password = self.validate_password['confirm_password']
            
            
            if password != confirm_password:
                raise serializers.ValidationError({'password': 'passwords do not match.'})
            account.set_password(password)
            account.save()