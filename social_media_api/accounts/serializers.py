from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user

User = get_user_model()
class PublicUserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)
    is_following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'bio', 'profile_picture',
                  'followers_count', 'following_count', 'is_following']

    def get_is_following(self, obj):
        request = self.context.get('request')
        if not request or not request.user or not request.user.is_authenticated:
            return False
        return request.user.following.filter(id=obj.id).exists()

class UserSerializer(serializers.ModelSerializer):
    dummy = serializers.CharField(write_only=True,required=False) 
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture','dummy']

