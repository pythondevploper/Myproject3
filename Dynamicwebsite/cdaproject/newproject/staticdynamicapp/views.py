from django.shortcuts import render
from . models import Bigd
from . models import Great
from . models import Goose
from . models import Goofy
from . models import Gog
# Create your views here.
def demo(request):
    obj=Bigd.objects.all()
    obj2=Great.objects.all()
    obj3=Goose.objects.all()
    obj4=Goofy.objects.all()
    obj5=Gog.objects.all()
    return render (request,'index.html',{'result':obj,'result2':obj2,'result3':obj3,'result4': obj4,'result5':obj5}) 
