from django.shortcuts import render

def about(request):
    return render(request, "main/about_us.html")