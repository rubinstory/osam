from django.urls import path

from . import views

urlpatterns = [
	path('', views.List_User.as_view()),
	path('<int:pk>/', views.Detail_User.as_view()),
]