from server.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_name', 'user_id', 'user_phone', 'user_email',
            'user_display_name', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, *args, **kwargs):
        user = User(
            user_name=self.validated_data['user_name'],
            user_id=self.validated_data['user_id'],
            user_display_name=self.validated_data['user_display_name'],
            user_email=self.validated_data['user_email'],
            user_phone=self.validated_data['user_phone'],
        )
        password = self.validated_data['password']
        if len(password) < 8:
            raise serializers.ValidationError({
                'user_password': ['password must be of atleast 8 characters']
            })
        user.set_password(password)
        user.save()
        return user