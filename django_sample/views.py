from django.shortcuts import render

def mainpage_view(request):
    template = "mainpage.html"
    context = {}
    return render(request,template,context)