from django.shortcuts import render

# Home page view
def index(request):
    return render(request, 'myproject/index.html')

def portfolio(request):
    return render(request, 'myproject/portfolio.html')

def contact(request):
    return render(request, 'myproject/contact.html')

def service(request):
    return render(request, 'myproject/service.html')

def blog(request):
    return render(request, 'myproject/blog.html')

def about(request):
    return render(request, 'myproject/about.html')

def vision(request):
    return render(request, 'myproject/vision.html')

def blog1(request):
    return render(request, 'myproject/blog1.html')

def blog2(request):
    return render(request, 'myproject/blog2.html')

def blog3(request):
    return render(request, 'myproject/blog3.html')