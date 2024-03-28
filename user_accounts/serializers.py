from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for the User model.

    This serializer is used to convert User model instances to JSON and vice versa.
    It specifies the fields to be included in the serialized representation of the User model.
    It also provides validation for the input data during deserialization.

    Attributes:
        model (CustomUser): The User model class to be serialized.
        fields (list): The fields to be included in the serialized representation of the User model.
        extra_kwargs (dict): Additional keyword arguments for the fields.

    Methods:
        create(validated_data): Creates a new User instance based on the validated data.

    """

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create and save a new User instance.

        Args:
            validated_data (dict): The validated data for creating the User instance.

        Returns:
            CustomUser: The newly created User instance.

        """
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer class for changing user password.

    This serializer is used to validate the input data for changing user password.

    Attributes:
        old_password (str): The old password of the user.
        new_password (str): The new password to be set for the user.

    """

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordEmailSerializer(serializers.Serializer):
    """
    Serializer class for resetting user password via email.

    This serializer is used to validate the input data for resetting user password via email.

    Attributes:
        email (str): The email address of the user.

    """

    email = serializers.EmailField(required=True)