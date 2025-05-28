from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from core.models import Legislation, LegislationFile

def legislation_file_list(request):
    """List all legislation files across all categories"""
    files = LegislationFile.objects.all().order_by('-timestamp')
    
    # Optional filtering by category
    category_slug = request.GET.get('category')
    if category_slug:
        files = files.filter(category__slug=category_slug)
    
    # Pagination
    paginator = Paginator(files, 10)  # 10 files per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get all categories for filter dropdown
    categories = Legislation.objects.all().order_by('slug')
    
    context = {
        'files': page_obj,
        'categories': categories,
        'selected_category': category_slug,
        'total_count': files.count()
    }
    return render(request, 'legislation/list.html', context)


def legislation_file_detail(request, file_id):
    """Get single legislation file by ID"""
    file = get_object_or_404(LegislationFile, id=file_id)
    
    context = {
        'file': file,
        'category': file.category
    }
    return render(request, 'legislation/detail.html', context)