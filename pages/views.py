from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('feed')
    else:
        return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')
