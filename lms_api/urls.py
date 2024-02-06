from django.urls import path

from .views import PersonGenerics, PersonList

app_name = 'lms_api'

urlpatterns = [
    path('persons/<int:pk>', PersonGenerics.as_view()),
    path('persons/', PersonList.as_view()),
]
