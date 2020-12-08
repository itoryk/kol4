from django.urls import path

from applications.blog import views

urlpatterns = [
    path("", views.AllPostsView.as_view()),
]
