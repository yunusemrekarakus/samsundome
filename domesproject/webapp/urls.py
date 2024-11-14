from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("services", views.onaylanmis_yorumlar_view, name="services"),
    # path("project", views.project, name="project"),
    path("satisfactionform", views.otel_memnuniyet_view, name="satisfactionform"), 
    path("succesfull", views.tesekkurler, name="succesfull"),
    path("", views.home)
    
]