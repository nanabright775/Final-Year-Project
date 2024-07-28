# business_card/views.py

from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import BusinessCardTemplate, UserBusinessCard
from .forms import UserBusinessCardForm
from PIL import Image, ImageDraw, ImageFont
import qrcode


#bussiness card creation
@login_required
def create_business_card(request):
    if request.method == 'POST':
        form = UserBusinessCardForm(request.POST, request.FILES)
        if form.is_valid():
            business_card = form.save(commit=False)
            business_card.user = request.user

            if not business_card.template and not business_card.custom_template_image:
                form.add_error('template', 'Please select a template or upload a custom template image.')
                form.add_error('custom_template_image', 'Please select a template or upload a custom template image.')
            else:
                business_card.save()
                return redirect('business_card_detail', pk=business_card.pk)
    else:
        form = UserBusinessCardForm()

    templates = BusinessCardTemplate.objects.all()
    return render(request, 'business_card/create_business_card.html', {'form': form, 'templates': templates})

#bussiness card details
@login_required
def business_card_detail(request, pk):
    business_card = get_object_or_404(UserBusinessCard, pk=pk)
    return render(request, 'business_card/business_card_detail.html', {'business_card': business_card})

#rendering busssiness card as image
@login_required
def render_business_card(request, business_card_id):
    business_card = get_object_or_404(UserBusinessCard, id=business_card_id)
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename="{business_card.name}_business_card.png"'
    return response

#listing all the bussiness card a user has created
@login_required
def business_card_list(request):
    business_cards = UserBusinessCard.objects.filter(user=request.user)
    return render(request, 'business_card/business_card_list.html', {'business_cards': business_cards})

#updating a bussiness card
@login_required
def business_card_update(request, pk):
    business_card = get_object_or_404(UserBusinessCard, pk=pk, user=request.user)
    if request.method == 'POST':
        form = UserBusinessCardForm(request.POST, instance=business_card)
        if form.is_valid():
            form.save()
            return redirect('business_card_list')
    else:
        form = UserBusinessCardForm(instance=business_card)
    return render(request, 'business_card/business_card_form.html', {'form': form})

#deleting a bussiness card
@login_required
def business_card_delete(request, pk):
    business_card = get_object_or_404(UserBusinessCard, pk=pk, user=request.user)
    if request.method == 'POST':
        business_card.delete()
        return redirect('business_card_list')
    return render(request, 'business_card/business_card_confirm_delete.html', {'business_card': business_card})

