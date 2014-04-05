from django.shortcuts import render, HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html", {
        })

def echo(request):
    user_input = request.POST['user_input']
    return render(request, "index.html", {
        'echo' : user_input
        })
