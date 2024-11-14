from django.urls import path 
from .views import  *

urlpatterns = [
 path('enable/', enable_wallet, name='enable_wallet'),
 path('add/', add_money, name='add_money'),
path('remove/', remove_money, name='remove_money'),
path('transactions/',transaction_history, name='transaction_history'),
]