from django.urls import path
from .views import Mobile
urlpatterns = [
    path('', Mobile.as_view())
]