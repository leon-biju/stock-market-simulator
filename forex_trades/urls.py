from django.urls import path
from .views import view_forex_rates

urlpatterns = [
    path('forex_trades/', view_forex_rates, name='view_forex_rates'),
]