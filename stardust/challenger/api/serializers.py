from rest_framework import serializers
from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if not data['username'].isalnum():
            raise serializers.ValidationError({'username': 'Only alphanumeric character allowed in username.'})
        return data

    def save(self):
        user = Account.objects.create_user(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match!'})

        user.set_password(password)
        user.save()

        return user
