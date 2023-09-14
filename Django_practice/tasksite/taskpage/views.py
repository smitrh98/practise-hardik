from django.shortcuts import render

# Create your views here.
#render is shortcut method for HttpResponse and loader

def index(request):
    context = { 'name' : "Hardik"}
    return render(request, "taskpage/index.html", context)