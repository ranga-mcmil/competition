from django.shortcuts import get_object_or_404, render, redirect
from core.models import Division
from django.contrib import messages
from django.core.paginator import Paginator


def division_details(request, category):
    template_name = 'about/division_details.html'
    obj = get_object_or_404(Division, category= category)
    divisions = Division.objects.exclude(slug = obj.slug)
    return render(request, template_name, { "obj":obj, 'divisions':divisions })

def background_or_mandate(request):
    template_name = 'about/background_or_mandate.html'
    return render(request, template_name)