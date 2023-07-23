from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
def about(request):
    return render(request, 'pages/about.html')
def introduction(request):
    return render(request, 'pages/introduction.html')
def dodientu(request):
    return render(request, 'pages/dodientu.html')
def bachhoa(request):
    return render(request, 'pages/bachhoa.html')
def trangsuc(request):
    return render(request, 'pages/trangsuc.html')
def sign_in(request):
    return render(request, 'pages/sign_in.html')
def register(request):
    return render(request, 'pages/register.html')
