from django.urls import include, path

from integration import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('initiate-payment/', views.initiate, name="initiate-payment"),
    path('response/', views.response, name="response")
]