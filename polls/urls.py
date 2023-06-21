from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('new-poll/', views.CreatePollsView.as_view(), name='create-polls'),
    path('choices/<str:pk>/create-choices/', views.CreateNewChoicesView.as_view(), name='create-choices'),
    path('voting/<str:pk>/polls/', views.VotingView.as_view(), name='vote'),
    path('<str:pk>/edit/', views.EditPollsView.as_view(), name='edit-polls'),
    path('choices/<str:pk>/edit/', views.EditChoicesView.as_view(), name='edit-choices'),

]