from django.urls import path
from .views import app, Register

urlpatterns = [
    path('', app.as_view(), name='table'),
    path('register/', Register.as_view(), name='register'),
    path('update/<int:id>', app.as_view(), name='update'),
    path('delete/<int:id>', app.as_view(), name='delete'),
]