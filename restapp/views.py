from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Profile, SpamNumber, Contact
from .serializers import UserSerializer, SpamNumberSerializer, ContactSerializer
from rest_framework.views import APIView


class UserRegister(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserSerializer

class UserLogin(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number', '')
        print(phone_number)
        password = request.data.get('password', '')

        if phone_number == '' or password == '':
            return Response({'error': 'Please provide both phone number and password.'}, status=status.HTTP_400_BAD_REQUEST)
        user=None
        try:
            user = Profile.objects.get(phone_number=phone_number)
            print(user)
        except Profile.DoesNotExist:
            return Response({'error': 'User with this phone number does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        if user and password == user.password:
            # Authentication successful
            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)


class MarkSpamNumber(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SpamNumber.objects.all()
    serializer_class = SpamNumberSerializer

class SearchByName(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        queryset = Profile.objects.filter(name__icontains=name)
        spam_likelihood_dict = {}

        for user in queryset:
            spam_count = SpamNumber.objects.filter(number=user.phone_number).count()
            spam_likelihood_dict[user.phone_number] = spam_count

        for user in queryset:
            user.spam_likelihood = spam_likelihood_dict.get(user.phone_number, 0)

        return queryset



class SearchByPhoneNumber(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        phone_number = self.request.query_params.get('phone_number', '')
        queryset = Profile.objects.filter(phone_number=phone_number)
        
        spam_likelihood_dict = {}  
        for user in queryset:
            spam_count = SpamNumber.objects.filter(number=user.phone_number).count()
            spam_likelihood_dict[user.phone_number] = spam_count

        for user in queryset:
            user.spam_likelihood = spam_likelihood_dict.get(user.phone_number, 0)

        return queryset


class ContactDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer