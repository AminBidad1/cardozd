from django.contrib import admin
from django.urls import (
    path,
    include,
)
from rest_framework import routers
from backend.srvs.camp.camp.views import PostViewSet

camp_router = routers.DefaultRouter()
camp_router.register(r"posts", PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("camp/", include(camp_router.urls)),
]
