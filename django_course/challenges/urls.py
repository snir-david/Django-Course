from django.urls import path
from . import views

urlpatterns  = [
    path("", views.index),
    path("<int:month>", views.month_handler_int),
    path("<str:month>", views.month_handler_str, name='monthly_handle_str')
]
