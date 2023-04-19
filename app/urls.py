from django.urls import path
from . views import home,delete,update
urlpatterns = [
    path("", home , name='home'),
    path('delete/<int:st_id>/', delete, name='delete'),
    path('update/<int:st_id>', update, name='update')
]
