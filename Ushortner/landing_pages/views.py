# landing_pages/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LandingPageForm
from .models import LandingPage
from django.utils.text import slugify

@login_required
def create_landing_page_view(request):
    if request.method == 'POST':
        form = LandingPageForm(request.POST, request.FILES)
        if form.is_valid():
            landing_page = form.save(commit=False)
            landing_page.user = request.user
            landing_page.slug = slugify(landing_page.title)
            landing_page.save()
            return redirect('landing_page', slug=landing_page.slug)
    else:
        form = LandingPageForm()
    return render(request, 'landing_pages/create_landing_page.html', {'form': form})

def landing_page_view(request, slug):
    landing_page = get_object_or_404(LandingPage, slug=slug)
    return render(request, 'landing_pages/landing_page.html', {'landing_page': landing_page})


@login_required
def user_landing_pages_view(request):
    landing_pages = LandingPage.objects.filter(user=request.user)
    return render(request, 'landing_pages/user_landing_pages.html', {'landing_pages': landing_pages})

@login_required
def update_landing_page_view(request, slug):
    landing_page = get_object_or_404(LandingPage, slug=slug, user=request.user)
    if request.method == 'POST':
        form = LandingPageForm(request.POST, request.FILES, instance=landing_page)
        if form.is_valid():
            form.save()
            return redirect('landing_page', slug=landing_page.slug)
    else:
        form = LandingPageForm(instance=landing_page)
    return render(request, 'landing_pages/create_landing_page.html', {'form': form})



@login_required
def delete_landing_page_view(request, slug):
    landing_page = get_object_or_404(LandingPage, slug=slug, user=request.user)
    if request.method == 'POST':
        landing_page.delete()
        return redirect('user_landing_pages')
    return render(request, 'landing_pages/delete_landing_page.html', {'landing_page': landing_page})


@login_required
def landing_page_detail(request, slug):
    landing_page = get_object_or_404(LandingPage, slug=slug)
    return render(request, 'landing_pages/landing_page_detail.html', {'landing_page': landing_page})
