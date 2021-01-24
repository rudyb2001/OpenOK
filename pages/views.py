from django.http import HttpResponse # Import this to change website
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # these parameters are python-specific
    #phrase = "<h1>Anya is a Butthead</h1>" # string of HTML code
    #return HttpResponse(phrase)
    my_context = {
        "my_text": "This is for finding courses",
        "my_number": 123,
        "my_list": [123, 456, 1232],
        "this_is_true": True
    }
    return render(request, "home.html", my_context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def search_view(request, *args, **kwargs):
    
    return render(request, "search.html", {})

def course_view(request, *args, **kwargs):
    return render(request, "course.html", {})

def create_course_view(request, *args, **kwargs):
    #print(request.user)
    return render(request, "create_course.html", {})