import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from core import models
from django.contrib import messages
from django.utils import timezone


def vacancies(request):
    template_name = "vacancy/vacancies.html"
    vacancy_ = models.Vacancy.objects.filter(published = True).filter(closing_date__gte=timezone.now().date())
    page = request.GET.get('page', 1)
    paginator = Paginator(vacancy_, 8)
    vacancy = paginator.page(page)
    return render(request,template_name,{'vacancies':vacancy})

def vacancy_details(request, slug, id):
    template_name = "vacancy/vacancy_details.html"
    obj = get_object_or_404(models.Vacancy, slug=slug, id=id)
    return render(request,template_name,{'obj':obj})