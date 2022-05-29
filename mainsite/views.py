from django.shortcuts import render

from blog.models import Blogs
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.

def index_home(request):
    page_details=Blogs.objects.extra(where=["LENGTH(blog_content_original) - LENGTH(REPLACE(blog_content_original, ' ', ''))+1 > %s"], params=[1000]).filter(~Q(category="people"))[:60]
    page_details_header={}
    page_details_header['page_titel']="World News Headlines, Latest International News, World Breaking News - ToolsBand"
    page_details_header['page_description']="World News: ToolsBand news brings the latest world news headlines, Current International breaking news world wide. In depth analysis and top news headlines world wide."
    page_details_header['keyword']="news, latest news, today news, breaking news, news headlines, bollywood news, India news, top news, political news, business news, technology news, sports news"
    page_details_header['author']="Bibekananda Bhuyan"
    page_details={"page_details":page_details,"page_details_header":page_details_header}
    
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


