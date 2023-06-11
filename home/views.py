from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
def about(request):
    return render(request, 'pages/about.html')
def introduction(request):
    return render(request, 'pages/introduction.html')