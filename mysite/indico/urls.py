
from django.urls import path
from indico.views import About, Contact, Index, Service
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('about/',About.as_view(),name='about'),
    path('about/',Service.as_view(),name='about'),
    path('contact/',Contact.as_view(),name='contact'),

]