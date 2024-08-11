from django.http import HttpResponse
from django.shortcuts import render
from .models import Collection, Piece
# Create your views here.
def index(request):
    all_collection=Collection.objects.all()
    context={
        "all_collection" : all_collection
    }
    return render(request,"webone\\webonetemplate.html",context)

def details(request,webone_id):
    return HttpResponse("<h1>The webone id is: "+str(webone_id)+"</h1>")