from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from core.models import ClientCharter


def client_charter_list(request):
    """List all published client charters"""
    charters = ClientCharter.objects.filter(published=True).order_by('-timestamp')
    
    # Pagination
    paginator = Paginator(charters, 5)  # 5 charters per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'charters': page_obj,
        'total_count': charters.count()
    }
    return render(request, 'charters/list.html', context)


def client_charter_detail(request, slug):
    """Get single client charter by slug"""
    charter = get_object_or_404(ClientCharter, slug=slug, published=True)
    
    context = {
        'charter': charter
    }
    return render(request, 'charters/detail.html', context)
