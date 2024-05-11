from rest_framework import serializers
from .models import Profile, SpamNumber, Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number']
        
class UserSerializer(serializers.ModelSerializer):
    spam_likelihood = serializers.SerializerMethodField()
    password = serializers.CharField(max_length=128, write_only=True)
    contacts = ContactSerializer(many=True, read_only=True)

    def get_spam_likelihood(self, obj):
        spam_count = SpamNumber.objects.filter(number=obj.phone_number).count()
        return spam_count

    class Meta:
        model = Profile
        fields = ['id', 'name', 'phone_number', 'email', 'password','contacts', 'spam_likelihood']
        extra_kwargs = {
            'name': {'required': True},
            'phone_number': {'required': True},  
            'password': {'required': True},  
        }




class SpamNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamNumber
        fields = ['id', 'number']
