from django.contrib.auth import authenticate
from rest_framework import serializers
from drf_compound_fields.fields import ListField
#from apps.user_info.serialization import *
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    """Serilaizers registration requests and create a new user"""

    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )

    token = serializers.CharField(max_length = 255 , read_only = True)

    class Meta:
        model = User
        fields = ('id','username','email','firstname','lastname','password','token')

        read_only = ('id',)
    def create(self , validated_data):
        return User.objects.create_user(**validated_data)





class LoginSerilaizer(serializers.Serializer):

    email = serializers.CharField(max_length = 255)

    username = serializers.CharField(max_length=255, read_only = True)

    password = serializers.CharField(max_length = 128  , write_only = True)

    token = serializers.CharField(max_length = 255 , read_only = True)

    id = serializers.CharField(max_length = 255, read_only = True)
    #firstname = serializers.CharField(max_length = 75, read_only = True)

    lastname = serializers.CharField(max_length = 100 , read_only = True)

    def validate(self , data):

        email = data.get('email',None)

        password = data.get('password',None)

        if email is None:
            raise serializers.ValidationError(
                "An email address is required to log in"
            )

        if password is None:
            raise serializers.ValidationError(
                "A password is required"
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                "A user with this email and password does not exist"
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "The user has been deactivated"
            )
        return {
            "id" : user.id,
            "email" : user.email,
            "username" : user.username,
            "token": user.token

        }


class UserSerializer(serializers.ModelSerializer):


    """Handles Serilialization and deserialization of users"""

    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )

    class Meta:
        model = User
        fields = ('password','username','firstname','mi','lastname','email','token',)

        read_only_fields = ('token')


    def update(self,instance, validated_data):
        """perform a user update"""

        print(validated_data)

        password = validated_data.pop('password',None)

        for (key,value) in validated_data.items():
            setattr(instance ,key , value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

class CompleteUserSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = User
        fields = ('id','username','firstname','lastname','token')
        read_only_fields =('id','token',)

class UserProfileProperties_Profile_Page_Serilaizer(serializers.ModelSerializer):

    id  = serializers.IntegerField() 
    class Meta:
        model = User
        fields = ('id','token','firstname','lastname')
        read_only_fields = ('token','id')
        validators = [] 
    
    
    def create(self ,validated_data):
        user_id = validated_data.get('id')
        curr_user = User.objects.get(pk = user_id)
        
        return curr_user

    
    def update(self, instance ,validated_data):
        #preliminaries
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname',instance.lastname)
        instance.save()

       ############################################################ 
        return instance



