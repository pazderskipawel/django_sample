from django.shortcuts import render


# Create your views here.
def twchat_view(request):
    return render(request, "twitchchat/twitchchat.html", {})
