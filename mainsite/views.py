from django.shortcuts import render
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def index_home(request):
    return render(request,"home.html")
    
def terms_and_condition(request):
    return render(request,"terms-and-condition.html")

    
def privacy_policy(request):
    return render(request,"privacy-policy.html")


def contact(request):
    return render(request,"contact.html")


