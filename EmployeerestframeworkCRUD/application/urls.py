from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter() # api working
router.register('employess',EmployeeViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    

]