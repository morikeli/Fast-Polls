from django.urls import path
from polls import views

urlpatterns = [
    path('recent-polls', views.homepage_view, name='homepage'),
    path('polls-login-page/set-polls/', views.UserLogin.as_view(), name='login'),
    path('polls/create-account/', views.signup_view, name='signup'),
    path('set-polls/post-question/', views.set_questions_view, name='add_quiz'),
    path('edit-question/<str:pk>/change-question/', views.edit_questions_view, name='edit_question'),
    path('edit-choice/<str:pk>/change/', views.edit_choices_view, name='edit_choice'),
    path('delete-question/<str:pk>/', views.delete_view, name='delete'),
    path('submit-vote/<str:pk>/', views.vote_view, name='vote'),
    path('results/<str:pk>/polls-results-and-stats/', views.poll_results_view, name='results'),
    
        
    path('logout/', views.LogoutUser.as_view(), name='logout'),    
]