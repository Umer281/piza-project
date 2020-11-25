from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .order import PizaOrderForm
from .models import Piza
# Create your views here.
def order(request):
    if request.method=='POST':
        form=PizaOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'pizza has been ordered')
            return redirect('items')
    else:
        form=PizaOrderForm()
        return render(request,'Piza/order.html',{'form':form})


def items(request):
    return render(request,'Piza/items.html')


def storeditems(request):
    piza_list=Piza.objects.all()
    return render(request,'Piza/storeditems.html',{'piza_list':piza_list})


    