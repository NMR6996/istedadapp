from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index, name="index"),
    path("haqqimizda", views.haqqimizda, name="haqqimizda"),
    path("struktur", views.struktur, name="struktur"),
    path("filiallar", views.filiallar, name="filiallar"),
    path("muellimler", views.muellimler, name="muellimler"),
    path("kurslar", views.kurslar, name="kurslar"),
    path("kurs_details/<slug:slug>", views.kurs_details, name="kurs_details"),
    path("xeber_details/<slug:slug>", views.xeber_details, name="xeber_details"),
    path("sinaq_details/<int:id>", views.sinaq_details, name="sinaq_details"),
    path("tedbirler", views.tedbirler, name="tedbirler"),
    path("qeydiyyatt", views.qeydiyyatt, name="qeydiyyat"),
    path("media", views.media, name="media"),
    path("sinaqnetice", views.sinaqlar, name="sinaqnetice"),
    path("sinaqcavab", views.sinaqcavab, name="sinaqcavab"),
    path("adminsinaqcavab", views.adminsinaqcavab, name="adminsinaqcavab"),
]
