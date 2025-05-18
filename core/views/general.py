from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from core.email import Email
from core import models
from core.forms import ContactForm
from django.contrib import messages

# Create your views here.

def home(request):
    template_name = "general/index.html"
    divisions = models.Division.objects.all()
    slider = models.Slider.objects.all()
    emblems = models.Emblem.objects.all()
    latest_news = models.BlogPost.objects.filter(published = True)[:3]
    return render(request,template_name,{'sliders':slider,'divisions':divisions,'latest_news':latest_news,'emblems':emblems})

def contact(request):
    template_name = "general/contact.html"
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            email = Email(
	            subject="Contact us",
				recipient_list=['ngonimug@gmail.com'],
				message=f"""
				<p>Testing</p>
				""",
            )
            email.send()
            print(f"Cleaned Data : {cleaned_data}")
            messages.success(request,"Message successfully received, we will contact you as soon as possible.")
            return redirect('general:contact')
    return render(request,template_name,{'form':form})


def downloads(request, category):
    template_name = "general/downloads.html"
    downloads_ = models.Download.objects.filter(category = category)
    page = request.GET.get('page', 1)
    paginator = Paginator(downloads_, 8)
    downloads = paginator.page(page)
    return render(request,template_name,{'downloads':downloads,'category':category})

def teams(request, category):
    template_name = "general/teams.html"
    items = models.Team.objects.filter(category = category)
    return render(request,template_name,{'items':items,'category':category})

def legislation(request, slug):
    template_name = "general/legislation.html"
    obj = get_object_or_404(models.Legislation, slug =slug)
    return render(request,template_name,{'obj':obj})