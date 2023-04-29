from django.shortcuts import render, redirect
from .models import *
from .form import PersonForm
from django.views import generic
# Create your views here.


def index(request):
    tests = Test.objects.all()
    context = {
        'tests':tests
    }
    return render(request, 'test/index.html', context)


def show(request, id):
    test = Test.objects.get(id=id)
    form = PersonForm
    context = {
        'test':test,    
        'form':form
    }
    return render(request, 'test/show.html', context)

def chek(request):
    form = PersonForm(request.POST)
    test = Test.objects.get(id=request.POST.get('test'))
    num = num_point(request,test)
    if form.is_valid():
        person = form.save(commit=False)
        person.test = test
        person.point = num
        count = person.test.question.count()
        person.result = (100/int(count))*person.point
        person.save()
    return redirect('index')

def num_point(request, test):
    num = 0
    for i in test.question.all():
        a= request.POST.get(f'question{i.id}')
        choice = Choice.objects.get(id=a)
        if choice.pr:
            num +=1
    return num

# class I(generic.ListView):
#     def get(self, request, *args, **kwargs):
#         self.request.POST.
#         return super().get(request, *args, **kwargs)





