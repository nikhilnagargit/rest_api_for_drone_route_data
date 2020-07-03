
from django.urls import path, include
from api.views import home, FindPathView
urlpatterns = [
    path('', home, name="home"),
    path('find-path/', FindPathView.as_view(), name='find-path')

]
