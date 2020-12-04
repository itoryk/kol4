from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("applications.landing.urls")),
    path("h/", include("applications.hello.urls")),
    path("e/", lambda _r: 1 / 0),
    path("b/", include("applications.blog.urls")),
]
