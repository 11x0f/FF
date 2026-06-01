from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "alias", "password", "confirm_password")
        extra_kwargs ={ 'password':{'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("alias", "email", "phone", "avatar", "bio")

class PublicUserSerializer(serializers.ModelSerializer):

    follower_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ("alias", "avatar", "bio" ,"follower_count")

    def get_follower_count(self, obj):
        return obj.follower_set.count()