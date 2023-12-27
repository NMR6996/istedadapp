from django.urls import path
from . import views

urlpatterns = [
    path("qeydiyyat", views.qeydiyyat, name="qeydiyyat"),
    path("sinaqqeydiyyat", views.sinaqqeydiyyat, name="sinaqqeydiyyat"),
    path("elaqe", views.elaqe, name="elaqe"),
]