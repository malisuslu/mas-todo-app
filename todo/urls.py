from django.urls import path
from .views import app

urlpatterns = [
    path('', app.as_view(), name='table'),
    path('update/<int:id>', app.as_view(), name='update'),
    path('delete/<int:id>', app.as_view(), name='delete'),
]