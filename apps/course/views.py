from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
    "courses": Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def addCourse(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    data = {
    'courseId': Course.objects.get(id=id),
    "courses": Course.objects.filter(id=id)
    }
    return render(request, 'course/destroy.html', data)

def remove(request, id):
    data = {
    'courseId': Course.objects.get(id=id),
    "courses": Course.objects.filter(id=id).delete()
    }
    return redirect('/')
