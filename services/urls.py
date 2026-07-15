from django.urls import path
from . import views

urlpatterns = [
    path("service-inquiry/",views.service_inquiry,name="service_inquiry"),
    path(
        "services/<slug:slug>/",
        views.service_detail,
        name="service_detail",
    ),
]