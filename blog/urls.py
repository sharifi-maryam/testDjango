from django.urls import path, include
from .views import ArticleList
from .views import Home


app_name = "blog"

urlpatterns = [
    path("" , ArticleList.as_view(), name="list"),
    path("", Home, name='home')
]