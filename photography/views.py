from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html')
def about_page(request):
    return render(request, 'about.html')
def contact_page(request):
    return render(request, 'contact.html')
def services_page(request):
    return render(request, 'services.html')
def starter_page(request):
    return render(request, 'stater.html')
def gallery_page(request):
    return render(request, 'gallery.html')
def gallery_single(request):
    return render(request, 'gallery-single.html')
