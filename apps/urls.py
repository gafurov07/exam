from django.urls import path

from apps.views import form_view, profile_view, profile_deteil_view, add_profile_view

urlpatterns = [
    path('send-email', form_view, name='send-email'),
    path('profile', profile_view, name='profiles'),
    path('profile/<int:pk>', profile_deteil_view, name='profiles_deteil'),
    path('add-profile/', add_profile_view, name='add_profile')
]
