from django.urls import path
from .views import home, HelloCreateView

urlpatterns = [
    path("", home, name="home"),
    path("hellos/create/", HelloCreateView.as_view(), name="create_hello"),
]
