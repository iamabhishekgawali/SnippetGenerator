
from django.shortcuts import render
from django.http import HttpResponse

def Convert(List,Description,tag,code,texteditor):
    pass

def home(request):
    

    List = {
            'text' : "Your Snippet will be generated here",
            'Description' : "Description..",
            'tag' : "Tab Trigger .. ",
            'code' : "Enter your code here :)",
             
        }
    

    if(request.method=='POST'):
        texteditor = request.POST.get("radiobtn")
        Description = request.POST.get("description")
        tag = request.POST.get("tag")
        code = request.POST.get("code")


        print(texteditor)
        print(Description)
        print(tag)
        print(code)
    
    return render(request,"Home/index.html",{"List": List })


