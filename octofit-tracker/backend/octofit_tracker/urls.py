"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import os
from django.http import JsonResponse
from .views import TeamViewSet, UserViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from django.http import HttpResponse
def homepage(request):
    return HttpResponse('<h1>Welcome to Octofit Tracker API</h1><p>Visit <a href="/api/">/api/</a> for REST endpoints.</p>')


# Helper to get codespace URL
def get_codespace_url():
    codespace_name = os.environ.get('CODESPACE_NAME', None)
    if codespace_name:
        return f"https://{codespace_name}-8000.app.github.dev"
    return "http://localhost:8000"


# Custom API root view to show endpoint URLs with correct base
def custom_api_root(request):
    base_url = get_codespace_url()
    endpoints = {
        "teams": f"{base_url}/api/teams/",
        "users": f"{base_url}/api/users/",
        "activities": f"{base_url}/api/activities/",
        "workouts": f"{base_url}/api/workouts/",
        "leaderboard": f"{base_url}/api/leaderboard/",
    }
    return JsonResponse(endpoints)


router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
