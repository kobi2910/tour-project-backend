
from rest_framework import generics, status
from django.core.mail import send_mail
from .serializers import Contact_usSerializer
from .models import Contact_us
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class MsgCreateView(generics.CreateAPIView):
    """
    A view for creating a new contact message.

    This view allows users to send a contact message by providing their name, email, subject, and message.
    Upon receiving the message, an email is sent to the specified email address.

    Methods:
    - post: Create a new contact message and send an email.

    Attributes:
    - queryset: A queryset of all Contact_us objects.
    - serializer_class: The serializer class for serializing and deserializing Contact_us objects.
    - permission_classes: The permission classes for the view.

    """

    queryset = Contact_us.objects.all()
    serializer_class = Contact_usSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Create a new contact message and send an email.

        This method creates a new contact message using the provided data in the request.
        It validates the data, performs the creation, and sends an email to the specified email address.

        Args:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - A Response object with the serialized data of the created contact message and the HTTP status code.

        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        name = request.data.get('name')
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')

        # Construct the message
        full_message = f"Message from {name} ({email}):\n\n{message}"

        # Send the email
        send_mail(subject, full_message, None, ['ktravelservis@gmail.com'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
