from django.urls import path

from . import views



urlpatterns = [
    # API to post comment
    path('/feedComment/', views.feedComment, name="feedComment"),

    path('', views.index, name="Home"),
    path('find-jobs/', views.findjobs, name="find-job"),
    path('feed/<str:slug>/', views.detail, name="detail"),
    path('tags/<slug:slug>/', views.tags, name="tags"),
    ]
