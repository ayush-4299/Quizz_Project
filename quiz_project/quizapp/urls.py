from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('quiz/<int:subject_id>/', views.start_quiz, name='start_quiz'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]