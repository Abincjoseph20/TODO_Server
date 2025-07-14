from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . views import TodoViewset

router = DefaultRouter()
router.register(r'todos',TodoViewset)
#path specified.
urlpatterns = [
    path('',include(router.urls))
]
