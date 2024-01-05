from django.urls import path
from .views import place_bet, results

urlpatterns = [
    # path('', index, name='index'),
    path('', place_bet, name='place_bet'),
    path('results/<str:result>/<path:winnings>/', results, name='results'),
]
