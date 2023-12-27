from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import QeydiyyatForm, SinaqQeydiyyatForm, ElaqeForm


def qeydiyyat(request):
    form = QeydiyyatForm()
    
    if request.method == 'POST':
        form = QeydiyyatForm(request.POST)
        
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render(request, 'qeydiyyat/qeydiyyat.html', context)

def sinaqqeydiyyat(request):
    form = SinaqQeydiyyatForm()

    if request.method == 'POST':
        form = SinaqQeydiyyatForm(request.POST)

        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'qeydiyyat/sinaqqeydiyyat.html', context)

def elaqe(request):
    form = ElaqeForm()

    if request.method == 'POST':
        form = ElaqeForm(request.POST)

        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'qeydiyyat/elaqe.html', context)