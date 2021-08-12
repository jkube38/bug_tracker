"""bugtracker_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from bugtracker_app import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('getthembugs/', views.home_view, name='home'),
    path('createticket/', views.create_ticket_view, name='create_ticket'),
    path('logout/', views.logout_view, name='logout'),
    path('ticket/<str:title>/', views.ticket_view, name='ticket'),
    path('edit/<str:title>/', views.edit_view, name='edit'),
    path('assignedto/<str:title>/', views.assigned_view, name='assigned'),
    path('invalid/<str:title>/', views.invalid_view, name='invalid'),
    path('done/<str:title>/', views.done_view, name='done'),
    path('returnticket/<str:title>/', views.return_view, name='return'),
    path('user/<str:username>/', views.user_view, name='user'),
    path('admin/', admin.site.urls)
]
