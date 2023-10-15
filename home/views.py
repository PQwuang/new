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
def sign_up(request):
    return render(request, 'pages/sign_up.html')
def register(request):
    return render(request, 'pages/register.html')
def editprofile(request):
    return editprofile(request, 'pages/editprofile.html')
# def password_change_form(request):
#     return password_change_form(request, 'pages/password_change_form.html')
