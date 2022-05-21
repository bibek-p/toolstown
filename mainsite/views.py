from django.shortcuts import render

from blog.models import Blogs
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index_home(request):
    page_details=Blogs.objects.all()[:60]
    page_details={"page_details":page_details}
    return render(request, 'blog/index_sample.html', page_details)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

# def index_home(request):
#     return render(request,"home.html")
    
def terms_and_condition(request):
    return render(request,"terms-and-condition.html")

    
def privacy_policy(request):
    return render(request,"privacy-policy.html")


def contact(request):
    return render(request,"contact.html")
def about_us(request):
    return render(request,"about-us.html")


