from django.urls import path
from .views import home, NewHelloCreateView

urlpatterns = [
    path("", home, name="home"),
    path("newhellos/create/", NewHelloCreateView.as_view(), name="create_newhello"),
]
