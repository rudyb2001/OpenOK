"""openok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, search_view, course_view, create_course_view
from courses.views import (
    course_detail_view, 
    course_create_view, 
    course_edit_view, 
    dynamic_lookup_view,
    course_delete_view,
    course_list_view
    )

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('courses/', course_list_view, name="course-lists"),
    #path('course/', course_view),
    #path('create/', course_create_view),
    path('courses/create/', course_create_view),
    path('admin/', admin.site.urls),
    #path('course/', course_detail_view),
    path('courses/<int:my_id>/', dynamic_lookup_view, name='course-detail'),
    # ^^ int:my_id is creating some variable id, not referencing anything
    # ^^ That is an argument that we are creating for dynamic_lookup_view
    path(
        'courses/<int:my_id>/delete/',
        course_delete_view,
        name='course-delete'
        ),
    path(
        'courses/<int:my_id>/edit/',
        course_edit_view,
        name='course-edit'
        ),
]
