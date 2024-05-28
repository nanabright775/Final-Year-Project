# business_card/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BusinessCardTemplate, UserBusinessCard
from .forms import UserBusinessCardForm

@login_required
def create_business_card(request):
    if request.method == 'POST':
        form = UserBusinessCardForm(request.POST)
        if form.is_valid():
            business_card = form.save(commit=False)
            business_card.user = request.user
            business_card.save()
            return redirect('business_card_detail', business_card_id=business_card.id)
    else:
        form = UserBusinessCardForm()

    templates = BusinessCardTemplate.objects.all()
    return render(request, 'business_card/create_business_card.html', {'form': form, 'templates': templates})

@login_required
def business_card_detail(request, business_card_id):
    business_card = get_object_or_404(UserBusinessCard, id=business_card_id)
    return render(request, 'business_card/business_card_detail.html', {'business_card': business_card})
