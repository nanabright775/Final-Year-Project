# landing_pages/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import LandingPage
from .forms import LandingPageForm

def landing_page_view(request, page_id):
    landing_page = get_object_or_404(LandingPage, id=page_id)
    return render(request, 'landing_pages/landing_page.html', {'landing_page': landing_page})

def create_landing_page_view(request):
    if request.method == 'POST':
        form = LandingPageForm(request.POST, request.FILES)
        if form.is_valid():
            landing_page = form.save()
            return redirect('landing_page', page_id=landing_page.id)
    else:
        form = LandingPageForm()
    return render(request, 'landing_pages/create_landing_page.html', {'form': form})
