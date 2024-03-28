from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trip
        fields = '__all__'



    def create(self, validated_data):
        
        if 'guide' not in validated_data or not validated_data['guide']:
            validated_data['guide'] = self.context['request'].user

        return super(TripSerializer, self).create(validated_data)
    
    