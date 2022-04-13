from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Blog,Contact,Service,Slider,Project,Testimonial,Author


def index(request):
    sliders = Slider.objects.all()
    context= {
        "is_index": True,
        "sliders": sliders,
        "number": 30,
    }
    return render(request,'web/index.html',context)


def about_us(request):
    context= {
        "is_abous_us":True
    }
    return render(request,'web/about-us.html',context)


def blog_single_with_sidebar(request):
    context= {
        "is_blog_single_with_sidebar":True
    }
    return render(request,'web/blog-single-with-sidebar.html',context)


def blog_with_sidebar(request):
    context= {
        "is_blog_with_sidebar":True
    }
    return render(request,'web/blog-with-sidebar.html',context)


def contact(request):
    context= {
        "is_contact":True
    }
    return render(request,'web/contact.html',context)


def index(request):
    context= {
        "is_index":True
    }
    return render(request,'web/index.html',context)


def index_startup(request):
    context= {
        "is_index_startup":True
    }
    return render(request,'web/index-startup.html',context)


def project_details(request):
    context= {
        "is_project_details":True
    }
    return render(request,'web/project-details.html',context)


def projects(request):
    context= {
        "is_projects":True
    }
    return render(request,'web/projects.html',context)


def services_two(request):
    context= {
        "is_services_2":True
    }
    return render(request,'web/services-2.html',context)


def services_details(request):
    context= {
        "is_services_details":True
    }
    return render(request,'web/services-details.html',context)


def notfound(request):
    context= {
        "is_notfound":True
    }
    return render(request,'web/404.html',context)
