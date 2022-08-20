from rest_framework import serializers
from account.models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(style = {"input_type": "password"},write_only=True)
    
    class Meta:
        
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
        'password':{write_only:True}
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