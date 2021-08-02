
from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    if(request.method=='POST'):
        val = request.POST.get("radiobtn")
        print(val)

    return render(request,"Home/index.html")
