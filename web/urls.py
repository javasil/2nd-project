from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("",views.index,name = "index"),
    path("about/",views.about_us,name = "about-us"),
    path("blog_single_with_sidebar/",views.blog_single_with_sidebar,name = "blog_single_with_sidebar"),
    path("blog_with_sidebar/",views.blog_with_sidebar,name = "blog_with_sidebar"),
    path("contact/",views.contact,name = "contact"),
    path("notfound/",views.notfound,name = "notfound"),
    path("index_startup/",views.index_startup,name = "index_startup"),
    path("project_details/",views.project_details,name = "project_details"),
    path("projects/",views.projects,name = "projects"),
    path("services_two/",views.services_two,name = "services_two"),
    path("services_details/",views.services_details,name = "services_details"),




]