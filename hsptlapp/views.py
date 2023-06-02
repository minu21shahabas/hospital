from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'frontview.html')
def about(request):
    return render(request,'aboutus.html')
def special(request):
    return render(request,'special.html')
def gal(request):
    return render(request,'gallery.html')
def con(request):
    return render(request,'contact.html')
def homes(request):
    return render(request,'homepage.html')
def log(request):
    return render(request,'login.html')
def sign(request):
    return render(request,'sign_up.html')
def out(request):
    return render(request,'frontview.html')
