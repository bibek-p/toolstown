from django.urls import path
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    path("news/<weblink>",views.details,name="Blog Details Page"),
    path("",views.index,name="Blog Index"),
    path("create",views.createpost,name="createpost Index"),
    path("headcheck",views.is_headingexits,name="headcheck Index"),
    # path("feed/rss",views.rssfeed,name="Rssfeed Index"),
    path('feed/rss', LatestPostsFeed(), name='latest_feed'),
    # path("/<cat>",views.index,name="Blog Index"),
    path("<cat>",views.blog_cat,name="blog_cat Page"),


   
]