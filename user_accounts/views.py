from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, ChangePasswordSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import update_session_auth_hash
from .models import CustomUser
from rest_framework.authentication import TokenAuthentication
from django.core.mail import send_mail
from rest_framework.views import APIView


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    Register a new user.

    Endpoint: /register_user
    Method: POST
    Permissions: AllowAny

    Parameters:
    - request.data: User data to be serialized and saved.

    Returns:
    - Response: Serialized user data if registration is successful, or errors if registration fails.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def check_token(request):
    """
    Check the validity of a token.

    Endpoint: /check_token
    Method: GET
    Permissions: AllowAny

    Returns:
    - Response: "ok" if the token is valid, or "token invalid" if the token is invalid.
    """
    print("checking token...")
    try:
        return Response("ok", status=status.HTTP_200_OK)
    except Exception as e:
        return Response("token invalid", e, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def get_user_from_token(request):
    """
    Get user information from a token.

    Endpoint: /get_user_from_token
    Method: GET
    Permissions: AllowAny

    Returns:
    - Response: Serialized user data if the token is valid, or "token invalid" if the token is invalid.
    """
    print("getting user from token...")
    try:
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header:
            # Split the header to extract the token part
            auth_token = auth_header.split(' ')[1]
            token = Token.objects.get(key=auth_token)
            print(token.user)
            user = CustomUser.objects.get(id=token.user_id)
            serialized_user = UserSerializer(user)
            print(serialized_user.data)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response("token invalid", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    """
    Change the password of the authenticated user.

    Endpoint: /change_password
    Method: POST
    Permissions: IsAuthenticated

    Parameters:
    - request.data: Contains the old password and the new password.

    Returns:
    - Response: Success message if the password is changed successfully, or error message if the old password is incorrect.
    """
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def guide_list(request):
    """
    Get a list of guides.

    Endpoint: /guide_list
    Method: GET
    Permissions: AllowAny

    Returns:
    - Response: Serialized data of all guides.
    """
    guides = CustomUser.objects.filter(is_guide=True)
    serializer = UserSerializer(guides, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def serve_guide_detail(request, pk):
    """
    Get, update, or delete a specific guide.

    Endpoint: /serve_guide_detail/<pk>
    Method: GET, PUT, DELETE
    Permissions: AllowAny

    Parameters:
    - pk: Primary key of the guide.

    Returns:
    - Response: Serialized data of the guide if found (GET), updated serialized data if update is successful (PUT),
      or status code 204 if deletion is successful (DELETE).
    """
    print(request.data)
    try:
        guide = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(guide)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(guide, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        guide.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)