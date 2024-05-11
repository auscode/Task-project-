from django.urls import path
from .views import UserRegister,UserLogin, MarkSpamNumber, SearchByName, SearchByPhoneNumber, ContactDetail


urlpatterns = [
    path('register/', UserRegister.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('mark-spam/', MarkSpamNumber.as_view(), name='mark-spam'),
    path('search-by-name/', SearchByName.as_view(), name='search-by-name'),
    path('search-by-phone/', SearchByPhoneNumber.as_view(), name='search-by-phone'),
    path('contact/<int:pk>/', ContactDetail.as_view(), name='contact-detail'),
]
