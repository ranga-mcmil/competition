from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.core.paginator import Paginator
from core.models import Folder, Image, Media

# Create your views here.

def folders(request):
    template_name = 'gallery/folders.html'
    folders_ = Folder.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(folders_, 8)
    folders = paginator.page(page)
    context = {
        'folders':folders,
    }
    return render(request, template_name, context)

def folders_images(request,slug):
    template_name = 'gallery/folders_images.html'
    folder = get_object_or_404(Folder,slug=slug)
    images_ = Image.objects.filter(folder = folder)
    page = request.GET.get('page', 1)
    paginator = Paginator(images_, 12)
    images = paginator.page(page)
    context = {
        'obj':folder,
        'images':images
    }
    return render(request, template_name, context)

def media(request):
    template_name = 'gallery/media.html'
    folders_ = Media.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(folders_, 8)
    media = paginator.page(page)
    context = {
        'medias':media,
    }
    return render(request, template_name, context)