from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name= 'queue_management'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='queue'),
    path('update-queue/',views.CheckOutNumberView.as_view() , name='update-queue'),
    path('free-queue/',views.FreeCheckOutView.as_view() , name='free-queue'),
]
