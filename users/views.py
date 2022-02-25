from rest_framework import viewsets, serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response

"""create a user serializer that uses the get_user_model() method to get the user model
and has the fields of email and password with the extra kwargs with write only and required"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_student')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create(
            **validated_data
        )  # create a new user with the validated data and return it to the user object
        return user


"""create a viewset that uses the UserSerializer to serialize the user model 
and uses the get_user_model() method to get the user model"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
