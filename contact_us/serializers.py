from rest_framework import serializers
from .models import Contact_us


class Contact_usSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact_us
        fields = '__all__'
       