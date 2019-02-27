from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpApplication

# Create your views here.
def index(request):
    return HttpResponse("WELCOME")

def empForm(request):
    print("Calling EmpForm Beginning")
    if(request.method == 'POST'):
        print("Post")
        print(request.POST)
        context = {
            "name": request.POST["name"],
            "birthday": request.POST["birthday"],
            "applyingTo": request.POST["applyingTo"],
            "salary": request.POST["salary"],
        }
        return render(request, 'frmApp/infoPage.html', context)
    else:
        print("Else")
        appForm = EmpApplication()
        return render(request, 'frmApp/index.html', {"appForm": appForm})
