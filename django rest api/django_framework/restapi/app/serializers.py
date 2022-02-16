from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    phone_mumber = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateField()

    def create(self,validated_data):
        return Contact.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name')
        instance.phone_mumber = validated_data.get('phone_mumber')
        instance.email = validated_data.get('email')
        instance.date = validated_data.get('date')
        return instance

class ContactModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name','phone_mumber','email','date']
        