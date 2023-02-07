from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Departments, Employee


# Create your views here.
def home(request):
    data = Departments.objects.all().values()
    emp = Employee.objects.all().values()
    return HttpResponse(render(request, 'index.html', {'depts': zip(data, emp)}))


def add(request):
    return HttpResponse(render(request, 'add.html'))


def save(request):
    id = request.POST["dept_id"]
    name = request.POST["name"]
    managername = request.POST["manager"]
    e = Employee(name=managername)
    dept = Departments(dept_id=id, name=name, manager=e)
    e.save()
    dept.save()
    return redirect('/')


def update(request, id):
    dept = Departments.objects.get(manager_id=id)
    emp = Employee.objects.get(id=id)
    return HttpResponse(render(request ,'update.html', {'dept': dept, 'emp': emp}))


def edit(request, id):
    dept = Departments.objects.get(manager_id=id)
    emp = Employee.objects.get(id=id)
    dept_id = request.POST["dept_id"]
    name = request.POST["name"]
    managername = request.POST["manager"]
    dept.dept_id = dept_id
    dept.name = name
    emp.name = managername
    emp.save()
    dept.save()
    return redirect('/')


def delete(request, id):
    dept = Departments.objects.get(manager_id=id)
    emp = Employee.objects.get(id=id)
    dept.delete()
    emp.delete()
    return redirect('/')









