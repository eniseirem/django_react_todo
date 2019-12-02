from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('list', views.UserList)

urlpatterns = [
    path('users/create', views.UserCreate.as_view(), name='account-create'),
    # path('users/', include(router.urls)),

]