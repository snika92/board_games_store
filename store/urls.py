from django.urls import path
from store.views import home, contacts
from store.apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
