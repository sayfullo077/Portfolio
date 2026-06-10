from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.post_list, name="blog"),
    path("blog/<slug:slug>/", views.post_detail, name="post_detail"),
]
