from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.core.paginator import Paginator
from core.models import Tender

# Create your views here.


def tenders(request):
    template_name = 'tenders/tenders.html'
    tenders_ = Tender.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tenders_, 10)
    tenders = paginator.page(page)
    context = {
        'tenders':tenders,
    }
    return render(request, template_name, context)