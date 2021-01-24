from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CourseForm, RawCourseForm
from .models import Course
# Create your views here.

def course_list_view(request):
    queryset = Course.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "courses/course_list.html", context)

def course_delete_view(request, my_id):
    #obj = Course.objects.get(id=my_id)
    obj = get_object_or_404(Course, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "courses/course_delete.html", context)

def dynamic_lookup_view(request, my_id):
    #obj = Course.objects.get(id=my_id)
    #obj = get_object_or_404(Course, id=my_id)
    # ^^ This method or whatever is wonderful.
    # If someone tries accessing an invalid object
    # (or if no objects yet exist or that current object doesn't exist)
    # the website will throw a 404 error.
    try:
        obj = Course.objects.get(id=my_id)
        boo = True
    except Course.DoesNotExist:
        raise Http404
        #obj = null
        boo = False
    context = {
        "object": obj,
        "bool": boo
    }
    return render(request, "courses/course_detail.html", context)

def course_edit_view(request, my_id):
    obj = get_object_or_404(Course, id=my_id)
    form = CourseForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form = CourseForm()
    context = {
        'form': form
    }
    return render(request, "courses/course_create.html", context)

def course_create_view(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CourseForm()
    context = {
        "form": form
    }
    return render(request, "courses/course_create.html", context)

def course_detail_view(request):
    obj = Course.objects.get(id=1)
    #context = {
    #    "title" : obj.title,
    #    "description" : obj.description,
    #    "videos" : obj.videos
    #}
    context = {
        "object": obj
    }
    return render(request, "courses/course_detail.html", context)