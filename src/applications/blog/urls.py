from django.urls import path

from applications.blog import views

urlpatterns = [
    path("", views.all_post_view),
    path("new/", views.new_post_view),
]
