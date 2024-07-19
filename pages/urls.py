from django.urls import path

from info.views import AboutListView
from offers.views import ServicesListView
from pages.views import HomeTemplateView, ContactCreateView

app_name = 'pages'

urlpatterns = [
    path('services/', ServicesListView.as_view(), name='services'),
    path('about/', AboutListView.as_view(), name='about'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('', HomeTemplateView.as_view(), name='home'),
]
