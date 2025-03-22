from django.shortcuts import render,redirect
from .forms import DiscussionForm,ModuleForm
from .models import Module,Discussion

# Create your views here.

def create_module(request):
    if request.method=="POST":
        form=ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")     
    else:
        form=ModuleForm()       
    return render(request,"discussions/index.html",{
        "name":form['name'],
        "description":form["description"],
      
      
    })
    
def list_of_modules(request):
    modules=Module.objects.all()
    return render(request,"discussions/index.html",{"modules":modules})



def list_of_filtered_discussions(request,mdl):
    discussions=Discussion.objects.filter(module__name=mdl)
    return render(request,"discussions/discussions.html",{"discussions":discussions})


def list_of_discussions(request):
    discussions=Discussion.objects.all()
    return render(request,"discussions/discussions.html",{"discussions":discussions})

